#!/usr/bin/python
import sys
sys.path.append("..")
from provider.python_test_migration \
    import Credentials, MountPoint, Workload, MigrationTarget, Migration


def credentials_create(username, password, ipaddress):
    """Service Layer to Create Credentials"""
    credentials = Credentials(username, password, ipaddress.get_ipaddress())
    return credentials


def credentials_get(credentials):
    """Service Layer to get credentials"""
    return credentials.get_Credentials()


def mountpoint_create(name, size):
    """Service Layer to create mountpoint"""
    mountpoint = MountPoint(name, size)
    return mountpoint


def mountpoint_get(mountpoint):
    """Service Layer to get Mountpoint details"""
    return mountpoint.get_mountPoint_instances()


def mountpoints_list(*args):
    """Service Layer to get mountpoint list"""
    mountpoints_list = []
    for instance in args:
        mountpoints_list.append(instance.get_mountPoint_instances())
    return mountpoints_list


def workload_create(creds, MountPoint):
    """Service Layer to create workload"""
    source = Workload(creds, MountPoint)
    return source


def workload_get(workload):
    """Service Layer to get workload details"""
    workload = workload.get_workload()
    return workload


def constrains(source, ipaddress):
    """Service Layer to check constrains"""
    return source.constrains(ipaddress.get_ipaddress())


def check_duplicate_ip(sources):
    """Service Layer to check sources from duplicate IP addresses"""
    sources_ips = []
    for instance in sources:
        sources_ips.append(instance.get_workload()['domain'])
    return sources[0].checksourceip(sources_ips)


def migrationTarget_Create(cloud_type, creds_cloud, cloud_workload):
    """Service Layer to create Migration target"""
    targetVM = MigrationTarget(cloud_type, creds_cloud, cloud_workload)
    return targetVM


def migrationTarget_get(targerVM):
    """Service Layer to get Migration Target details"""
    return targerVM.get_Migration_Target()


def check_Mounts(selected_mountpoint_list, mountpoint_list1):
    """Service Layer to check mounts if selected mount is present in provided mountpoints or no"""
    selected_mountpoint = []
    mountpoints_provided = []
    for item in selected_mountpoint_list:
        selected_mountpoint.append(item['mount_name'])
    for item in mountpoint_list1:
        mountpoints_provided.append(item['mount_name'])

    for i in selected_mountpoint:
        for j in mountpoints_provided:
            if i == j:
                return {
                    'key': 'success',
                    'message': 'Selected Mount type present in MountTypes provided'
                }
            else:
                return {
                    'key': 'error',
                    'message': 'Selected Mount type not present in MountTypes provided'
                }


def migration(selected_mountpoint, source,
              targetVM, ipaddress,
              sources, mountpoint_list1):
    """Service Layer to run migrations"""
    check_ipchanged = constrains(source, ipaddress)
    if check_ipchanged['key'] == 'error':
        return {
            'key': 'error',
            'message': check_ipchanged['message'],
            'migration_State': 'error'
        }

    check_mul_ips = check_duplicate_ip(sources)
    if check_mul_ips['key'] == 'error':
        return {
            'key': 'error',
            'message': check_mul_ips['message'],
            'migration_State': 'error'
        }

    check_mount = check_Mounts(selected_mountpoint, mountpoint_list1)
    if check_mount['key'] == 'error':
        return {
            'key': 'error',
            'message': check_mount['message'],
            'migration_State': 'error'
        }

    run_migration = Migration(selected_mountpoint, source, targetVM)
    status = run_migration.run(source, targetVM)
    return status
