# -*- coding: utf-8 -*-

import boto3
import botocore.exceptions


class s3_server:
    def __init__(self, bucket, region):
        self.bucket = bucket
        self.region = region
        self.client = boto3.client("s3", region_name=region)

    def gen_folders(self, prefix=""):
        paginator = self.client.get_paginator("list_objects_v2")
        for result in paginator.paginate(
            Bucket=self.bucket, Prefix=prefix, Delimiter="/"
        ):
            for key_prefix in result.get("CommonPrefixes", []):
                if prefix in key_prefix.get("Prefix"):
                    yield key_prefix.get("Prefix")

    def gen_files(self, prefix=""):
        paginator = self.client.get_paginator("list_objects_v2")

        for page in paginator.paginate(
            Bucket=self.bucket, Prefix=prefix, Delimiter="/"
        ):
            try:
                contents = page["Contents"]
            except KeyError:
                return

            for obj in contents:
                if obj["Size"] == 0:
                    continue
                yield obj

    def key_exists(self, key):
        """ Try to fetch the metadata for an object. If the object does not
            exist, head_object will raise an exception. Returns True if the
            object exists
        """
        try:
            head = self.client.head_object(Bucket=self.bucket, Key=key)
            if head.get("ContentLength") == 0:
                # Disregard empty objects
                return False
        except (
            botocore.exceptions.ParamValidationError,
            botocore.exceptions.ClientError,
        ):
            return False
        return True

    def create_signed_url(self, key):
        return self.client.generate_presigned_url(
            "get_object", Params={"Bucket": self.bucket, "Key": key}, ExpiresIn=90
        )
