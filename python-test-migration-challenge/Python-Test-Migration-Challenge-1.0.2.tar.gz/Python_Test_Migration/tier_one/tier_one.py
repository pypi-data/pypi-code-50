#!/usr/bin/python
from Python_Test_Migration.service.app_service import *
from Python_Test_Migration.provider.constant import IP_ADDRESS
from Python_Test_Migration.persistence.make_dill import dump_classes
from Python_Test_Migration.persistence.un_dill import load_classes
import os


# Loading persistent classes
if os.stat("python_test_migration").st_size != 0:
    load_classes()

# List of sources
sources = []


# Creates credentials object for source 1
ipaddress1 = IP_ADDRESS('1.1.1.1')
credentials1 = credentials_create('test', 'password', ipaddress1)

# Creates credentials object for source 2
ipaddress2 = IP_ADDRESS('2.2.2.2')
credentials2 = credentials_create('test2', 'password', ipaddress2)

# Create Source Mount points for target source 1
mountpoint1 = mountpoint_create('C:\\', 25)
mountpoint2 = mountpoint_create('D:\\', 25)
mountpoint3 = mountpoint_create('E:\\', 25)


# Create Source Mount points for target source 2
mountpoint4 = mountpoint_create('C:\\', 25)
mountpoint5 = mountpoint_create('N:\\', 25)


# Create Mountpoint list for source1
mountpoint_list1 = mountpoints_list(mountpoint1, mountpoint2, mountpoint3)

# Create Mountpoint list for source2
mountpoint_list2 = mountpoints_list(mountpoint4, mountpoint5)


# Create Workload for source 1
source1 = workload_create(credentials1, mountpoint_list1)
sources.append(source1)
# Create Workload for source 2
source2 = workload_create(credentials2, mountpoint_list2)
sources.append(source2)


# Create Target VM
cloud_type = 'aws'
ipaddress_cloud = IP_ADDRESS('3.3.3.3')
creds_cloud = Credentials('mukul', '234234', ipaddress_cloud.get_ipaddress())
cloud_workload = Workload(creds_cloud)

targetVM = migrationTarget_Create(cloud_type,
                                  creds_cloud,
                                  cloud_workload)
if targetVM.cloudtype == 'Not Supported':
    sys.exit()


# Run Migration
# Check for constrains i.e. no source has same IP address and and ip address remains same during workload
# Above checks are being added to Service Layer Migration function

# Created selected mount types
selected_mountpoint = mountpoint_create('C:\\', 25)
selected_mountpoint_list = [selected_mountpoint.get_mountPoint_instances()]


run_migration = migration(selected_mountpoint_list,
                          source1, targetVM,
                          ipaddress1, sources, mountpoint_list1)

print(run_migration)
# Saving classes to filesystem
dump_classes()
