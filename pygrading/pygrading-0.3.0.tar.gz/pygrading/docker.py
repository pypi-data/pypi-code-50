"""
    Name: docker.py
    Author: Charles Zhang <694556046@qq.com>
    Propose: A module to generate html code.
    Coding: UTF-8

    Change Log:
        **2020.03.09**
        Create this file!
"""

import pygrading.general_test as gg
from typing import Dict, List


class Container(object):
    """Container

    Class of a docker container.

    Attributes:
        name: Container name.
        status: Container run status.
        volumes: Volumes mounted to the container.
        network: The network which the container connected.
        options: Container run options.
        cmd: Container start cmd.
        remove_when_stop: Remove container when stop.
    """

    def __init__(self, image_name: str, cmd: str = "bash", name: str = "", network: str = "", volumes: Dict = None,
                 options: List[str] = None, remove_when_stop: bool = False):
        if volumes is None:
            volumes = {}
        if options is None:
            options = ["-itd"]

        self.image_name = image_name
        self.cmd = cmd
        self.name = name
        self.network = network
        self.volumes = volumes
        self.options = options
        self.remove_when_stop = remove_when_stop
        self.id = ""

        # -1: Not Exist, 0: Stopped, 1: Running
        self.status = -1

        if self.remove_when_stop:
            options.append("--rm")

        if self.name:
            options.append("--name {}".format(self.name))

        if self.network:
            options.append("--network {}".format(self.network))

        for v in self.volumes.items():
            options.append("-v {}:{}".format(v[0], v[1]))

        self.docker_run_cmd = " ".join(["docker", "run"] + options + [self.image_name] + [cmd])

    def updateStatus(self):
        # Get running container id
        get_running_container_id_result = gg.utils.bash("docker ps -q")

        running_id_list = get_running_container_id_result[1].split("\n")

        if self.id in running_id_list:
            self.status = 1
            return 1

        # Get all container id
        get_all_container_id_result = gg.utils.bash("docker ps -aq")

        all_id_list = get_all_container_id_result[1].split("\n")

        if self.id in all_id_list:
            self.status = 0
            return 0
        else:
            self.status = -1
            return -1

    def create(self):
        # Create a container
        create_container_result = gg.utils.bash(self.docker_run_cmd)

        # Get container id
        self.id = create_container_result[1][:12]

        # Update status
        self.updateStatus()

        return create_container_result

    def stop(self):
        # Stop container
        stop_container_result = gg.utils.bash("docker stop {}".format(self.name))

        # Update status
        self.updateStatus()

        return stop_container_result

    def start(self):
        # Start container
        start_container_result = gg.utils.bash("docker start {}".format(self.name))

        # Update status
        self.updateStatus()

        return start_container_result

    def restart(self):
        stop_result = self.stop()
        start_result = self.start()
        if start_result[0]:
            return start_result

    def remove(self):
        # Remove container
        stop_container_result = self.stop()
        if stop_container_result[0]:
            return stop_container_result

        remove_container_result = gg.utils.bash("docker rm {}".format(self.name))

        # Update status
        self.updateStatus()

        return remove_container_result

    def exec(self, cmd: str, options: List = None):
        if options is None:
            options = []

        exec_result = gg.utils.bash(" ".join(["docker", "exec"] + options + [self.name] + [cmd]))

        return exec_result


class Cluster(object):
    """Cluster

    Class of a docker container cluster.

    Attributes:
        name: Cluster name.
        status: Cluster node status.
        nodes: Containers in this cluster.
    """

    def __init__(self, name: str, node_num: int, image_name: str, cmd: str = "bash", network: str = "",
                 volumes: Dict = None, options: List[str] = None, name_list: List[str] = None,
                 remove_when_stop: bool = False):
        self.name = name
        self.node_num = node_num
        self.image_name = image_name
        self.cmd = cmd
        self.network = network
        self.volumes = volumes
        self.options = options
        self.name_list = name_list
        self.remove_when_stop = remove_when_stop
        self.status = [-1] * self.node_num
        self.nodes = []

        if name_list is None:
            name_list = []

        for i in range(node_num):
            node_name = self.name + "-" + str(i)
            if name_list:
                node_name = name_list[i]

            node = Container(self.image_name, self.cmd, node_name, self.network, self.volumes, self.options,
                             self.remove_when_stop)

            self.nodes.append(node)

        if not name_list:
            for node in self.nodes:
                name_list.append(node.name)

    def create(self):
        create_result = []
        for i in range(self.node_num):
            ret = self.nodes[i].create()
            create_result.append(ret)
            self.status[i] = self.nodes[i].status
        return create_result

    def start(self):
        start_result = []
        for i in range(self.node_num):
            ret = self.nodes[i].start()
            start_result.append(ret)
            self.status[i] = self.nodes[i].status
        return start_result

    def stop(self):
        stop_result = []
        for i in range(self.node_num):
            ret = self.nodes[i].stop()
            stop_result.append(ret)
            self.status[i] = self.nodes[i].status
        return stop_result

    def clear(self):
        clear_result = []
        for i in range(self.node_num):
            ret = self.nodes[i].remove()
            clear_result.append(ret)
            self.status[i] = self.nodes[i].status
        return clear_result

    def restart(self):
        restart_result = []
        for i in range(self.node_num):
            ret = self.nodes[i].restart()
            restart_result.append(ret)
            self.status[i] = self.nodes[i].status
        return restart_result

    def exec(self, cmd: str, options: List = None):
        exec_result = []
        for i in range(self.node_num):
            ret = self.nodes[i].exec(cmd, options)
            exec_result.append(ret)
            self.status[i] = self.nodes[i].status
        return exec_result


def clear_container(name_list: List[str]):
    stop_container_result = gg.utils.bash(" ".join(["docker", "stop"] + name_list))

    if stop_container_result[0]:
        return stop_container_result

    remove_container_result = gg.utils.bash(" ".join(["docker", "rm"] + name_list))

    return remove_container_result
