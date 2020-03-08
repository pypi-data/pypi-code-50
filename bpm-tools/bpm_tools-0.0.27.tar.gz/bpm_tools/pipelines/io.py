
'''
try:
    import unzip_requirements
except ImportError:
    pass

'''

import json
import boto3
from gzip import GzipFile
import io
from io import BytesIO
import os

#For parse s3 event function
from urllib.parse import unquote
import re
from datetime import datetime






#Import functions from package
from ..objects.EventUserMap import EventUserMap
from ..aws.s3 import get_file_data_from_s3



def read_lines(bucket, key, objEventUserMap = None, userIdKey = "userId"):
    
    try:

        if isinstance(objEventUserMap,EventUserMap):
            result, fileIndex = objEventUserMap.add_file(bucket,key,userIdKey = userIdKey)

        elif objEventUserMap is not None:
            print("ERROR reading file: objEventUserMap not of type EventUserMap...")
            return False



        raw_data = get_file_data_from_s3(bucket=bucket, key=key) 

        i_line = 0
        for line in raw_data.splitlines():
            try:
                event = json.loads(line)
            except Exception as e:
                #Invalid line (throw error?)
                pass
            else:
                
                #-------------------------------------------------------------------------
                #STEP 1: Iterate line-by-line and get the location of events for each user
                #-------------------------------------------------------------------------

                if objEventUserMap:
                    objEventUserMap.add_event(event,i_line,fileIndex)
                #-------------------------------------------------------------------------
                #STEP 2: Yield command to expose the event data to the calling function
                #-------------------------------------------------------------------------
                yield event
                
            i_line += 1
    except Exception as e:
        print('Unable to open the file...')
        print(e)

        return False

# ------------- get_partition_path_from_event ------------------
#
#    Function determines the partition path from the event timestamp
#    and returns a path in the format of:
#       year=yyyy/month=mm/day=dd/

#    Otherwise returns None
# ---------------------------------------------------------

def get_partition_path_from_event(event_timestamp, event_name, input_file_name, pipeline_client, source_name = ''):
    try:

        #Partition the data by year,month,day,hour (if not already done)
        year = '{:04d}'.format(event_timestamp.year)
        month = '{:02d}'.format(event_timestamp.month)
        day = '{:02d}'.format(event_timestamp.day)
        hour = '{:02d}'.format(event_timestamp.hour)
        
        #Partition to the DAY
        
        if source_name != '':
            partition = "year={year}/month={month}/day={day}/".format(year=year, month=month, day=day)
            target_key = pipeline_client + '/'  + source_name + '/' + event_name + '/' + partition + input_file_name
        else:
            partition = "year={year}/month={month}/day={day}/".format(year=year, month=month, day=day)
            target_key = pipeline_client + '/' + event_name + '/' + partition + input_file_name
           
        
        return target_key

    except Exception as e:
        print(e)
        raise

  


# ------------- parse_s3_key ------------------
#
#    Parses the s3 key and gets to extract (where present):
#       -the filename
#       -Any date partitions that are present in the path
#           (year=yyyy/month=mm/day=dd/, YYYY/MM/DD, YYYY/MM, etc.)
#       -The event name
#       -The source name
#       -The pipeline client
#       -The filename (without the file extension)

# ---------------------------------------------------------

def parse_s3_key(key, bucket = '', pipeline_client = 'Unknown'):
    

    #Return values
    pipeline_client = ''
    pipeline_client_default = 'Unknown'
    source_name = ''
    event_name = ''
    datePartitionPath = ''
    pathDateTime = None    
    year = None
    #Returned dictionary of parsed values
    parsedKeyDict = {}
    
    #remove the file extention from path and make lowercase
    s3_prefix = os.path.splitext(key)[0].lower()
    
    filename = s3_prefix.rsplit('/', 1)[-1]
    
    #Remove filename from prefix
    s3_prefix = s3_prefix.replace(filename,'')
    
    
    d_hour = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/(\d{1,2})/', s3_prefix)
    d_day = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', s3_prefix)
    d_month = re.findall(r'/(\d{4})/(\d{1,2})/', s3_prefix)
    d_year = re.findall(r'/(\d{4})/', s3_prefix)
    
    d_hour_names = re.findall(r'/(year=\d{4})/(month=\d{1,2})/(day=\d{1,2})/(hour=\d{1,2})/', s3_prefix)
    d_day_names = re.findall(r'/(year=\d{4})/(month=\d{1,2})/(day=\d{1,2})/', s3_prefix)
    d_month_names = re.findall(r'/(year=\d{4})/(month=\d{1,2})/', s3_prefix)
    d_year_names = re.findall(r'/(year=\d{4})/', s3_prefix)
    
    #Return the path
    if d_hour != []:
        datePartitionPath = d_hour[0][0] + '/' + d_hour[0][1]+ '/' + d_hour[0][2] + '/' + d_hour[0][3] + '/'
        pathDateTime = datetime(int(d_hour[0][0]),int(d_hour[0][1]),int(d_hour[0][2]),int(d_hour[0][3]))
        year = d_hour[0][0]

    elif d_day != []:
        datePartitionPath = d_hour[0][0] + '/' + d_hour[0][1]+ '/' + d_hour[0][2] + '/' 
        pathDateTime = datetime(int(d_hour[0][0]),int(d_hour[0][1]),int(d_hour[0][2]))
        year = d_day[0][0]
        
    elif d_month != []:
        datePartitionPath = d_month[0][0] + '/' + d_month[0][1]+ '/' 
        year = d_month[0][0]
        
    elif d_year != []:
        datePartitionPath = d_year[0] + '/'
        year = d_year[0]
       
    
    elif d_hour_names != []:
        datePartitionPath = d_hour_names[0][0] + '/' + d_hour_names[0][1]+ '/' + d_hour_names[0][2] + '/' + d_hour_names[0][3] + '/'
        pathDateTime = datetime(int(d_hour_names[0][0].replace('year=','')), \
                             int(d_hour_names[0][1].replace('month=','')), \
                             int(d_hour_names[0][2].replace('day=','')), \
                             int(d_hour_names[0][3].replace('hour=','')))
        year = d_hour_names[0][0]


    elif d_day_names != []:
        datePartitionPath = d_day_names[0][0] + '/' + d_day_names[0][1]+ '/' + d_day_names[0][2] + '/'
        pathDateTime = datetime(int(d_day_names[0][0].replace('year=','')), \
                             int(d_day_names[0][1].replace('month=','')), \
                             int(d_day_names[0][2].replace('day=','')))
        year = d_day_names[0][0]


    elif d_month_names != []:
        datePartitionPath = d_month_names[0][0] + '/' + d_month_names[0][1]+ '/'
        year = d_month_names[0][0]

    elif d_year_names != []:
        datePartitionPath = d_year_names[0] + '/' 
        year = d_year_names[0] 

        
    #Remove the date partition from the prefix
    if datePartitionPath is not None:
        s3_prefix = s3_prefix.replace('/' + datePartitionPath,'')
        
    #Get the Pipeline client, source and event name from the path
    remainingPathElements = s3_prefix.rsplit('/')
    
    #Pipeline client, source and Event Name in path
    if len(remainingPathElements) == 3:
        pipeline_client = remainingPathElements[0]
        source_name = remainingPathElements[1]
        event_name = remainingPathElements[2]

    #Pipeline client and Event Name in path
    elif len(remainingPathElements) == 2:
        pipeline_client = remainingPathElements[0]
        event_name = remainingPathElements[1]

    #If there is only one path element assume that this is the event
    elif len(remainingPathElements) == 1:
        
        #Set the pipeline client to unknown
        pipeline_client = pipeline_client_default
        source_name = remainingPathElements[0]
        
        
    parsedKeyDict['bucket'] = bucket
    parsedKeyDict['key'] = key
    parsedKeyDict['pipeline_client'] = pipeline_client
    parsedKeyDict['source_name'] = source_name
    parsedKeyDict['event_name'] = event_name
    parsedKeyDict['filename'] = filename
    parsedKeyDict['path_date_partition'] = datePartitionPath
    parsedKeyDict['path_datetime'] = pathDateTime
    parsedKeyDict['year'] = year

    return parsedKeyDict


# ------------- parse_s3_event ------------------
#
#    Parses the s3 key and gets to extract (where present):
#       -the filename
#       -Any date partitions that are present in the path
#           (year=yyyy/month=mm/day=dd/, YYYY/MM/DD, YYYY/MM, etc.)
#       -The event name
#       -The source name
#       -The pipeline client
#       -The filename (without the file extension)

# ---------------------------------------------------------

def parse_s3_event(event, pipeline_client = 'Unknown'):
    
    print(event)

    try:
        s3_event = event["Records"][0]["s3"]
        key = unquote(s3_event["object"]["key"])
        bucket = s3_event["bucket"]["name"]
    except:
        print("this is not an s3-event, checking if manually triggered")
        if "s3key" in event and "s3bucket" in event:
            key = event["s3key"]
            bucket = event["s3bucket"]
            print("manual-event")
        else:
            return None

    parsedKeyDict = parse_s3_key(key, bucket, pipeline_client = pipeline_client)
    return parsedKeyDict

    '''
    #Return values
    pipeline_client = ''
    pipeline_client_default = 'Unknown'
    source_name = ''
    event_name = ''
    datePartitionPath = ''
    pathDateTime = None    
    
    #Returned dictionary of parsed values
    parsedKeyDict = {}
    
    #remove the file extention from path and make lowercase
    s3_prefix = os.path.splitext(key)[0].lower()
    
    filename = s3_prefix.rsplit('/', 1)[-1]
    
    #Remove filename from prefix
    s3_prefix = s3_prefix.replace(filename,'')
    
    
    d_hour = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/(\d{1,2})/', s3_prefix)
    d_day = re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', s3_prefix)
    d_month = re.findall(r'/(\d{4})/(\d{1,2})/', s3_prefix)
    d_year = re.findall(r'/(\d{4})/', s3_prefix)
    
    d_hour_names = re.findall(r'/(year=\d{4})/(month=\d{1,2})/(day=\d{1,2})/(hour=\d{1,2})/', s3_prefix)
    d_day_names = re.findall(r'/(year=\d{4})/(month=\d{1,2})/(day=\d{1,2})/', s3_prefix)
    d_month_names = re.findall(r'/(year=\d{4})/(month=\d{1,2})/', s3_prefix)
    d_year_names = re.findall(r'/(year=\d{4})/', s3_prefix)
    
    #Return the path
    if d_hour != []:
        datePartitionPath = d_hour[0][0] + '/' + d_hour[0][1]+ '/' + d_hour[0][2] + '/' + d_hour[0][3] + '/'
        pathDateTime = datetime(int(d_hour[0][0]),int(d_hour[0][1]),int(d_hour[0][2]),int(d_hour[0][3]))


    elif d_day != []:
        datePartitionPath = d_hour[0][0] + '/' + d_hour[0][1]+ '/' + d_hour[0][2] + '/' 
        pathDateTime = datetime(int(d_hour[0][0]),int(d_hour[0][1]),int(d_hour[0][2]))

        
    elif d_month != []:
        datePartitionPath = d_month[0][0] + '/' + d_month[0][1]+ '/' 

        
    elif d_year != []:
        datePartitionPath = d_year[0] + '/'

       
    
    elif d_hour_names != []:
        datePartitionPath = d_hour_names[0][0] + '/' + d_hour_names[0][1]+ '/' + d_hour_names[0][2] + '/' + d_hour_names[0][3] + '/'
        pathDateTime = datetime(int(d_hour_names[0][0].replace('year=','')), \
                             int(d_hour_names[0][1].replace('month=','')), \
                             int(d_hour_names[0][2].replace('day=','')), \
                             int(d_hour_names[0][3].replace('hour=','')))

    elif d_day_names != []:
        datePartitionPath = d_day_names[0][0] + '/' + d_day_names[0][1]+ '/' + d_day_names[0][2] + '/'
        pathDateTime = datetime(int(d_day_names[0][0].replace('year=','')), \
                             int(d_day_names[0][1].replace('month=','')), \
                             int(d_day_names[0][2].replace('day=','')))


    elif d_month_names != []:
        datePartitionPath = d_month_names[0][0] + '/' + d_month_names[0][1]+ '/'

    elif d_year_names != []:
        datePartitionPath = d_year_names[0] + '/' 

        
    #Remove the date partition from the prefix
    if datePartitionPath is not None:
        s3_prefix = s3_prefix.replace('/' + datePartitionPath,'')
        
    #Get the Pipeline client, source and event name from the path
    remainingPathElements = s3_prefix.rsplit('/')
    
    #Pipeline client, source and Event Name in path
    if len(remainingPathElements) == 3:
        pipeline_client = remainingPathElements[0]
        source_name = remainingPathElements[1]
        event_name = remainingPathElements[2]

    #Pipeline client and Event Name in path
    elif len(remainingPathElements) == 2:
        pipeline_client = remainingPathElements[0]
        event_name = remainingPathElements[1]

    #If there is only one path element assume that this is the event
    elif len(remainingPathElements) == 1:
        
        #Set the pipeline client to unknown
        pipeline_client = pipeline_client_default
        source_name = remainingPathElements[0]
        
        
    parsedKeyDict['bucket'] = bucket
    parsedKeyDict['key'] = key
    parsedKeyDict['pipeline_client'] = pipeline_client
    parsedKeyDict['source_name'] = source_name
    parsedKeyDict['event_name'] = event_name
    parsedKeyDict['filename'] = filename
    parsedKeyDict['path_date_partition'] = datePartitionPath
    parsedKeyDict['path_datetime'] = pathDateTime
    
    return parsedKeyDict

    '''






