import boto3
import json
from gzip import GzipFile
import io
from io import BytesIO
import decimal

# This is a workaround for: http://bugs.python.org/issue16535
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return int(obj)
        return super(DecimalEncoder, self).default(obj)



"""
----------------------------------------------------------------------------------------
get_file_data_from_s3


Function can handle the following text encodings:
    -utf-8
    -cp1252
    -latin-1


----------------------------------------------------------------------------------------
"""




def get_file_data_from_s3(bucket, key,s3 = boto3.client("s3")):

    #s3 = boto3.client("s3")
    raw_data = None

    #Read data from filename
    retr = s3.get_object(Bucket=bucket, Key=key)
    body = BytesIO(retr['Body'].read())

    #Decompress file if necessary
    try:
        raw_data=GzipFile(None, 'rb', fileobj=body).read()
        #print("Decompressing GZIP file...")

    except Exception as e:
        #print("Input file not compressed...")
        raw_data = body.getvalue()

    #Decode text - try utf-8 and if this fails try cp1252 (windows)
    try:
        raw_data = raw_data.decode("utf-8")
    except:
        try:
            raw_data = raw_data.decode("cp1252")
        except:
            raw_data = raw_data.decode("latin-1")
        
    return raw_data




"""
----------------------------------------------------------------------------------------
Write data to s3








----------------------------------------------------------------------------------------
"""
def write_to_s3(Bucket, Key, ioBuffer, Metadata = {'Meta0': 'Meta data not specifified'}, output_type ='json_gzip' ):
    s3 = boto3.client("s3")
    try:

        if output_type == 'json_gzip':
            s3.put_object(
            Bucket=Bucket,
            Key=Key,       #Remove the gzip prefix b/c the output is not GZIP ecoded 
            ContentType='binary/octet-stream',      # the original type
            ContentEncoding='gzip',                # MUST have or browsers will error
            Metadata=Metadata,
            Body=ioBuffer.getvalue()
            )


        elif output_type == 'json':
            s3.put_object(
              Bucket=Bucket,
              Key=Key,       #Remove the gzip prefix b/c the output is not GZIP ecoded 
              ContentType='binary/octet-stream',      # the original type
              ContentEncoding='standard',                # MUST have or browsers will error
              Metadata=Metadata,
              Body=ioBuffer.getvalue()
            )

        ioBuffer.close()
        return True

    except Exception as e:
        print("Write to s3 failed!")
        print(e)
        return False

    return False


"""
----------------------------------------------------------------------------------------
Write JSON events to s3








----------------------------------------------------------------------------------------
"""



def write_json_events_array_to_s3(jsonEventsArray,Bucket, Key, Metadata = {'Meta0': 'Meta data not specified'}, output_type ='json_gzip', cls=None):

    try:

        #Create the BytesIO object
        io_buffer = io.BytesIO()
        if output_type == 'json_gzip':
            io_buffer_gzip = GzipFile(None, 'wb', 9, io_buffer)

        for data in jsonEventsArray:

            #No custom encoding
            if cls is None:
                if output_type == 'json_gzip':
                    io_buffer_gzip.write("{}\n".format(json.dumps(data)).encode('utf-8'))

                elif output_type == 'json':
                    io_buffer.write("{}\n".format(json.dumps(data)).encode('utf-8'))

            #Custom encoding required - e.g. to convert from decimal to floating point
            else:
                if output_type == 'json_gzip':
                    io_buffer_gzip.write("{}\n".format(json.dumps(data,cls=DecimalEncoder)).encode('utf-8'))

                elif output_type == 'json':
                    io_buffer.write("{}\n".format(json.dumps(data,cls=DecimalEncoder)).encode('utf-8'))

        if output_type == 'json_gzip':
              io_buffer_gzip.close()

        response = write_to_s3(Bucket = Bucket, Key = Key, ioBuffer = io_buffer, Metadata = Metadata, output_type =output_type)
        return response

    except Exception as e:
        print("Write to s3 failed!")
        print(e)
        return False
    
    return False





"""
----------------------------------------------------------------------------------------
get_matching_s3_objects
                
----------------------------------------------------------------------------------------

"""

def get_matching_s3_objects(bucket, prefix="",  suffix="",suffix_list = [],s3 =boto3.client("s3")):
    """
    Generate objects in an S3 bucket.

    :param bucket: Name of the S3 bucket.
    :param prefix: Only fetch objects whose key starts with
        this prefix (optional).
    :param suffix: Only fetch objects whose keys end with
        this suffix (optional).
    """
    #s3 = boto3.client("s3")
    paginator = s3.get_paginator("list_objects_v2")

    kwargs = {'Bucket': bucket}

    # We can pass the prefix directly to the S3 API.  If the user has passed
    # a tuple or list of prefixes, we go through them one by one.
    if isinstance(prefix, str):
        prefixes = (prefix, )
    else:
        prefixes = prefix

    for key_prefix in prefixes:
        kwargs["Prefix"] = key_prefix

        for page in paginator.paginate(**kwargs):
            try:
                contents = page["Contents"]
                
            except KeyError:
                return

            for obj in contents:
                key = obj["Key"]
                #if key.endswith(suffix):
                if suffix_list != []:
                    if any(suf in key for suf in suffix_list):
                         yield obj
                
                
                elif suffix in key:
                    yield obj



"""
----------------------------------------------------------------------------------------
get_matching_s3_keys
----------------------------------------------------------------------------------------
"""
def get_matching_s3_keys(bucket, prefix="", suffix="", suffix_list = []):

    for obj in get_matching_s3_objects(bucket, prefix, suffix,suffix_list):
        yield obj["Key"],obj["Size"]


"""
----------------------------------------------------------------------------------------
get_matching_s3_keys_v2 - returns date_modified
----------------------------------------------------------------------------------------
"""
def get_matching_s3_keys_v2(bucket, prefix="", suffix="", suffix_list = [],s3 =boto3.client("s3")):

    for obj in get_matching_s3_objects(bucket, prefix, suffix,suffix_list,s3):
        yield obj["Key"],obj["Size"], obj['LastModified']



        