import dill
import sys
sys.path.append("..")
from provider.python_test_migration \
    import Credentials, MountPoint, Workload, MigrationTarget, Migration

def dump_classes():
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
