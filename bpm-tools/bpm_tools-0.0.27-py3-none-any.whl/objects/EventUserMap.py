
import json
import re


#Input and output from s3
from ..aws.s3 import write_json_events_array_to_s3
from ..aws.s3 import write_to_s3
from ..aws.s3 import get_file_data_from_s3


keys_to_exclude =  ['key', 'bucket','projectId', '_metadata','writeKey']

'''
--------------------------------------------------------------------------

Common HELPER Functions

--------------------------------------------------------------------------
'''
def build_map_filename(pipeline_client,
                       source_name,
                       event_name,
                       date_partition, datePartitionType = 'day', filename = None ):
    #map_filename = "{date}{client}/{source}/{event}/event-user.map".format(
    #                     client = pipeline_client
    #                    ,source = source_name
    #                    ,date = date_partition
    #                    ,event = event_name)  
    

    #Mapping file is file partitioned (e.g. mapping file corresponds to a single file)
    if datePartitionType in ['file']:
        map_filename = "{date}{client}/{source}/{event}/{filename}".format(
                             client = pipeline_client
                            ,source = source_name
                            ,date = date_partition
                            ,event = event_name
                            ,filename = filename)  
        
    #Mapping data is date and client partitioned (not source or event)
    elif datePartitionType in ['day-merged','month-merged']:
        map_filename = "{date}{client}/event-user.map".format(
                             client = pipeline_client
                            ,date = date_partition)  

    #Mapping file is date, client, source and event partitioned -
    else:
        map_filename = "{date}{client}/{source}-{event}-event-user.map".format(
                             client = pipeline_client
                            ,source = source_name
                            ,date = date_partition
                            ,event = event_name)  
    return map_filename




def get_path_partition(key, datePartitionType = 'day'):


    params = {}
    try:
        pathElements = key.rsplit('/')
        pipeline_client = pathElements[0]
        source_name = pathElements[1]
        event_name = pathElements[2]

        #Find the source/event/date partition of the file
        d_month_names = re.findall(r'/(year=\d{4})/(month=\d{1,2})/', key)
        d_day_names = re.findall(r'/(year=\d{4})/(month=\d{1,2})/(day=\d{1,2})/', key)
        day_partition = d_day_names[0][0] + '/' + d_day_names[0][1]+ '/' + d_day_names[0][2] + '/'
        month_partition = d_month_names[0][0] + '/' + d_month_names[0][1]+ '/'    

        filename = None
        
        if datePartitionType in ['day','day-merged']:
            date_partition = day_partition
            
        elif datePartitionType  in ['month','month-merged']:
            date_partition = month_partition
            
        elif datePartitionType == 'file':
            filename = key.rsplit('/', 1)[-1]
            date_partition = day_partition
        
        else:
            print('ERROR: datePartitionType variable not valid for object, returning...')
            return None

        map_filename = build_map_filename(pipeline_client,
                                          source_name,
                                          event_name,
                                          date_partition,
                                          datePartitionType = datePartitionType,
                                          filename = filename) 
        
        params['pipeline_client'] = pipeline_client
        params['source_name'] = source_name
        params['event_name'] = event_name
        params['date_partition'] = date_partition
        params['day_partition'] = day_partition
        params['month_partition'] = month_partition
        params['map_filename'] = map_filename



        return params
    
    except Exception as e:
        print("Invalid s3 key - must be of format...",e)
        return None


'''
--------------------------------------------------------------------------

class EventUserMap

--------------------------------------------------------------------------
'''



class EventUserMap:
    """
    A class to create, read and write an event-user map.
    
    Event-user maps are basically a hash table that maps
    a user (via user id) to the location of their events
    in the raw JSON data.
    
    This class only hold single distinct event type and
    date partition at a time. 
    
    Date partition is the year and month of the event
    data

    Attributes
    ----------
    files : dict
        the files that are contained in the event-map 
    users : dict
        the users that covered in the event-map 
    fileIndex : int
        the number of files contained in the event-map


    Methods
    -------
    add_file(bucket,key,userIdKey="userId")
        Adds a file to the event-map 

    add_event(event,i_line,fileIndex)
        Adds the mapping for the passed event for specified file 
        and line number

    create_map()
        Creates the event-user map for the files contained in
        self.files. All existing mappings in self.users will be deleted. 

    load_from_s3(bucket, key, append = True)
        Loads data from event-map file to the event-map.  By default
        this appends the new data to the existing
    
    write_to_s3(bucket, key)
        Writes the event-map data contained in self.files and self.users
        to s3, at the specified bucket/key
    
    get_user_events(event_userids)
        Fetches the event data for the specified list of user ids.
        The event-map must be loaded into the object for this to work.
        
    
        
    """
    def __init__(self, datePartitionType = 'day'):
        """
        Parameters
        ----------
        files : dict
            the files that are contained in the event-map 
        users : dict
            the users that covered in the event-map 
        fileIndex : int
            the number of files contained in the event-map
        """
        self.files = {}
        self.users = {}
        self.fileIndex = -1
        self.pipeline_client = None,
        self.source_name = None,
        self.event_name = None,
        self.date_partition = None,
        self.day_partition = None,
        self.month_partition = None,

        self.map_filename = None
        self.datePartitionType = datePartitionType

        
    def add_file(self,bucket,key,userIdKey="userId"):

        """Adds a file to the event-map 
        
        Also parses the path to extract:
            (1) pipeline_client (e.g. segment, cxense)
            (2) source_name (e.g. nettavis)
            (3) event_name (e.g. page, identify)
            (4) datePartitionTypePath - at the month level (assuming year=yyyy/month=mm)

        Parameters
        ----------
        bucket : str
            s3 bucket where file is located

        key : str
            s3 path of file

        userIdKey : str,optional
            The fieldname used to store the user id (defaults to userId)
            
        Raises
        ------
        
        Returns
        ------
        
        The fileIndex of the added file.   If file already exists
        it returns the fileIndex of the existing.

        """
        params = get_path_partition(key,datePartitionType=self.datePartitionType)        
        if self.map_filename is None and params is not None:

            self.pipeline_client = params['pipeline_client']
            self.source_name = params['source_name']
            self.event_name = params['event_name']
            self.date_partition = params['date_partition']
            self.day_partition = params['day_partition']
            self.month_partition = params['month_partition']
            self.map_filename = params['map_filename']
            
            #print("Creating a new map_filename for the object...")
            
        #Add file if the event type and partition are consistent
        if params['map_filename'] == self.map_filename:


            file = {
                "bucket": bucket,
                "key": key,
                "userIdKey": userIdKey

            }

            fileAlreadyAdded = False
            for k,v in self.files.items():
                if file == v:
                    #print("File already added to EventUserMap object, return index...")
                    return False, k

            self.fileIndex +=1
            self.files[self.fileIndex] = file
            return True, self.fileIndex
        
        #File event/partition not the same as existing
        else:
            print("Provided file is not consistent with the event/data parition of the existing files...")
            return False, None
            
            
            
        
    
    def add_event(self,event,i_line,fileIndex):

        """ Adds the mapping for the passed event for specified file 
        and line number
        

        Parameters
        ----------
        event : dict
            The event (JSON) to be added

        i_line : int
            The line number where the event is located

        fileIndex : int
            The fileIndex of the file that the event corresponds to
            
        Raises
        ------
        
        Returns
        ------
        
        True if successful, False if not

        """
        userid = None
        if fileIndex in self.files:
            userIdKey = self.files[fileIndex]["userIdKey"]
            if userIdKey in event:
                userid = event[userIdKey]

            #Add userid to the mapping dict
            if userid is not None and userid != '' and userid != 'None':
                if userid not in self.users:
                    self.users[userid] = {}
                if fileIndex not in self.users[userid]:
                    self.users[userid][fileIndex] = []

                #append the location of the event in the file
                self.users[userid][fileIndex].append(i_line)

        
        else:
            print("File not of index ",fileIndex, " not present in the EventUserMap obj" )
            return False

        
    def create_map(self):
        """ Creates the event-user map for the files contained in 
        self.files. All existing mappings in self.users will be deleted. 

        Parameters
        ----------
        None
        
        Raises
        ------
        
        Returns
        ------
        
        True if successful, False if not

        """
        self.users = {}
        for fileIndex, file in self.files.items():

            raw_data = get_file_data_from_s3(bucket=file["bucket"], key=file["key"])  
            i_line = 0
            for line in raw_data.splitlines():
                try:
                    event = json.loads(line)
                except Exception as e:
                    #Invalid line (throw error?)
                    pass
                else:
                    self.add_event(event,i_line,fileIndex)
                
                i_line+=1


        
        
    def write_to_s3(self, bucket, prefix):
        """ Writes the event-map data contained in self.files and self.users
        to s3, at the specified bucket/key
    
        Event-user map file formatted as such:
        
        userFileDataMap = {

                "pipeline_client": self.pipeline_client,
                "source_name": self.source_name,
                "event_name": self.event_name,
                "date_partition": self.date_partition,
                "map_filename": self.map_filename,
                "files": self.files, 
                "users": self.users 
        }

        Parameters
        ----------
        bucket : str
            s3 bucket where event-user map will be written

        prefix : str
            The path to the folder that contains the event-user maps
        
        
        Raises
        ------
        
        Returns
        ------
        
        True if successful, False if not

        """
        
        #Add a slash to the prefix if it is not present
        if prefix[-1:] != '/':
            prefix += '/'
        
        #If partitioned by day then merge with any existing mapping data
        if self.datePartitionType in ['day','day-merged','month','month-merged']:
            key = prefix + self.datePartitionType + '/' + self.map_filename
            self.load_from_s3(bucket, key)

        elif self.datePartitionType == 'file':
            #Create the file key (made of the event and partition details - e.g. prefix)
            key = prefix + 'file/' + self.map_filename

        else:
            print("Invalid data partition specified in object - please use datePartitionType = day or month")
            return False
        
        #Data available to write
        if self.map_filename is not None and self.users != {}:
            userFileDataMap = {
                
                    "pipeline_client": self.pipeline_client,
                    "source_name": self.source_name,
                    "event_name": self.event_name,
                    "date_partition": self.date_partition,
                    "month_partition": self.month_partition,
                    "day_partition": self.day_partition,
                    "map_filename": self.map_filename,
                    "datePartitionType": self.datePartitionType,
                    "files": self.files, 
                    "users": self.users 
            }
        
            try:

                print('Writing user-file lookup to s3...')
                

                
                write_json_events_array_to_s3(jsonEventsArray=[userFileDataMap]
                        ,Bucket = bucket
                        ,Key=key
                        ,Metadata = {'FileType': 'User-File Event Map for Privacy Broker'}
                        ,output_type = "json_gzip")
                
                print(key)
                return True

            except Exception as e:
                print("ERROR: Failed to save the event-user map files to s3...", e)
                return False
        else:
            print("No event-maping data to write.  Have you called create_map()?")
            
    
    def load_from_s3(self, bucket, key):
        """ Loads data from event-map file to the event-map.  By default
        this appends the new data to the existing
        
        Event-user map must be formatted as such:
        

        Parameters
        ----------
        bucket : str
            s3 bucket where event-user map is located

        key : str
            s3 path of file where event-user map is located
        
        Raises
        ------
        
        Returns
        ------
        
        True if successful, False if not

        """ 
    
                
        try:
            raw_data = get_file_data_from_s3(bucket=bucket, key=key)         
            lookupDict = json.loads(raw_data)
            self.load_from_map_dict(lookupDict)
            #print("Existing mapping file - appending...")

            return True

        except Exception as e:
            print("No existing mapping file - creating new...")
            return False

    def load_from_map_dict(self, lookupDict):
        """ Adds the mapping data from a from the event user map dictionary as
        read from from s3
        
        Files that are already in the object will not be replace within the
        data from s3.  This means that we always consider the data present in the
        object to be the newest/correct

        Parameters
        ----------
        lookupDict : event-user map dictionary read from the s3 file

        Raises
        ------
        
        Returns
        ------
        
        True if successful, False if not

        """ 
        #Iterate throught the New files in the mapping file and append and re-index
        fileIndexMap = {}
        files = lookupDict["files"]
        
        for fileIndexOld, file in files.items():                
            result, fileIndexNew = self.add_file(file["bucket"],file["key"],userIdKey =file["userIdKey"])

            #IF file was added (e.g. same file is not present in the file)
            if result == True:
                fileIndexMap[fileIndexOld] = fileIndexNew

        for userid, locationDict in lookupDict["users"].items():

            if userid not in self.users:
                self.users[userid] = {}

            for fileIndexOld, event_locations in locationDict.items(): 

                #If file valid for adding then  add user event maps locations
                if fileIndexOld in fileIndexMap:
                    self.users[userid][fileIndexMap[fileIndexOld]] = event_locations


        
    def get_user_events(self, event_userids):
        
        """  Fetches the event data for the specified list of user ids.
        The event-map must be loaded into the object for this to work.
    

        
        Parameters
        ----------
        event_userids : list (str)
            A list of user ids to extract event data for
        
        
        Raises
        ------
        
        Returns
        ------
        
        The event data for the specified user ids

        """
        user_data = {}
        n_files_with_user_data = 0
        for userid in event_userids:

            try:
                for fileIndex, eventLocations in self.users[userid].items():
                    bucket = self.files[fileIndex]['bucket']
                    key = self.files[fileIndex]['key']

                    #Data for the user is in the file
                    if eventLocations != []:
                        n_files_with_user_data += 1
                        
                        #Get the event meta data
                        params = get_path_partition(key)
                        pipeline_client = params["pipeline_client"]
                        source_name = params["source_name"]
                        event_name = params["event_name"]
                        
                        eventKey = "{pipeline_client}/{source_name}/{event_name}".format(
                                            pipeline_client=pipeline_client, 
                                            source_name=source_name, 
                                            event_name=event_name
                        )
                        if eventKey not in user_data:
                            user_data[eventKey] = []
                            
                        #Get the events from the requested file
                        eventdata_lines= get_file_data_from_s3(bucket=bucket, key=key).splitlines() 
                        for i in eventLocations:
                            #user_data.append(json.loads(eventdata_lines[i]))
                            data =  json.loads(eventdata_lines[i])

                            #Delete unecessary keys (and those potentially sensitive to PM)
                            for k in keys_to_exclude:
                                try:
                                    del data[k]
                                except KeyError:
                                    pass

                            #Append  data
                            user_data[eventKey].append(data)

            except Exception as e:
                pass
        
        return user_data






'''
--------------------------------------------------------------------------

class EventUserMapList

--------------------------------------------------------------------------
'''

class EventUserMapList:
    """
    A class to create, read and write an event-user map.
    
    Event-user maps are basically a hash table that maps
    a user (via user id) to the location of their events
    in the raw JSON data.
    
    This class only hold single distinct event type and
    date partition at a time. 
    
    Date partition is the year and month of the event
    data

    Attributes
    ----------
    files : dict
        the files that are contained in the event-map 
    users : dict
        the users that covered in the event-map 
    fileIndex : int
        the number of files contained in the event-map


    Methods
    -------
    add_file(bucket,key,userIdKey="userId")
        Adds a file to the event-map 

    add_event(event,i_line,fileIndex)
        Adds the mapping for the passed event for specified file 
        and line number

    create_map()
        Creates the event-user map for the files contained in
        self.files. All existing mappings in self.users will be deleted. 

    load_from_s3(bucket, key, append = True)
        Loads data from event-map file to the event-map.  By default
        this appends the new data to the existing
    
    write_to_s3(bucket, key)
        Writes the event-map data contained in self.files and self.users
        to s3, at the specified bucket/key
    
    get_user_events(event_userids)
        Fetches the event data for the specified list of user ids.
        The event-map must be loaded into the object for this to work.
        
    
        
    """
    def __init__(self, datePartitionType = 'day'):
        """
        Parameters
        ----------
        files : dict
            the files that are contained in the event-map 
        users : dict
            the users that covered in the event-map 
        fileIndex : int
            the number of files contained in the event-map
        """
        self.objDict = {}
        self.datePartitionType = datePartitionType


    def add_file(self,bucket,key,userIdKey="userId"):

        """Adds a file to the event-map 
        
        Also parses the path to extract:
            (1) pipeline_client (e.g. segment, cxense)
            (2) source_name (e.g. nettavis)
            (3) event_name (e.g. page, identify)
            (4) datePartitionTypePath - at the month level (assuming year=yyyy/month=mm)

        Parameters
        ----------
        bucket : str
            s3 bucket where file is located

        key : str
            s3 path of file

        userIdKey : str,optional
            The fieldname used to store the user id (defaults to userId)
            
        Raises
        ------
        
        Returns
        ------
        
        The fileIndex of the added file.   If file already exists
        it returns the fileIndex of the existing.

        """
        params = get_path_partition(key,datePartitionType=self.datePartitionType)
        map_filename = params['map_filename']
        
        
        #If the map_filename is present in list then add file to existing
        if map_filename in self.objDict:
            self.objDict[map_filename].add_file(bucket,key,userIdKey)
        #otherwise create a new EventUserMap object in the list and add the file
        else:
            self.objDict[map_filename] = EventUserMap(datePartitionType = self.datePartitionType)
            self.objDict[map_filename].add_file(bucket,key,userIdKey)
        
        return True
            
        
    def create_map(self):
        """ Creates the event-user map for the files contained in 
        self.files. All existing mappings in self.users will be deleted. 

        Parameters
        ----------
        None
        
        Raises
        ------
        
        Returns
        ------
        
        True if successful, False if not

        """
        
        for key, eventUserMap in self.objDict.items():
            eventUserMap.create_map()


        
        
    def write_to_s3(self, bucket, prefix):
        """ Writes the event-map data contained in self.files and self.users
        to s3, at the specified bucket/key

        Parameters
        ----------
        bucket : str
            s3 bucket where event-user map will be written

        prefix : str
            The path to the folder that contains the event-user maps
        
        
        Raises
        ------
        
        Returns
        ------
        
        True if successful, False if not

        """
        for key, eventUserMap in self.objDict.items():
            eventUserMap.write_to_s3(bucket, prefix)


    
    def load_from_s3(self, bucket, key):
        """ Loads data from event-map file to the event-map.  By default
        this appends the new data to the existing
        
        Event-user map must be formatted as such:
        

        Parameters
        ----------
        bucket : str
            s3 bucket where event-user map is located

        key : str
            s3 path of file where event-user map is located
        
        Raises
        ------
        
        Returns
        ------
        
        True if successful, False if not

        """ 
    
                
        try:
            raw_data = get_file_data_from_s3(bucket=bucket, key=key)         
            lookupDict = json.loads(raw_data)
            datePartitionType = lookupDict['datePartitionType']
            if datePartitionType in ['month','month-merged'] and self.datePartitionType in ['day','day-merged']:
                print("Note possible to load a month partitioned map into a day partitioned object. Returning...")
                return False
            
            #Incoming data is day or file partitioned and object is month (need to convert)
            elif datePartitionType in ['day','file'] and self.datePartitionType in ['day-merged', 'month','month-merged']:
                lookupDict['map_filename'] = build_map_filename(
                        pipeline_client = lookupDict['pipeline_client'],
                        source_name = lookupDict['source_name'],
                        event_name = lookupDict['event_name'],
                        date_partition = lookupDict['month_partition'],
                        datePartitionType = self.datePartitionType)
                
            #Incoming data is file partitioned and object is day (need to convert)
            elif datePartitionType in ['file'] and self.datePartitionType in ['day', 'day-merged']:
                lookupDict['map_filename'] = build_map_filename(
                        pipeline_client = lookupDict['pipeline_client'],
                        source_name = lookupDict['source_name'],
                        event_name = lookupDict['event_name'],
                        date_partition = lookupDict['day_partition'],
                        datePartitionType = self.datePartitionType)
            
            #Both the object and the incoming data have the same partition (continue)
            elif datePartitionType == self.datePartitionType:
                pass
            
            else:
                print("Incoming data not partitioned correctly")
                return False
    
            map_filename = lookupDict['map_filename']
            

            #If the map_filename is present in list then add file to existing
            if map_filename in self.objDict:
                self.objDict[map_filename].load_from_map_dict(lookupDict)
            #otherwise create a new EventUserMap object in the list and add the file
            else:
                self.objDict[map_filename] = EventUserMap(datePartitionType = self.datePartitionType)
                self.objDict[map_filename].load_from_map_dict(lookupDict)

            return True

        except Exception as e:
            print("ERROR: failed to open the mapping file...",e)
            return False
    

        
    def get_user_events(self, event_userids):
        
        """  Fetches the event data for the specified list of user ids.
        The event-map must be loaded into the object for this to work.
    

        
        Parameters
        ----------
        event_userids : list (str)
            A list of user ids to extract event data for
        
        
        Raises
        ------
        
        Returns
        ------
        
        The event data for the specified user ids

        """
        user_data = {}
        
        for key, eventUserMap in self.objDict.items():
            for eventKey, eventsList in eventUserMap.get_user_events(event_userids).items():
                if eventKey not in user_data:
                    user_data[eventKey] = []
                user_data[eventKey] += eventsList
                
        return user_data
        