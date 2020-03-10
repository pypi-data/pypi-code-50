import psutil


class Process:
    @staticmethod
    def all():
        processes = []
        for process in psutil.process_iter():
            try:
                with process.oneshot():
                    processes.append({
                        'pid': process.pid,
                        'name': process.name(),
                        'username': process.username(),
                        'exe': process.exe(),
                        'cpu': '%.1f' % (process.cpu_percent() / psutil.cpu_count()),
                        'memory': '%.1f' % process.memory_percent()
                    })
            except psutil.AccessDenied:
                pass

        return {'data': processes}

    @staticmethod
    def start(executable_path, executable_args):
        try:
            psutil.Popen([executable_path])
        except Exception:
            return {'success': False}
        else:
            return {'success': True}

    @staticmethod
    def stop(pid):
        try:
            parent = psutil.Process(pid)

            for child in parent.children(recursive=True):
                child.kill()

            parent.kill()
        except Exception:
            return {'success': False}
        else:
            return {'success': True}
