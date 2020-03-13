"""Utilities for opentea additionnal processing in tabs"""
import sys
import yaml

from tiny_3d_engine import (load_geo_as_scene, Scene3D)


def process_tab(func_to_call):
    """Execute the function of an external process.external.

    func_to_call : see above for a typical function
    to be called by openTea GUIS

    A typical callback scriptwill look like this:

    ::
        def template_aditional_process(nob_in):
            nob_out = nob_in.copy()
            # Your actions here to change the content of nob_out
            # nob_out["foobar"] = 2 * nob_in["foobar"]
            # (...)
            return nob_out


        if __name__ == "__main__":
            process_tab(template_aditional_process)


    """
    with open(sys.argv[1], "r") as fin:
        data = yaml.load(fin, Loader=yaml.FullLoader)
    data_out = func_to_call(data)
    with open("dataset_to_gui.yml", "w") as fout:
        yaml.dump(data_out, fout, default_flow_style=False)


def update_3d_callback(func_to_call):
    """Execute the function of an external process.external.

    func_to_call : see above for a typical function
    to be called by openTea GUIS

    A typical call back will look like this:

    ::

        def update_3d_scene1(nob_in, scene):
            SIZE = 50
            LENGTH= 200.
            points = list()
            conn = list()
            dx = LENGTH/SIZE
            edges = 0
            for i in range(SIZE):
                for j in range(SIZE):
                    index = len(points)
                    points.append([i*dx, j*dx, 0])
                    points.append([(i+1)*dx, j*dx, 0])
                    points.append([i*dx, (j+1)*dx, 0])
                    points.append([(i+1)*dx, (j+1)*dx, 0])
                    #conn.append([index, index+1, index+2])
                    #conn.append([index+3, index+1, index+2])
                    conn.append([index, index+1])
                    conn.append([index+3, index+1])
                    edges += 1
            scene.add_or_update_part("square1", points, conn, color="#0000ff")
            return scene

        if __name__ == "__main__":
            update_3d_callback(update_3d_scene1)

    """
    with open(sys.argv[1], "r") as fin:
        data = yaml.load(fin, Loader=yaml.FullLoader)

    if sys.argv[2] == "no_scene":
        scene_in = Scene3D()
    else:
        scene_in = load_geo_as_scene(sys.argv[2])

    scene_out = func_to_call(data, scene_in)
    scene_out.dump("scene_to_gui")
