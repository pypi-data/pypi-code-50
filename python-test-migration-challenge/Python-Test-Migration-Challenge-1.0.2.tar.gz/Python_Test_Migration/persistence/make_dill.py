import dill
#import sys
#sys.path.append("..")
from Python_Test_Migration.provider.python_test_migration \
    import Credentials, MountPoint, Workload, MigrationTarget, Migration

def dump_classes():
    """Function to dump classes to a persistence text file"""
    credentials = Credentials()
    mountpoint = MountPoint()
    workload = Workload()
    migrationtarget = MigrationTarget()
    migration = Migration()

    with open('../tier_one/python_test_migration', 'wb') as f:
        dill.dump(credentials, f)
        dill.dump(mountpoint, f)
        dill.dump(workload, f)
        dill.dump(migrationtarget, f)
        dill.dump(migration, f)
