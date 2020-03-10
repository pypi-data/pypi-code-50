import psutil


class Memory:
    @staticmethod
    def virtual():
        result = psutil.virtual_memory()
        return {'available': result.available, 'used': result.used, 'free': result.free, 'total': result.total}

    @staticmethod
    def swap():
        result = psutil.swap_memory()
        return {'used': result.used, 'free': result.free, 'total': result.total}
