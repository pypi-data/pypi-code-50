# Faust RockDB store extended to use an S3 bucket as a backing store
from pathlib import Path
import aiobotocore
from typing import (
    Any,
    Callable,
    DefaultDict,
    Dict,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    NamedTuple,
    Optional,
    Set,
    Tuple,
    Union,
    cast,
    AsyncIterable,
)
import rocksdb
import rocksdb.errors
import math
import hashlib
import base64
import io
import os
import errno
import datetime
from faust.stores.rocksdb import Store as RocksDBStore
from faust.types import AppT, CollectionT, EventT, TP
from faust.sensors.statsd import StatsdMonitor
from mode import Service


class Store(RocksDBStore):
    """Extended RocksDB Store"""

    def __init__(self, url, app, table, *args, **kwargs):
        super().__init__(url, app, table, *args, **kwargs)

        if hasattr(self.app.conf, "rocksdbs3_backup_frequency_seconds"):
            self._backup_frequency_seconds = self.app.conf.rocksdbs3_backup_frequency_seconds
        else:
            self._backup_frequency_seconds = 60 * 5

        self._backup_engines = {}
        self._last_backup = {}

        bucket = self.app.conf.rocksdbs3_bucket
        if bucket is not None:
            if not bucket.endswith("/"):
                bucket += "/"
            slash = bucket.find("/")
            self.s3bucket_name = bucket[:slash]
            self._s3bucket_prefix = bucket[slash + 1:]
        else:
            self.s3bucket_name = None
            self._s3bucket_prefix = None

    @Service.timer(60.0)
    async def _publish_stats(self) -> None:
        """
            Publish Rocksdb properties to statsd every 60 seconds.
        """
        if isinstance(self.app.monitor, StatsdMonitor):
            statsd_client = cast(StatsdMonitor, self.app.monitor).client

            for partition in self._dbs:
                db = self._db_for_partition(partition)
                if db is not None:
                    # property descriptions available at: https://github.com/facebook/rocksdb/blob/36c504be17d9e7c81567ba0732ef81632d3d2c74/include/rocksdb/db.h#L593
                    for prop_name in [
                        "estimate-num-keys",
                        "estimate-live-data-size",
                        "size-all-mem-tables",
                        "total-sst-files-size",
                        "estimate-table-readers-mem",
                        "actual-delayed-write-rate",
                        "estimate-oldest-key-time",
                        "live-sst-files-size",
                        "num-entries-active-mem-table",
                    ]:
                        try:
                            value = db.get_property(
                                f"rocksdb.{prop_name}".encode("utf-8")
                            )
                            statsd_client.gauge(
                                f"rocksdb.{self.basename}.{partition}.{prop_name}",
                                int(value.decode("utf-8")),
                            )
                        except AttributeError:
                            statsd_client.incr(
                                f"rocksdb.{self.basename}.{prop_name}.AttributeError",
                            )

        # Backup databases for active partitions (not standbys) every 'backup_frequency_seconds'
        if self.s3bucket_name is not None and self._backup_frequency_seconds > 0:
            actives = self.app.assignor.assigned_actives()
            topic = self.table._changelog_topic_name()

            for partition in self._dbs:
                tp = TP(topic=topic, partition=partition)
                if tp in actives:
                    last_backup = self._last_backup.get(partition, datetime.datetime.min)
                    self.log.debug("publish_stats: last_backup is: %s for partition %d", last_backup, partition)
                    if last_backup is not None and datetime.datetime.utcnow() > last_backup + datetime.timedelta(
                            seconds=self._backup_frequency_seconds
                    ):
                        self.log.debug("publish_stats:  backup triggered. last backup at: %s", last_backup)
                        await self.backup_database(partition)

    async def on_rebalance(
            self,
            table: CollectionT,
            assigned: Set[TP],
            revoked: Set[TP],
            newly_assigned: Set[TP],
    ) -> None:
        """Rebalance occurred.

        Arguments:
            table: The table that we store data for.
            assigned: Set of all assigned topic partitions.
            revoked: Set of newly revoked topic partitions.
            newly_assigned: Set of newly assigned topic partitions,
                for which we were not assigned the last time.
        """
        if self.s3bucket_name is not None:
            await self.backup_databases(table, revoked)
        self.revoke_partitions(table, revoked)

        if self.s3bucket_name is not None:
            await self.restore_databases(table, newly_assigned)
        await self.assign_partitions(table, newly_assigned)

    async def backup_databases(self, table: CollectionT, tps: Set[TP]) -> None:
        """Does incremental backup of rocksdb to local folder {app.conf.tabledir}/{table-name}-{partition-number}.backup
        :param table - The table to back up:
        :param tps: - The partitions that need backing up
        :return:
        """
        actives = self.app.assignor.assigned_actives()
        for tp in tps:
            if tp.topic in table.changelog_topic.topics and tp in actives:
                await self.backup_database(tp.partition)

    async def backup_database(self, partition):
        db = self._db_for_partition(partition)
        if db is not None:
            self.log.info("backup start partition=%d", partition)

            backup = self._backup_engine_for_partition(partition)
            backup.create_backup(db, flush_before_backup=True)

            # Keep just the most recent backup
            backup.purge_old_backups(1)
            try:
                await self.sync_to_s3(partition)

                self._last_backup[partition] = datetime.datetime.utcnow()
                self.log.info("backup complete partition=%d", partition)
            except Exception as e:
                self.log.warn("Backup database partition %d failed.  Ignoring", partition,
                              exc_info=True)

    async def restore_databases(self, table: CollectionT, tps: Set[TP]) -> None:
        for tp in tps:
            if tp.topic in table.changelog_topic.topics:
                await self.restore_database(tp.partition)

    async def restore_database(self, partition: int):
        self.log.info("restore start partition=%d", partition)
        is_backup_present = await self.sync_from_s3(partition)

        if is_backup_present:
            backup = self._backup_engine_for_partition(partition)
            db_path = str(self.partition_path(partition))
            try:
                backup.restore_latest_backup(db_path, db_path)
            except Exception:
                self.log.warn("Restore database partition %d failed.  Ignoring", partition, exc_info=True)

        # Set last backup time so that backup thread doesn't immediately back up the database.
        self._last_backup[partition] = datetime.datetime.utcnow()
        self.log.info("restore complete partition=%d", partition)

    def _backup_engine_for_partition(self, partition: int) -> rocksdb.BackupEngine:
        if partition not in self._backup_engines:
            self._backup_engines[partition] = rocksdb.BackupEngine(str(self.backup_path(partition)))
        return self._backup_engines[partition]

    def backup_path(self, partition: int) -> Path:
        """Return :class:`pathlib.Path` to db file of specific partition."""
        p = self.path / self.basename
        return self._path_with_suffix(
            p.with_name(f"{p.name}-{partition}"), suffix=".backup"
        )

    def s3bucket_prefix(self, partition: int) -> str:
        return f"{self._s3bucket_prefix}{self.basename}-{partition}/"

    async def sync_to_s3(self, partition: int) -> None:
        """Copy new files in backup folder to shared S3 bucket"""

        folder = self.backup_path(partition)
        files = self.list_folder_files(str(folder))

        self.log.debug("starting sync_to_s3 %s", str(folder))

        session = aiobotocore.get_session()
        async with session.create_client("s3", region_name="us-west-2") as s3:

            bucket_keys = await self.bucket_keys(
                s3, self.s3bucket_name, prefix=self.s3bucket_prefix(partition)
            )

            # Upload all the new files to S3
            for filename in files:
                if filename not in bucket_keys:
                    self.log.debug("Copy to S3=%s", filename)
                    await self.upload_file(
                        s3,
                        folder / filename,
                        self.s3bucket_name,
                        self.s3bucket_prefix(partition) + filename,
                    )

            # Delete all the unnecessary files from the S3 bucket
            delete_keys = [{"Key": self.s3bucket_prefix(partition) + k} for k in bucket_keys if k not in files]
            if len(delete_keys) > 0:
                self.log.debug("Delete S3 bucket files %s", str(delete_keys))
                await s3.delete_objects(
                    Bucket=self.s3bucket_name, Delete={"Objects": delete_keys}
                )

        self.log.debug("ending sync_to_s3 %s", str(folder))

    async def upload_file(self, s3, file: Path, bucket: str, key: str, bytes_per_chunk=5 * 1024 * 1024) -> None:
        source_size = file.stat().st_size
        chunks_count = int(math.ceil(source_size / float(bytes_per_chunk)))

        result = await s3.create_multipart_upload(Bucket=bucket, Key=key)
        upload_id = result["UploadId"]

        try:
            parts = []

            with file.open("rb") as fp:
                for i in range(chunks_count):
                    offset = i * bytes_per_chunk
                    remaining_bytes = source_size - offset
                    length = min([bytes_per_chunk, remaining_bytes])
                    part_num = i + 1

                    self.log.debug("Upload %s part %d of %d", key, part_num, chunks_count)

                    file_part = FilePart(fp, offset, length)
                    result = await s3.upload_part(
                        Bucket=bucket,
                        Key=key,
                        UploadId=upload_id,
                        PartNumber=part_num,
                        ContentLength=length,
                        ContentMD5=file_part.md5(),
                        Body=file_part,
                    )
                    etag = result["ETag"]

                    parts.append({"PartNumber": part_num, "ETag": etag})

            result = await s3.complete_multipart_upload(
                Bucket=bucket,
                Key=key,
                UploadId=upload_id,
                MultipartUpload={"Parts": parts},
            )
            self.log.info("upload_file %s done.  ETag=%s", key, result["ETag"])
        except:
            await s3.abort_multipart_upload(Bucket=bucket, Key=key, UploadId=upload_id)
            raise

    async def sync_from_s3(self, partition: int) -> bool:
        """Copy new files to backup folder from shared S3 bucket"""

        is_backup_present = False

        folder = self.backup_path(partition)
        files = self.list_folder_files(str(folder))

        self.log.debug("starting sync_from_s3 %s", str(folder))

        session = aiobotocore.get_session()
        async with session.create_client("s3", region_name="us-west-2") as s3:
            bucket_keys = await self.bucket_keys(
                s3, self.s3bucket_name, prefix=self.s3bucket_prefix(partition)
            )

            # Download all the new files from S3
            for key in bucket_keys:
                self.log.debug("Copy from S3=%s", key)
                if key not in files:
                    await self.download_file(
                        s3,
                        self.s3bucket_name,
                        self.s3bucket_prefix(partition) + key,
                        folder / key,
                    )
                    is_backup_present = True

            # Delete all the unnecessary files from the backup folder
            for filename in files:
                if filename not in bucket_keys:
                    os.remove(folder / filename)

        self.log.debug("ending sync_from_s3 %s", str(folder))

        return is_backup_present

    async def download_file(self, s3, bucket: str, key: str, filename: str, bytes_per_chunk=1 * 1024 * 1024) -> None:
        """
        Download file from S3 via multipart retrieval

        :param s3:
        :param bucket:
        :param key:
        :param filename:
        :param bytes_per_chunk:
        :return:
        """
        result = await s3.get_object(Bucket=bucket, Key=key)
        stream_reader = result["Body"]
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        try:
            with io.open(filename, "wb+") as fd:
                chunk = await stream_reader.read(bytes_per_chunk)
                while len(chunk) > 0:
                    fd.write(chunk)
                    chunk = await stream_reader.read(bytes_per_chunk)
        except:
            self.log.warn("download_file %s failed.", key)
            raise

    @staticmethod
    async def bucket_keys(s3, bucket: str, prefix: str) -> Set:
        """
        List all keys for the given bucket.

        :param s3:
        :param bucket: Bucket name.
        :param prefix: Prefix required on all Key names
        :return: A list of keys in the bucket.

        """
        try:
            contents = await s3.list_objects(Bucket=bucket, Prefix=prefix)
            contents = contents["Contents"]

            keys = set()
            for o in contents:
                key_path = o["Key"][len(prefix):]
                if len(key_path) > 0:
                    keys.add(key_path)
            return keys
        except KeyError:
            # No Contents Key, empty bucket.
            return set()

    @staticmethod
    def list_folder_files(source_folder: str) -> Set:
        """
        :param source_folder:  Root folder for resources you want to list.
        :return: A [str] containing relative names of the files.

        Example:

            /tmp
                - example
                    - file_1.txt
                    - some_folder
                        - file_2.txt

            >>> sync._list_folder_files("/tmp/example")
            ['file_1.txt', 'some_folder/file_2.txt']

        """

        path = Path(source_folder)

        paths = set()

        for file_path in path.rglob("*"):
            if file_path.is_dir():
                continue
            paths.add(str(file_path)[len(source_folder) + 1:])

        return paths


class FilePart(AsyncIterable):
    def __init__(self, file, offset, length, chunk=10 * 1024):
        self._file = file
        self._offset = self._orig_offset = offset
        self._length = self._orig_length = length
        self._chunk = chunk

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._length <= 0:
            raise StopAsyncIteration
        return self.read()

    def seek(self, offset, whence=os.SEEK_SET):
        if whence == os.SEEK_SET:
            self._offset = self._orig_offset + offset
            self._length = self._orig_length - offset
        elif whence == os.SEEK_CUR:
            self._offset += offset
            self._length -= offset
        elif whence == os.SEEK_END:
            self._offset = self._orig_offset + self._orig_length + offset - 1
            self._length = -offset

    def read(self):
        self._file.seek(self._offset)
        data = self._file.read(min(self._chunk, self._length))
        self._offset += self._chunk
        self._length -= self._chunk

        return data

    def md5(self):
        hash_md5 = hashlib.md5()

        self._file.seek(self._offset)
        len = self._length

        while len > 0:
            hash_md5.update(self._file.read(min([self._chunk, len])))
            len -= self._chunk

        return base64.b64encode(hash_md5.digest()).decode("utf-8")
