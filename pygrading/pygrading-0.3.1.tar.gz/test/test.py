import pygrading.general_test as gg
from pygrading.html import *
import pygrading.docker as pk

name_list = ["node1", "node2", "node3", "node4"]

cluster = pk.Cluster("mpi_cluster", 4, "cg/thread-kernel", network="mpi-network", name_list=name_list)

cluster.clear()

cluster.create()

gg.utils.bash("echo 111 > 1.txt")

cluster.copy("1.txt", "/")
ret = cluster.exec("cat /1.txt")

print(ret)

