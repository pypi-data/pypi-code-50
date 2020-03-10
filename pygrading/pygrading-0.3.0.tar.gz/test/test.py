import pygrading.general_test as gg
from pygrading.html import *
import pygrading.docker as pk

name_list = ["node1", "node2", "node3", "node4"]

cluster = pk.Cluster("mpi_cluster", 4, "cg/thread-kernel", network="mpi-network", name_list=name_list)

cluster.clear()

cluster.create()

ret = cluster.exec("hostname")

print(ret)

