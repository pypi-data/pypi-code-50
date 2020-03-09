from datetime import datetime
import hashlib
import json
import os

class DataObject:

    def __init__(self, 
                    directory = None, 
                    digest = None,
                    parent_directory = None
                ):
        
        self.data = {}
        self.keys = None
        self.hash_digest = None
        self.directory_name = None
        self.parent_directory = None

        #   If a hash given then we need to assume
        #   this is a block that has already been written
        #   before.
        
        if digest:
            self.hash_digest = digest

        #   Override the directory name
        #   By default it will be dump_hash()
        if directory:
            self.directory_name = directory

        #   Let them pass a parent directory
        #   for us to build ours on top of
        #   (will come in handy when building a chain)
        
        if parent_directory:
            self.parent_directory = parent_directory

    def __getitem__(self, key):
        return str(key)

    def __str__(self):
        return "DataObject"

    def refresh(self, details = {}):
        for key in self.keys.denormalized:
            value = None
            if key in details:
                value = details[key]
            
            self.__dict__[key] = value

        return self

    def build_keys(self, denormalized = [], objects = []):
        self.keys = Keys(denormalized=denormalized, objects=objects)

    def digest(self, accuracy = 5):
        if 'hash_digest_buffer' in self.__dict__ and self.hash_digest_buffer:
            return self.hash_digest_buffer

        hash_object = hashlib.new("whirlpool")
        hash_object.update(self.dump_all(serialized = True).encode('utf-8'))

        hash_buffer = hash_object.hexdigest()
        
        if accuracy:
            hash_buffer = hash_buffer[0:accuracy]

        return hash_buffer

    def directory(self):
        dirname_buf = ""
        if self.parent_directory:
            dirname_buf = self.parent_directory
        
        if self.directory_name:
            dirname_buf += self.directory_name
        else:
            if len(dirname_buf) > 0:
                dirname_buf += "/"
            
            if self.hash_digest:
                dirname_buf += self.hash_digest
            else:
                dirname_buf += self.digest()
        
        return dirname_buf

    def dump_all(self, serialized = False):
        output_buffer = {
            "details": self.dump_details(serialized=serialized),
            "data": self.dump_data(serialized=serialized)
        }

        if serialized:
            output_buffer = json.dumps(output_buffer)

        return output_buffer

    def dump_data(self, serialized = False):
        output_buffer = self.data

        if serialized:
            output_buffer = json.dumps(output_buffer)

        return output_buffer

    def dump_details(self, serialized = False):
        local_data_buffer = self.__dict__
        output_buffer = {}

        for key in self.keys.denormalized:
            if key in local_data_buffer:
                output_buffer[key] = local_data_buffer[key]

        if serialized:
            output_buffer = json.dumps(output_buffer)

        return output_buffer

    def denormalized_keys(self):
        return []

    def from_dict(self, object_dict = {}):
        self.refresh(details=object_dict['details'])
        self.data = object_dict['data']
        
        return self
        
    def read(self):
        details_filename = self.directory() + "/details"
        data_filename = self.directory() + "/data"  
        data_buffer = None
        with open(data_filename, 'r') as fp:
            data_buffer = json.loads(fp.read())
            fp.close()

        details_buffer = None
        with open(details_filename, 'r') as fp:
            details_buffer = json.loads(fp.read())
            fp.close()

        self.hash_digest_buffer = None
        return self.from_dict({
            'data': data_buffer,
            'details': details_buffer
        })

    def write(self):
        details_filename = self.directory() + "/details"
        data_filename = self.directory() + "/data"        
        
        if not os.path.exists(self.directory()):
            os.mkdir(self.directory())
        
        data = self.dump_data(serialized = True)
        with open(data_filename, 'w') as fp:
            fp.write(data)
            fp.close()

        details = self.dump_details(serialized = True)
        with open(details_filename, 'w') as fp:
            fp.write(details)
            fp.close()

class Keys:
    
    def __init__(self, denormalized = [], objects = []):
        self.denormalized = None
        if len(denormalized) > 0:
            self.denormalized = denormalized
        
        self.objects = None
        if len(objects) > 0:
            self.objects = objects

    def __str__(self):
        return str({
            "denormalized": self.denormalized,
            "objects": self.objects
        })