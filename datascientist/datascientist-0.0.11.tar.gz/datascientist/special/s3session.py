"""
@doc: a helper for accessing AWS resources using credentials.
@note: priority is environment variables -> .aws/credentials -> ~/spec_creds.json -> manually entered
"""
import boto3
import os
import json
import io
from pathlib import Path

hm = str(Path.home())

access = os.environ.get("AWS_S3_SPECIAL_KEY")
secret = os.environ.get("AWS_S3_SPECIAL_SECRET")

def get_resource():
    """
    @doc: create a boto3 session
    @args: None
    @return: a boto3 session object
    """
    sess = boto3.Session(aws_access_key_id = access, aws_secret_access_key = secret)
    ret = sess.resource('s3')
    return ret

def read_creds():
    """
    @doc: look for locally stored AWS credentials
    @args: None
    @return: a tuple of str with access key and secret
    @note: if none are found then return None
    """
    ret = None
    if os.path.isfile("{}/.aws/credentials".format(hm)):
        access = None
        secret = None
        with open("{}/.aws/credentials".format(hm)) as file:
            lines = file.readlines()
        for line in lines:
            if line[:10] == 'aws_access':
                access = line[line.find("=") + 2:-1]
            elif line[:10] == 'aws_secret':
                secret = line[line.find("=") + 2:-1]
        ret = access, secret
    return ret

if access is None:
    no_creds = True
    creds = read_creds()
    if creds is not None:
        if creds[0] is not None and creds[1] is not None:
            no_creds = False
            access = creds[0]
            secret = creds[1]
    if no_creds:
        try:
            creds = json.load(open(hm + "/spec_creds.json", "r"))
            access = creds["AWS_S3_SPECIAL_KEY"]
            secret = creds["AWS_S3_SPECIAL_SECRET"]
        except:
            print("No access or secret found.  The values set here will not be stored.")
            access = input("Please enter your AWS access key: ")
            secret = input("Please enter your AWS secret key: ")
    
