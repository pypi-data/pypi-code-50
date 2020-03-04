import json
import scrybe
import numpy as np
from typing import Dict

from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.depgraph.lineage_graph import LineageGraph, LineageGraphNode


def check_cycle(node: LineageGraphNode, starting_node_id: str, graph: LineageGraph):
    out = False
    for incoming_edge in node.incoming_edges:
        if incoming_edge.src_id == starting_node_id:
            return True
        out = out or check_cycle(node=graph.nodes[incoming_edge.src_id],
                                  starting_node_id=starting_node_id,
                                  graph=graph)
    return out


def is_cyclical(obj):
    obj_lineage = TrackingGraph.get_lineage_of_tracked_object(obj=obj)
    out = False
    for node_id, node in obj_lineage.nodes.items():
        out = out or check_cycle(node=node, starting_node_id=node_id, graph=obj_lineage)
    return out


def is_upload_error_thrown(obj):
    try:
        [x for x in TrackingGraph.get_node_for_tracked_object(obj=obj).prepare_for_upload()]
    except RecursionError:
        return True
    else:
        return False


def check_and_print_dag_status(obj):
    dag_check_failed, error_check_failed = (is_cyclical(obj=obj), is_upload_error_thrown(obj=obj))
    if dag_check_failed:
        print("======== Cycle exists ========")
    else:
        print("** No cycle **")

    if error_check_failed:
        print("======== Error thrown ========")
    else:
        print("** No error thrown **")


a = np.zeros(10)
# print(id(a))
b = np.zeros(10)
# print(id(b))
c = np.zeros(10)

a += b
# print(id(a))
b += c
c += a

check_and_print_dag_status(obj=c)

# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(a).to_json(), indent=2))
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(c).to_json(), indent=2))

c += c
check_and_print_dag_status(obj=c)

"""
[
  {
    "id": "b4d12709-503b-439b-98db-d67fc46df00b",
    "info": {
      "client_id": "b4d12709-503b-439b-98db-d67fc46df00b",
      "oid": 4447912400,
      "version": 0,
      "sequence_num": 2,
      "node_type": "dataset"
    },
    "incoming_edges": []
  },
  {
    "id": "e94258f6-3049-4b2d-855e-cb8d10397a03",
    "info": {
      "client_id": "e94258f6-3049-4b2d-855e-cb8d10397a03",
      "oid": 4447913424,
      "version": 0,
      "sequence_num": 2,
      "node_type": "dataset"
    },
    "incoming_edges": []
  },
  {
    "id": "52b73682-51b1-452b-acf1-ec0b1d211f31",
    "info": {
      "client_id": "52b73682-51b1-452b-acf1-ec0b1d211f31",
      "oid": 4390618320,
      "version": 0,
      "sequence_num": 2,
      "node_type": "dataset"
    },
    "incoming_edges": []
  },
  {
    "id": "21b94440-6b08-4ede-afcc-8f3d0845292e",
    "info": {
      "client_id": "21b94440-6b08-4ede-afcc-8f3d0845292e",
      "oid": 4447913424,
      "version": 1,
      "sequence_num": 2,
      "node_type": "dataset"
    },
    "incoming_edges": [
      {
        "predecessor": "52b73682-51b1-452b-acf1-ec0b1d211f31",
        "info": {
          "processing": "Transformation"
        }
      },
      {
        "predecessor": "e94258f6-3049-4b2d-855e-cb8d10397a03",
        "info": {
          "processing": "Transformation"
        }
      }
    ]
  },
  {
    "id": "94dfe27e-2b51-4df3-9832-280de906173a",
    "info": {
      "client_id": "94dfe27e-2b51-4df3-9832-280de906173a",
      "oid": 4447912400,
      "version": 1,
      "sequence_num": 2,
      "node_type": "dataset"
    },
    "incoming_edges": [
      {
        "predecessor": "21b94440-6b08-4ede-afcc-8f3d0845292e",
        "info": {
          "processing": "Transformation"
        }
      },
      {
        "predecessor": "b4d12709-503b-439b-98db-d67fc46df00b",
        "info": {
          "processing": "Transformation"
        }
      }
    ]
  },
  {
    "id": "1c2ec2af-68d1-493d-b3b4-f06a9aa78ac5",
    "info": {
      "client_id": "1c2ec2af-68d1-493d-b3b4-f06a9aa78ac5",
      "oid": 4447912400,
      "version": 2,
      "sequence_num": 2,
      "node_type": "dataset"
    },
    "incoming_edges": [
      {
        "predecessor": "94dfe27e-2b51-4df3-9832-280de906173a",
        "info": {
          "processing": "Transformation"
        }
      }
    ]
  }
]"""