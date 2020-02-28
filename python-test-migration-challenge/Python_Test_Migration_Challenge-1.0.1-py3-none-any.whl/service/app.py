#!/usr/bin/python
import sys
sys.path.append("..")
from provider.python_test_migration \
    import Credentials, MountPoint, Workload, MigrationTarget, Migration
from provider.constant import IP_ADDRESS


#Source Workload1
mountpoint1 = MountPoint('C:\\', 25)
mountpoint2 = MountPoint('D:\\', 25)
mountpoint3 = MountPoint('E:\\', 25)
MountPoints1 = [mountpoint1.get_mountPoint_instances(),
                mountpoint2.get_mountPoint_instances(),
                mountpoint3.get_mountPoint_instances()]

ipaddress1 = IP_ADDRESS('2.2.2.2')
#print(ipaddress1.get_ipaddress())
creds1 = Credentials('alhad', '12345', ipaddress1.get_ipaddress())
print(creds1.get_Credentials()['username'])
source1 = Workload(creds1, MountPoints1)
source1.constrains(ipaddress1.get_ipaddress())

print(source1.get_workload())

#Source Workload2
mountpoint3 = MountPoint('E:\\', 25)
mountpoint4 = MountPoint('F:\\', 25)
MountPoints2 = [mountpoint3.get_mountPoint_instances(), mountpoint4.get_mountPoint_instances()]

ipaddress2 = IP_ADDRESS('2.2.2.2')

creds2 = Credentials('alhad', '12345', ipaddress2.get_ipaddress())
source2 = Workload(creds2, MountPoints2)
source2.constrains(ipaddress2.get_ipaddress())

print(source2.get_workload()['domain'])

source_ips = [source1.get_workload()['domain'], source2.get_workload()['domain']]

source2.checksourceip(source_ips)

#Migration Target1

cloud_type = 'azure'
ipaddress_cloud = IP_ADDRESS('3.3.3.3')
creds_cloud = Credentials('mukul', '234234', ipaddress_cloud.get_ipaddress())
cloud_workload = Workload(creds_cloud)
targetVM = MigrationTarget(cloud_type, creds_cloud, cloud_workload)

#Run Migration

#Selected MountPoints
mountpoint7 = MountPoint('C:\\', 25)
mountpoint8 = MountPoint('D:\\', 25)
selected_mountpoint = [mountpoint7.get_mountPoint_instances(), mountpoint8.get_mountPoint_instances()]

run_migration = Migration(selected_mountpoint, source1, targetVM)
status = run_migration.run(source1, targetVM)
print(status)