import time
import psutil


class Network:
    @staticmethod
    def io_counters():
        result = psutil.net_io_counters()
        return {'bytes_sent': result.bytes_sent, 'bytes_recv': result.bytes_recv,
                'packets_sent': result.packets_sent, 'packets_recv': result.packets_recv,
                'errin': result.errin, 'errout': result.errout,
                'dropin': result.dropin, 'dropout': result.dropout}

    @staticmethod
    def connections():
        result = psutil.net_connections(kind='inet')
        return result

    @staticmethod
    def if_addrs():
        result = psutil.net_if_addrs()
        return result

    @staticmethod
    def if_stats():
        result = psutil.net_if_stats()
        return result
    #######################################################
    @staticmethod
    def download_kbps():
        start = psutil.net_io_counters().bytes_recv
        time.sleep(1)
        return (psutil.net_io_counters().bytes_recv - start) / 1024 / 125

    @staticmethod
    def upload_kbps():
        start = psutil.net_io_counters().bytes_sent
        time.sleep(1)
        return (psutil.net_io_counters().bytes_sent - start) / 1024 / 125
