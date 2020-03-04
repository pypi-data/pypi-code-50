from LatLon import LatLon
from LatLon import Latitude
from LatLon import Longitude

"""Convert a gecode 2d list from [[deg,min,sec],[deg,min,sec]] to [decimal,decimal] """


def dms2dec(dms):
    dec = list(LatLon(Latitude(degree=dms[0][0], minute=dms[0][1], second=dms[0][2]),
                      Longitude(degree=dms[1][0], minute=dms[1][1], second=dms[1][2])).to_string())

    return [float(dec[0]), float(dec[1])]
