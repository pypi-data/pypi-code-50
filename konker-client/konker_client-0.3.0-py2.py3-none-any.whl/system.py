import datetime
import time
import platform
import psutil
import netifaces
import os


class System:
    """
    Classe que define o System
    """
    def __init__(self):
        self.hostname = None
        self.ip = None
        self.host_memory_perc = None
        self.host_memory_used = None
        self.host_swap_perc = None
        self.host_swap_used = None
        self.host_cpu = None
        self.host_disks = None
        self.process_memory_perc = None
        self.process_memory_used = None
        self.process_swap_perc = None
        self.process_swap_used = None
        self.process_cpu = None

        self.pid = os.getpid()

    def get_health(self):
        self.hostname = platform.uname()[1]
        self.ip = self.get_ip()
        self.host_memory_perc, self.host_memory_used = self.get_host_memory()
        self.host_swap_perc, self.host_swap_used = self.get_host_swap()
        self.host_cpu = self.get_host_cpu()
        self.host_disks = self.get_host_disks()
        self.process_memory_perc, self.process_memory_used = self.get_process_memory()
        self.process_swap_perc, self.process_swap_used = self.get_process_swap()
        self.process_cpu = self.get_process_cpu()

    def get_process(self) -> psutil.Process:
        """
        Function that returns the Process
        """
        return psutil.Process(self.pid)

    def get_process_swap(self) -> tuple:
        """
        Function that collects and returns the percentage of process and use of the Memory Swap
        """
        process = self.get_process()
        perc = 0
        usage = 0
        if psutil.LINUX and psutil.swap_memory().total > 0:
            perc = (process.memory_full_info().swap /
                    psutil.swap_memory().total) * 100
            usage = process.memory_full_info().swap
        return perc, usage

    def get_process_cpu(self):
        """
        Função que coleta e retorna o percentual de processo de CPU
        """
        pid = os.getpid()
        processo = psutil.Process(pid)
        perc = round(processo.cpu_percent(), 2)
        return perc

    def get_process_memory(self):
        """
        Função que coleta e retorna o percentual de processo e de uso da Memoria
        """
        pid = os.getpid()
        processo = psutil.Process(pid)
        perc = round(processo.memory_percent() / (10**6), 2)
        usage = round(((psutil.virtual_memory().total / (10**6)) * processo.memory_percent()) / 100, 2)
        return perc, usage

    def get_host_cpu(self):
        """
        Função que retorna o percentual de utilização do CPU
        """
        perc = round(psutil.cpu_percent(), 2)
        return perc

    def get_host_memory(self):
        """
        Função que retorna o percentual e uso da memoria
        """
        perc = round(psutil.virtual_memory().percent, 2)
        usage = round(((psutil.virtual_memory().total / (10**6)) * psutil.virtual_memory().percent) / 100, 2)
        return perc, usage

    def get_host_swap(self):
        """
        Função que retorna o percentual e uso da memoria swap
        """
        perc = round(psutil.swap_memory().percent, 2)
        usage = round(psutil.swap_memory().used / (10**6), 2)
        return perc, usage

    def get_ip(self):
        """
        Função que coleta e retorna os IPs
        """
        interfaces = netifaces.interfaces()
        for i in interfaces:
            if i == 'lo':
                continue
            iface = netifaces.ifaddresses(i).get(netifaces.AF_INET)
            if iface is not None:
                return iface[0]['addr']

    def get_host_disks(self):
        """
        Função que coleta e retorna as informações de disco
        """
        resposta = []
        # disk.device para pegar o nome mesmo /dev/sdaX
        for disk in psutil.disk_partitions(all=False):
            if disk.opts == 'cdrom':
                continue
            # print("Mountpoint: ", disk.mountpoint)
            resposta.append({disk.mountpoint: {"perc": psutil.disk_usage(disk.mountpoint).percent, "gb": round(psutil.disk_usage(disk.mountpoint).used / (10**9), 2)}})

        return resposta
