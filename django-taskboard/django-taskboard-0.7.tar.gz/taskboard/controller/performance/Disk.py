import psutil


class Disk:
    @staticmethod
    def partitions():
        return {'partitions': psutil.disk_partitions()}

    @staticmethod
    def usage(device):
        result = psutil.disk_usage(device)
        return {'total': result.total, 'used': result.used, 'free': result.free}

    @staticmethod
    def io_counters():
        result = psutil.disk_io_counters()
        return {'read_count': result.read_count, 'write_count': result.write_count,
                'read_bytes': result.read_bytes, 'write_bytes': result.write_bytes}
