import dill

def load_classes():
    with open('../tier_one/python_test_migration', 'rb') as f:
        credentials = dill.load(f)
        mountpoint = dill.load(f)
        workload = dill.load(f)
        migrationtarget = dill.load(f)
        migration = dill.load(f)