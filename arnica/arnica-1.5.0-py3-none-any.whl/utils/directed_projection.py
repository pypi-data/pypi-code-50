""" Module to compute the directed projection
of a point to a surface along a direction

::

        ___
            \
             \
        x---->\
               \

OST : Seven nation Army (Westworld), R. Djawadi
"""

from collections import namedtuple
from scipy import spatial
import numpy as np

BIG = 1e6

def projection_kdtree(points,
                      directions,
                      point_surface,
                      normal_surface,
                      **kwargs):
    """
    Project the n points following the direction on the m suface.

    :param points: "p" nparray of shape (n,3),
    :param directions: nparray of shape (n,3),
    :param point_surface: "s" nparray of shape (m,3),
    :param normal_surface: nparray of shape (m,3),
    :param neigbors: nb of neigbors to take into account
    :param tol: maximum distance beyond cyl dist witl bi set to BIG

    :returns:
        - **projected_pts** - "t" nparray of shape (n,3), projected on the surface
        - **indexes** - neigborhood of the points (n,k)
        - **cyl_dist** - cylindrical distance of p with each neighbor (n,k)

    ::

               < shp_dist >
        ______s___________t__________________
              |' .                       A
              |     '  .< cyl_dist >     .
              v                          .< surface_dist>
                     4                   .
                    /                    .
                   /                     .
                  p                      V

              align : alignment (pscal of two unit vectors, in [-1,1])

    - compute a kdtree, and reduce the surfacepoints to a neighborhood indexes [n,k]
    - iterate over all points [n]:
    - compute the distance surface_dist to the surface, for each neighbor [k]
    - compute the alignment align, scal. product of normal and direction [k]
    - compute all points all_pts moved on the surface [k,3]
    - compute shperical distance  for each point to its moved point [k]
    - get the closest point idx closest_pt
    - recompute the cylindrical distance cyl_dist for all the neigborhood
    """

    opts = {'neigbors': 1000, 'tol': 1000.0}
    for keyword in opts:
        if keyword in kwargs:
            opts[keyword] = kwargs[keyword]

    print("KDTree with  "
          + "\n-   Surface points | "
          + str(point_surface.shape[0])
          + "\n- Projected points | "
          + str(points.shape[0])
          + "\n-        Neighbors | "
          + str(opts['neigbors'])
          )

    # First step : find the closest point to the drill from the skin_data points
    kdtree = spatial.cKDTree(point_surface) # pylint: disable=not-callable
    _, index = kdtree.query(points, k=1)

    # Second step : project drill points on the surface along normal's closest point
    projected_pts = project_points(points,
                                   normal_surface[index],
                                   point_surface[index][:, np.newaxis, :]).proj_pts
    projected_pts = np.squeeze(projected_pts, axis=1)

    # Third step : compute cylindrical distances of the k-neigbor points.
    _, indexes = kdtree.query(projected_pts, k=opts["neigbors"])
    cyl_dists = compute_cyl_dist(projected_pts,
                                 directions,
                                 point_surface[indexes],
                                 normal_surface[indexes],
                                 opts["tol"])

    Proj_KDTree = namedtuple("Proj_KDTree", ["moved_pts", "indexes", "cyl_dists"])

    return Proj_KDTree(projected_pts, indexes, cyl_dists)


def compute_cyl_dist(points, directions, points_surf, normals_surf, tol):
    """
    *Compute cylindrical distances*

    For a i-number of points coordinates, compute the cylindrical distances\
    between the i,p-number of nodes with the i-number of axis.

    The array is then clipped according to the node normals and the direction\
    of the drills.

    :param points: Array of dim (i,3) of drill float coordinates
    :type points: np.array
    :param directions: Array of dim (i,3) of drill float axis components
    :type directions: np.array
    :param points_surf: Array of dim (i,p,3) of nodes float coordinates
    :type points_surf: np.array
    :param normals_surf: Array of dim (i,p,3) of nodes float normal components
    :type normals_surf: np.array
    :param params: Dict of parameter

    :returns:

        - **cyl_dists** - Array of dim (i,p) of float cylindrical distances
    """

    proj = project_points(points, directions, points_surf)
    cyl_dists = proj.rad_dists
    axi_dists = proj.axi_dists
    align = np.sum(np.multiply(normals_surf, directions[:, np.newaxis, :]), axis=-1)
    cyl_dists = np.where(align < 0.0,
                         cyl_dists,
                         BIG*np.ones(cyl_dists.shape))
    cyl_dists = np.where(np.absolute(axi_dists) < tol,
                         cyl_dists,
                         BIG*np.ones(cyl_dists.shape))

    return cyl_dists

def project_points(points_source, normals, points_target):
    r"""\
    *Compute the projected points, radial dists and axial dists*

    Compute projection from source points S of dim (k,) or (i,k),\
    on a plan defined by normals N of dim (k,), (i,k), (p,k) or (i,p,k),\
    and points T of dim (k,), (i,k), (p,k), (i,p,k).
    With :

        - **i** : Number of points to project
        - **p** : Number of points defining plans
        - **k** : Dimension of the domain

    ::

               S            T1          T2
                \          ⁄           ⁄
                 \       ⁄           ⁄
           axi_d1 \ ⁄\ ⁄ rad_d1    ⁄
                   \ ⁄           ⁄ rad_d2
                    \          ⁄
                     \       ⁄
               axi_d2 \ ⁄\ ⁄
                       \ ⁄
                        X proj_pt2
                         \
                          N

    S     : Points source
    N     : Normal
    T     : Points target
    axi_d : Axial distance of the point T projected on the axis Ax
    rad_d : Cylindrical or Radial distance between T and the axis Ax

               ------>   ->
    axi_dist = (T - S) . N

    -------------->   ->  ->
    projected_point = S + N * axi_dist

                    ->   -------------->
    rad_dist = norm(T - projected_point)

    :param points_source: Array of source points coordinates
    :type points_source: np.array
    :param proj_axis: Array of normal components defining projection plans
    :type proj_axis: np.array
    :param points_target: Array of points coordinates defining projection plans
    :type points_target: np.array

    :return:

        - **projected_points** - Array of shape points_target.shape of float coordinates
        - **axi_dists** - Array of shape points_target.shape[:-1] of float distances
        - **rad_dists** - Array of shape points_target.shape[:-1] of float distances
    """
    points_source = points_source[:, np.newaxis, :]
    normals = normals[:, np.newaxis, :]

    axi_dists = np.sum(np.multiply((points_target - points_source),
                                   normals),
                       axis=-1)
    projected_points = points_source + np.multiply(normals, axi_dists[:, :, np.newaxis])

    rad_dists = np.linalg.norm(points_target - projected_points, axis=-1)

    Proj = namedtuple('Proj', ['proj_pts', 'axi_dists', 'rad_dists'])

    return Proj(projected_points, axi_dists, rad_dists)
