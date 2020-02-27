# vim: set fileencoding=utf-8 :

import pkg_resources

from .models import VideoFile, Protocol, Client, ProtocolPurpose
from bob.db.base import SQLiteDatabase

class DatabaseError(Exception):
    def __init__(self, value = 'Database error'):
        self.value = value
    def __str__(self):
        return self.value


class Database(SQLiteDatabase):
    """
    The dataset class opens and maintains a connection opened to the Database.

    It provides many different ways to probe for the characteristics of the data
    and for the data itself inside the database.
    """
    def __init__(self, original_directory = None, original_extension = '.png'):
        # call base class constructor
        sqlite_file = self.get_raw_files()[0]
        SQLiteDatabase.__init__(self, sqlite_file, VideoFile, original_directory, original_extension)

    def get_raw_files(self):
        raw_files = ('db.sql3',)
        return [pkg_resources.resource_filename(__name__, k) for k in raw_files]

    def protocol_names(self):
        """Returns all registered protocol names"""
        return tuple(name[0] for name in self.query(Protocol.name))

    def protocols(self):
        """Returns all registered protocols"""
        return list(self.query(Protocol))

    def has_protocol(self, name):
        """Tells if a certain protocol is available"""
        return self.query(Protocol).filter(Protocol.name==name).count() != 0

    def protocol(self, name):
        """Returns the protocol object in the database given a certain name. Raises
        an error if that does not exist."""
        return self.query(Protocol).filter(Protocol.name==name)

    def purposes(self):
        """Returns the list of allowed purposes"""
        return ProtocolPurpose.PURPOSES

    def groups(self):
        """Returns the list of allowed groups"""
        return ProtocolPurpose.GROUPS

    def file_sessions(self):
        """Returns the list of allowed session numbers"""
        return tuple(i[0] for i in self.query(VideoFile.session_id).distinct() )

    def has_client_id(self, id):
        """Returns True if in the database is a client with a certain
        integer identifier.
        """
        return self.query(Client).filter(Client.id==id).count() != 0

    def presenters(self, protocol):
        """Returns a list of :py:class:`.Client` for the specific query by the user.
        Clients correspond to the database CLIENT entries 
        """

        protocol = self.check_parameters_for_validity(protocol, "protocol", self.protocol_names())

        # Now query the database
        q = self.query(Client)\
                .join(VideoFile)\
                .join(ProtocolPurpose, VideoFile.protocolPurpose)\
                .join(Protocol)\
                .filter(Protocol.name==protocol)\
                .filter(Client.is_presenter)
        return list(q)



    def client(self, id):
        """Returns the client object in the database given a certain id. Raises
        an error if that does not exist."""
        return self.query(Client).filter(Client.id==id).one()


    def objects(self, protocol=None, groups=None, purposes=None, sessions=None):
        """Returns a list of :py:class:`.File` for the specific query by the user.
        """

        protocol = self.check_parameters_for_validity(protocol, "protocol", self.protocol_names())
        purposes = self.check_parameters_for_validity(purposes, "purpose", self.purposes())
        groups = self.check_parameters_for_validity(groups, "group", self.groups())
        sessions = self.check_parameters_for_validity(sessions, "session", self.file_sessions())

        q = self.query(VideoFile)\
                       .join((ProtocolPurpose, VideoFile.protocolPurpose))\
                       .join(Protocol)\
                       .filter(Protocol.name.in_(protocol))\
                       .filter(ProtocolPurpose.group.in_(groups))\
                       .filter(ProtocolPurpose.purpose.in_(purposes))\
                       .filter(VideoFile.session_id.in_(sessions))
        retval = list(set(q))

        # because of the "set" there is no point sorting before:
        retval.sort()
        return retval
