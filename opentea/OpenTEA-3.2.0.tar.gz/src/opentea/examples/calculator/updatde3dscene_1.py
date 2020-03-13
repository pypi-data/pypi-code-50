"""Prototype for 3D interaction in opentea."""

from tiny_3d_engine import Scene3D
from opentea.process_utils import update_3d_callback

def update_3d_scene1(nob_in, scene):
    """Update the list of dimensions."""

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
