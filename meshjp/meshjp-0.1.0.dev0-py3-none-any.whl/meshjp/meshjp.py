# -*- coding: utf-8 -*-

import itertools
import numpy as np
import shapely.geometry


MESH_LEVEL_ALIAS = {
    "80km": 1, "10km": 2, "1km": 3,
    "500m": 4, "1/2": 4, "half": 4,
    "250m": 5, "1/4": 5, "quarter": 5,
    "125m": 6, "1/8": 6, "oneeighth": 6
}

# lat*120 = km, lon*80 = km
# i.e. km/120 = lat, km/80 = lon
MESH_SIZE_KM = (
    None,  # place holder for index match
    80.0, 10.0, 1.0, 0.5, 0.25, 0.125
)

MESH_SIZE_LONLAT = tuple((None, None) if km is None else (km/80.0, km/120.0) for km in MESH_SIZE_KM)


def mesh_size_in_km(level):
    level = _get_mesh_level(level)
    assert level >= 1 and level < len(MESH_SIZE_KM)
    return MESH_SIZE_KM[level]


def mesh_size_in_lonlat(level):
    level = _get_mesh_level(level)
    assert level >= 1 and level < len(MESH_SIZE_KM)
    return MESH_SIZE_LONLAT[level]


def mesh_level_aliases():
    """
    Mesh level aliases
    
    Returns
    -------
    Dictionary of mesh level aliases
    """
    return dict(v for v in MESH_LEVEL_ALIAS.items())


def _get_mesh_level(level):
    if isinstance(level, int): return level
    assert isinstance(level, str), "level must be str or int"
    if level not in MESH_LEVEL_ALIAS:
        raise ValueError("invalid value for level: %s" % level)
    return MESH_LEVEL_ALIAS[level]


def containing_mesh(lon, lat, level):
    """
    Mesh area containing the specified coordinates
    
    Parameters
    ----------
    lon: float/numpy.array/list
        Londitude
    lat: float/numpy.array/list
        Latitude
    level: int/str
        Mesh level. If int, 1-6.
        Intuitive str expression is also allowed (e.g. "500m").
        See mesh_level_aliases() for possible level expressions.
    
    Returns
    -------
    meshcode as int if lon, lat are scalar.
    meshcode as numpy.array of type int if lon, lat are sequences.
    """
    level = _get_mesh_level(level)
    assert level in [1, 2, 3, 4, 5, 6], "Only level 1-6 is supported"

    lon = np.array(lon)
    lat = np.array(lat)

    # Output parser for convenience.
    # Extract a single element array to a scalar.
    _parse = lambda x: x.item() if len(x.shape) == 0 else x
    
    # level 1
    x = lon - 100; y = lat * 1.5
    a = np.floor(x).astype(np.int64); b = np.floor(y).astype(np.int64)
    mesh = 100*b + a
    if level == 1: return _parse(mesh)

    # level 2
    x = x - a; y = y - b  # set the sourth west corner of the parent mesh as origin
    x = x * 8; y = y * 8
    a = np.floor(x).astype(np.int64); b = np.floor(y).astype(np.int64)
    mesh = 100*mesh + 10*b + a
    if level == 2: return _parse(mesh)

    # level 3
    x = x - a; y = y - b
    x = x * 10; y = y * 10
    a = np.floor(x).astype(np.int64); b = np.floor(y).astype(np.int64)
    mesh = 100*mesh + 10*b + a
    if level == 3: return _parse(mesh)

    # level 4-6
    for j in range(4, 7):
        x = x - a; y = y - b
        x = x * 2; y = y * 2
        a = np.floor(x).astype(np.int64); b = np.floor(y).astype(np.int64)
        mesh = 10*mesh + (1 + a + 2*b)
        if j == level: return _parse(mesh)
    # This part shouldn't be reached
    raise ValueError("level must be 1-6")


def mesh_center(mesh):
    """
    Center coordinates of mesh areas
    
    Parameters
    ----------
    mesh: int/str/list/numpy.array
        mesh code.  If sequence, all codes must be of the same level.
    
    Returns
    -------
    Tuple of lon, lat.
    Shape of each element matches the shape of x.
    """
    x1, y1, x2, y2 = mesh_coord(mesh)
    return (x1 + x2) / 2.0, (y1 + y2) / 2.0


def mesh_coord(mesh):
    """
    Coordinates of mesh areas
    
    Parameters
    ----------
    mesh: int/str/list/numpy.array
        mesh code.  If sequence, all codes must be of the same level.
    
    Returns
    -------
    Tuple of lon1, lat1, lon2, lat2
    Shape of each element matches the shape of x.
    """
    x = np.array(mesh).astype(np.int64)    
    digits = np.floor(np.log10(x)).astype(int) + 1
    if len(digits.shape) > 0:
        digits = np.unique(digits)
        assert len(digits) == 1, "mesh code level must be must be unique (#digits = %s)" % level
        digits = digits.item()
    level = 1 if digits == 4 else \
            2 if digits == 6 else \
            3 if digits == 8 else \
            4 if digits == 9 else \
            5 if digits == 10 else \
            6 if digits == 11 else \
            None
    assert level is not None, "code length is %d, matching no mesh level" % digits
    
    # get mesh size
    width, height = MESH_SIZE_LONLAT[level]
    
    # get south-west coordinates
    # level 1
    b, x = np.divmod(x, 10**(digits-2))
    digits -= 2
    a, x = np.divmod(x, 10**(digits-2))
    digits -= 2
    lon = a + 100.0 ; lat = b * 2.0 / 3   
    if level == 1: return lon, lat, lon + width, lat + height
    
    # level 2
    b, x = np.divmod(x, 10**(digits-1))
    digits -= 1
    a, x = np.divmod(x, 10**(digits-1))
    digits -= 1
    lon += a*MESH_SIZE_LONLAT[2][0]; lat += b*MESH_SIZE_LONLAT[2][1]
    if level == 2: return lon, lat, lon + width, lat + height
    
    # level 3
    b, x = np.divmod(x, 10**(digits-1))
    digits -= 1
    a, x = np.divmod(x, 10**(digits-1))
    digits -= 1
    lon += a*MESH_SIZE_LONLAT[3][0]; lat += b*MESH_SIZE_LONLAT[3][1]
    if level == 3: return lon, lat, lon + width, lat + height

    # level 4
    for j in range(4, 7):
        k, x = np.divmod(x, 10**(digits-1))
        digits -= 1
        b, a = np.divmod(k - 1, 2)
        lon += a*MESH_SIZE_LONLAT[j][0]; lat += b*MESH_SIZE_LONLAT[j][1]
        if level == j: return lon, lat, lon + width, lat + height

    # This part shouldn't be reached
    raise ValueError("level must be 1-6")


def mesh_polygon(mesh):
    """
    Mesh area(s) as polygon object

    Parameters
    ----------
    mesh: int/str/list/numpy.array
        mesh code.  If sequence, all codes must be of the same level.
    
    Returns
    -------
    shapely.geometry.Polygon if mesh is scalar.
    List of shapely.geometry.Polygon if mesh is a sequence.
    """
    mesh = np.array(mesh).astype(np.int64)
    coords = mesh_coord(mesh)
    rects = [shapely.geometry.box(*c) for c in zip(*coords)]
    if len(rects) == 1:
        return rects[0]
    else:
        return rects


def mesh_cover(g, level, rectonly=False):
    """
    Find a set of mesh areas that cover a geometry
    
    Parameters
    ----------
    g: geometry object
        Geometry to be covered
    level: int
        Mesh level.
    rectonly: bool (default: False)
        If the covered areas form a rectngle

    Returns
    -------
    List of mesh codes that cover the geometry.
    """
    level = _get_mesh_level(level)
    
    x1, y1, x2, y2 = g.bounds
    sw, ne = containing_mesh([x1, x2], [y1, y2], level=level)
    centx, centy = mesh_center([sw, ne])
    w, h = MESH_SIZE_LONLAT[level]
    lons, lats = zip(*itertools.product(
        np.arange(centx[0], centx[1] + w, w),
        np.arange(centy[0], centy[1] + h, h)
    ))
    meshes = containing_mesh(lons, lats, level=level)

    rects = mesh_polygon(meshes)
    tmp = [(m, r.intersection(g).area / r.area) \
           for m, r in zip(meshes, rects) if rectonly or r.intersects(g)]
    
    meshes, fractions = zip(*tmp)
    return meshes, fractions


def contained_mesh(g, level):
    """
    Find mesh areas that sit inside a geometry
    
    Parameters
    ----------
    g: geometry object
        Geometry to be covered
    level: int
        Mesh level.
    
    Returns
    -------
    List of mesh codes inside the geometry
    """
    # mesh_cover finds mesh areas that intersects with g
    # cotained mesh should be a subset of covers
    meshes, fracs = mesh_cover(g, level, rectonly=True)
    contained = np.isclose(fracs, 1.0)
    meshes = [m for m, c in zip(meshes, contained) if c]
    return meshes