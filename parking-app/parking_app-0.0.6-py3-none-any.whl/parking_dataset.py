import os
import json
import shutil
import tempfile
import hashlib
import base64
from google.cloud import storage
from google.cloud.storage.blob import Blob



class ParkingDataset:

    def __init__(self, dir):
        self.add_allowed = True
        if not dir or not os.path.exists(dir):
            self.add_allowed = False
            return
            # raise Exception(f'Dir {dir} doesnt exists')
        self.src = os.path.join(dir, 'src')
        os.makedirs(self.src, exist_ok=True)


    def add_src_entry(self, job_id, regions_map, detections_map, img_src_file):
        if not self.add_allowed:
            return None, None
        jdir = os.path.join(self.src, self._version_base_dir(job_id, regions_map))
        dnamp_file = os.path.join(jdir, os.path.splitext(os.path.basename(img_src_file))[0] + '.json')
        im_file =  os.path.join(jdir, os.path.basename(img_src_file))
        with open(dnamp_file, mode='w') as fp:
            json.dump(detections_map, fp=fp, indent=4, sort_keys=True)
        shutil.copy2(img_src_file, im_file)
        return dnamp_file, im_file

    def _version_base_dir(self, job_id, regions_map):
        base_jid = self._single_version_check(job_id, regions_map)
        if base_jid:
            return base_jid
        for x in range(100000):
            base_jid = f'{job_id}-{x}'
            if self._single_version_check(base_jid, regions_map):
                return base_jid
        raise Exception('Not possible create or detect version of entry in {} for {}'.format(self.src, job_id))


    def _single_version_check(self, base_jid, regions_map):
        rmap_file = os.path.join(self.src, base_jid+'.json')
        if not os.path.exists(rmap_file):
            with open(rmap_file, mode='w') as fp:
                json.dump(regions_map, fp=fp, indent=4, sort_keys=True)
            os.makedirs(os.path.join(self.src, base_jid), exist_ok=True)
            return base_jid
        else:
            # compare
            regions_map_existing = None
            with open(rmap_file, mode='r') as fp:
                regions_map_existing = json.load(fp)
            if json.dumps(regions_map_existing, indent=4, sort_keys=True) == \
                    json.dumps(regions_map,indent=4, sort_keys=True):
                return base_jid
        return None

GCLOUD_BUCKET_NAME = 'datasets-ai'
GCLOUD_PARKING_PREFIX = 'parking/src/'

class ParkingDatasetGcloud:

    def __init__(self, service_account_file):
        self.service_account_file = service_account_file
        if self.service_account_file:
            self._initialize()

    def check_config(self, service_account_file):
        if not self.service_account_file or self.service_account_file != service_account_file:
            self.service_account_file = service_account_file
            self._initialize()
            return

    def _initialize(self):
        self.storage_client = storage.Client.from_service_account_json(self.service_account_file)
        self.bucket = self.storage_client.bucket(GCLOUD_BUCKET_NAME)

    def _list_dir(self, path):
        pth = '' if not path or path == '' or path == '/' else path + '/'
        return list(self.storage_client.list_blobs( bucket_or_name=self.bucket,
            prefix=GCLOUD_PARKING_PREFIX+pth, delimiter='/'
        ))

    def _exists(self, full_name):
        blob = self._blob(full_name)
        return blob.exists()

    def _md5(self, full_name):
        blob = self._blob(full_name)
        if blob.exists():
            blob.reload()
            return blob.md5_hash
        return None

    def _blob(self, full_name):
        return Blob(GCLOUD_PARKING_PREFIX+full_name, self.bucket)

    @staticmethod
    def _is_utf(string):
        try:
            string.decode('utf-8')
            return True
        except (UnicodeError,AttributeError):
            return False

    @staticmethod
    def _md5_from_str(string):
        _str = str if ParkingDatasetGcloud._is_utf(string) else string.encode('utf-8')
        return base64.b64encode(hashlib.md5(_str).digest()).decode("utf-8")



    def _version_base_dir(self, job_id, regions_map):
        base_jid = self._single_version_check(job_id, regions_map)
        if base_jid:
            return base_jid
        for x in range(100000):
            base_jid = f'{job_id}-{x}'
            if self._single_version_check(base_jid, regions_map):
                return base_jid
        raise Exception('Not possible create or detect version of entry for {}'.format(job_id))


    def _single_version_check(self, base_jid, regions_map):
        rmap_file = base_jid+'.json'
        if not self._exists(rmap_file):
            blob = self._blob(rmap_file)
            blob.upload_from_string(json.dumps(regions_map,indent=4, sort_keys=True))
            return base_jid
        else:
            # compare
            remote_hash = self._md5(rmap_file)
            local_hash =  ParkingDatasetGcloud._md5_from_str(json.dumps(regions_map,indent=4, sort_keys=True))
            if remote_hash == local_hash:
                return base_jid
        return None


    def add_src_entry(self, job_id, regions_map, detections_map, img_src_file):
        jdir = self._version_base_dir(job_id, regions_map)
        dnamp_file = '{}/{}'.format(jdir, os.path.splitext(os.path.basename(img_src_file))[0] + '.json')
        im_file =  '{}/{}'.format(jdir, os.path.basename(img_src_file))
        dnamp_blob = self._blob(dnamp_file)
        dnamp_blob.upload_from_string(json.dumps(detections_map,  indent=4, sort_keys=True))
        im_blob = self._blob(im_file)
        im_blob.upload_from_filename(img_src_file)
        return dnamp_blob.name, im_blob.name


#     def test(self):
#         print(self._list_dir(''))
#         print(self._list_dir('exported_data4'))
#         print(self._exists('boring_morse_937c77b0-b867.json'))
#         print(self._exists('boring_morse_937c77b0-b867.jsona'))
#         print(self._md5('boring_morse_937c77b0-b867.json'))
#         print(self._md5('boring_morse_937c77b0-b867.jsona'))
#         print(ParkingDatasetGcloud._md5_from_str('boring_morse_937c77b0-b867.jsona'))
#
# if __name__ == '__main__':
#     p = ParkingDatasetGcloud('D:\work\CloudStation\keys\parking-dataset-contrib1.json')
#     p.test()