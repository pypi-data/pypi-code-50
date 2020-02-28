#!/usr/bin/python
import time
import copy

class Credentials:
    """Class to create Credentials Objects"""

    def __init__(self, username=None, password=None, domain=None):
        """Init method for initializing variables"""
        self.username = username
        self.password = password
        self.domain = domain

    def get_Credentials(self):
        """Method to get credentials"""
        return {'username': self.username,
                'password': self.password,
                'domain': self.domain}


class MountPoint:
    """Class to create MountPoint Object"""

    def __init__(self, mount_point_name=None, size=None):
        """Init method to initialize MountPoint object"""
        self.mount_point_name = mount_point_name
        self.size = size

    def get_mountPoint_instances(self):
        """Method to get MountPoint instances with size"""
        return {
            'mount_name': self.mount_point_name,
            'size': self.size
        }


class Workload(object):
    """Class to create workload Object"""

    def __init__(self, credentials=None, mountpoint=None):
        """Init method to initialize Workload Object"""
        self.Credentials = credentials
        self.storage = []
        if mountpoint is not None:
            for instance in mountpoint:
                self.storage.append(instance)

    def constrains(self, ipaddress=None):
        """Method to identify if there is an IP address changed over Workload"""
        username = self.Credentials.username
        password = self.Credentials.password
        domain = self.Credentials.domain
        storage = self.storage
        if domain != ipaddress:
            return {'key': 'error',
                    'message': 'IP address changed'}

        if username is None or password is None or domain is None:
            return {'key': 'error',
                    'message': 'Either IP address or password or domain is None'}
        return {'key': 'success',
                'message': 'Constrains passed'}

    def checksourceip(self, source_ips):
        """Method to check if there are multiple sources with same IP address"""

        if len(source_ips) != len(set(source_ips)):
            return {'key': 'error',
                    'message': 'Duplicate IP Addresses exist'}
        return {'key': 'success',
                'message': 'All Sources have separate IP\'s'}

    def get_credentials(self):
        """Method to get credentials"""
        return {
            'username': self.Credentials.username,
            'password': self.Credentials.password
        }

    def get_workload(self):
        """Method to get workload details"""
        return {
            'username': self.Credentials.username,
            'password': self.Credentials.password,
            'domain': self.Credentials.domain,
            'mount_point': self.storage
        }


class MigrationTarget(object):
    """Class to create MigrationTarget object"""

    def __init__(self, cloudtype=None, credentials=None, workload=None):
        """Init method to initialize MigrationTarget object"""
        self.cloudtype = cloudtype
        self.Credentials = credentials
        self.Workload = workload

        if self.cloudtype != 'aws':
            if self.cloudtype != 'azure':
                if self.cloudtype != 'vsphere':
                    if self.cloudtype != 'vcloud':
                        self.cloudtype = 'Not Supported'

    def get_Migration_Target(self):
        """Method to get MigrationTarget Details"""
        storage = self.Workload.storage
        return {
            'cloud_type': self.cloudtype, \
            'username': self.Credentials.username, \
            'password': self.Credentials.password, \
            'domain': self.Credentials.domain, \
            'mountpoint': storage}


class Migration(object):
    """Class to create Migration object"""

    def __init__(self, mountpoint=None, sourceWorkload=None, targetMigrationTarget=None):
        """Init method for initializing Migration object"""
        self.mountpoint = mountpoint
        self.sourceWorkload = sourceWorkload
        self.targetMigrationTarget = targetMigrationTarget
        self.migration_State = 'not_started'

    def run(self, sourceWorkload=None, targetMigrationTarget=None):
        """run method to start migration"""
        time.sleep(1)

        selected_mountpoints = []
        #print(len(self.mountpoint))
        for i in range(0, len(self.mountpoint)):
            selected_mountpoints.append(self.mountpoint[i]['mount_name'])

        # Checking if C:\\ is allowed to migrate
        for directory in selected_mountpoints:
            if 'C:\\' == directory:
                allowed = True
                break
            else:
                allowed = False

        migration_State = 'not_started'

        if allowed:
            try:
                migration_State = 'running'

                # Copying source to TargetVM for migration
                targetMigrationTarget = copy.copy(sourceWorkload)

                # Logic to make sure target only has selected mountpoints
                credentials = Credentials(targetMigrationTarget.get_credentials()['username'],
                                          targetMigrationTarget.get_credentials()['password'])

                targetMigrationTarget = Workload(credentials, self.mountpoint)
                migration_State = 'success'
                return {'key': 'success',
                        'message': 'Migration successfully completed',
                        'migration_State': migration_State}
            except:
                migration_State = 'error'
                return {'key': 'error',
                        'message': 'Error happened during migration',
                        'migration_State': migration_State}

        else:
            migration_State = 'error'
            return {'key': 'error',
                    'message': 'C:\\ not allowed.',
                    'migration_State': migration_State}
