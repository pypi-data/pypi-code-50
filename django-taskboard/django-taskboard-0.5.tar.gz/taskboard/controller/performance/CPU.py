from cpuinfo import get_cpu_info
import psutil


class CPU:
    @staticmethod
    def brand_bits():
        result = get_cpu_info()
        return {'brand': result.get('brand', ''), 'bits': result.get('bits', 0)}

    @staticmethod
    def cores():
        return {'physical': psutil.cpu_count(logical=False), 'logical': psutil.cpu_count(logical=True)}

    @staticmethod
    def utilization():
        return {'cpu': psutil.cpu_percent(percpu=False)}

    @staticmethod
    def times():
        result = psutil.cpu_times()
        return {'user': round(result.user), 'system': round(result.system), 'idle': round(result.idle)}

    @staticmethod
    def statistics():
        result = psutil.cpu_stats()
        return {'ctx_switches': result.ctx_switches, 'interrupts': result.interrupts,
                'soft_interrupts': result.soft_interrupts, 'syscalls': result.syscalls}

    @staticmethod
    def usage():
        return {'cpu': psutil.cpu_percent(percpu=True)}
