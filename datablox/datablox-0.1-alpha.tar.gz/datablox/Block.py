from . import Base
import json
import os


class Block(Base.DataObject):
    def __init__(self,
                    directory = None, 
                    digest = None,
                    parent_directory = None,
                    previous = None
                ):
        #   Call the parent class init
        #   (we need the values)
        super().__init__(
            directory=directory, 
            digest=digest, 
            parent_directory=parent_directory
        )

        #   Build block structure
        self.build_keys(
            denormalized=[
                'timestamp',
                'previous'
            ],

            objects = [
                'previous_object'
            ]
        )

        self.refresh()
        if previous:
            self.previous = previous

    def __str__(self):
        if not self.timestamp:
            return "Empty Block, Previous: " + str(self.previous) + " @[" + self.directory() + "]"

        return "Block: " + self.digest() + ", Previous: " + str(self.previous) + " @[" + self.directory().replace("/blocks/" + self.digest(), "") + "]"

    def from_hash(self, digest):
        self.hash_digest_buffer = digest
        self.read()       

        if digest == self.digest():
            return self
        else:
            raise AttributeError("Digests do not match!")

    def move(self):
        if self.previous:
            return self.from_hash(self.previous)
        
        return None