import datablox.Block as blk
import datablox.Ledger as ldr

from datetime import datetime

import json
import os

class Chain:
    
    def __del__(self):
        pass
        #self.write()

    def __init__(self, directory = None):
        if directory:
            self.directory = directory
        else:
            print("No chain directory given")
            exit(-1)

        self.head_setup()

    def block_spawn(self, previous = None):
        
        parent_directory = self.directory + "/blocks"
        if not previous:
            if self.head:
                previous = self.head

        block = blk.Block(
            parent_directory = parent_directory,
            previous=previous
        )

        return block

    def block(self, **args):
        block = self.block_spawn()
        new = False

        
        if 'new' in args or 'init' in args:
            new = True

        if new:
            block.timestamp = str(datetime.now())
            if 'data' in args:
                block.data = args['data']

            if self.head:
                print("Ha!")

            self.head = block.digest()
            self.head_object = block
            print(self.head_object)

            block.write()
            self.write()
        else:
            print("Not new")

    def build_directories(self):
        if not os.path.exists(self.directory):
            os.mkdir(self.directory)
        
        if not os.path.exists(self.directory + "/blocks"):
            os.mkdir(self.directory + "/blocks")

    def build_objects(self):
        #   Build up the objects (e.g. head_object) needed to run common 
        #   algorithms
        print("Creating head object and pointer to it...", end=' ')
        self.head_object = self.block_spawn().from_hash(self.head)
        print("Done.")

        print("Head object:", self.head_object)
    
    def dump(self):
        buffer = self.head_object
        while buffer is not None:
            print(buffer)
            buffer = buffer.move()

    def head_setup(self):
        self.head = None

        if os.path.isfile(self.directory + "/details"):
            print("Details file found [%s/details], reading..." % self.directory, end=' ')
            self.read()
            print("Done.")

            self.build_objects()
            #exit(-1)
        else:
            print("No details file")

    def initialize(self, data = {}):
        print("initializing...\n\n")
        if os.path.exists(self.directory):
            print("Refusing to reinitialize", self.directory)
            return False

        if self.read():
            return False

        self.build_directories()
        self.block(init = True, data = data)
        if self.head and self.head_object:
            self.write()
            return True
        
        return False

    def read(self):
        if os.path.exists(self.directory):
            with open(self.directory + "/details", 'r') as fp:
                buffer = json.loads(fp.read())
                fp.close()

            self.head = buffer['head']
            return True

        return False

    def write(self):            
        with open(self.directory + "/details", 'w') as fp:
            fp.write(json.dumps({'head': self.head}))
            fp.close()