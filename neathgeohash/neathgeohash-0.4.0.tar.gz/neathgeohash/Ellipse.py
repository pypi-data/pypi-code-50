"""
MIT License

Copyright (c) 2020 Marek Dwulit

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import math
import pygeohash as gh
from geopy import distance
import numpy as np
import json


class Ellipse:
    """
    Ellipse class provide interface to convert EEP95 to geohash coverage with probability values
    """

    def __init__(self, center_lat, center_long, semiMajor, semiMinor, orientation):
        """
        :param center_lat: ellipse center latitude in degrees
        :param center_long: ellipse center longitude in degrees
        :param semiMajor: semiMajor for the ellipse in meters
        :param semiMinor: semiMinor for the ellipse in meters
        :param orientation: rotation of ellipse in degrees
        """
        self.lat = center_lat
        self.long = center_long
        self.semiMajor = semiMajor
        self.semiMinor = semiMinor
        self.theta = orientation
        self.cos_theta = math.cos((self.theta / 180) * math.pi)
        self.sin_theta = math.sin((self.theta / 180) * math.pi)
        self.sqMaj = pow(self.semiMajor, 2)
        self.sqMin = pow(self.semiMinor, 2)
        self.lat_dtom_ratio = 1 / abs(distance.distance((self.lat, self.long), (self.lat + 1, self.long)).m)
        self.long_dtom_ratio = 1 / abs(distance.distance((self.lat, self.long), (self.lat, self.long + 1)).m)

    @staticmethod
    def get_sign(number):
        return np.sign(number)

    def get_yx_distance_from_the_center_to_the_point(self, point_lat, point_long):
        """
        Function computes y (lat) distance and x (long) distance in meters from the ellipse center to the point

        :param point_lat: the point latitude in degrees
        :param point_long: the point longitude in degrees
        :return ym, xm: latitude in meters, longitude in meters
        """
        delta_lat = point_lat - self.lat
        sign_delta_lat = self.get_sign(delta_lat)
        delta_long = point_long - self.long
        sign_delta_long = self.get_sign(delta_long)

        delta_ym = sign_delta_lat * abs(distance.distance((self.lat, self.long), (point_lat, self.long)).m)
        delta_xm = sign_delta_long * abs(distance.distance((self.lat, self.long), (self.lat, point_long)).m)
        return delta_ym, delta_xm

    def is_point_in_ellipse(self, point_lat, point_long):
        """
        Checks if the point is withing the elipse

        :param point_lat: the point latitude in degrees
        :param point_long: the point longitude in degrees
        :return is_in: True or False
        """
        dy, dx = self.get_yx_distance_from_the_center_to_the_point(point_lat, point_long)
        x_sq = pow(dx * self.cos_theta - dy * self.sin_theta, 2)
        y_sq = pow(dx * self.sin_theta + dy * self.cos_theta, 2)
        ell = x_sq / self.sqMin + y_sq / self.sqMaj

        if ell < 1:
            return True
        return False

    def which_geohashs_vertices_are_covered_by_ellipse(self, geohash):
        """
        Method checks if all vertices are inside ellipse

        :param geohash: geohash string
        :return: validates values for each vertex (North West, North East, South East, South West)
        """
        nlat, nlong, dlat, dlong = gh.decode_exactly(geohash)
        is_nw = self.is_point_in_ellipse(nlat + dlat, nlong - dlong)
        is_ne = self.is_point_in_ellipse(nlat + dlat, nlong + dlong)
        is_se = self.is_point_in_ellipse(nlat - dlat, nlong + dlong)
        is_sw = self.is_point_in_ellipse(nlat - dlat, nlong - dlong)
        return is_nw, is_ne, is_se, is_sw

    def is_geohash_covered_by_ellipse(self, geohash):
        """
        Method validates if vertexes of geohash are inside ellipse

        :param geohash:
        :return: (is_fully, is_partially) is_fully indicates if all vertexes are inside the ellipse, at least one
        vertex of the geohash is insde the ellipse
        """
        nw, ne, se, sw = self.which_geohashs_vertices_are_covered_by_ellipse(geohash)
        is_fully = nw and ne and se and sw
        is_partially = nw or ne or se or sw
        return is_fully, is_partially

    def vertices_not_covered_by_ellipse_count(self, geohash):
        """
        Counts how many vertices are covered by the ellipse

        :param geohash: the geohash
        :return: number of vertices for the geohash outside of the elipse
        """
        nw, ne, se, sw = self.which_geohashs_vertices_are_covered_by_ellipse(geohash)
        return sum([not x for x in (nw, ne, se, sw)])

    @staticmethod
    def generate_list_of_children_geohashes(geohash):
        """
        Helper method generating all children for the given geohash

        :param geohash: the geohash
        :return: list of geohash childrens
        """
        symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm',
                   'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
        return [geohash + s for s in symbols]

    def generate_geohash_children_coverage_per_geohash(self, geohash, depth=9):
        """
        Generate list off children of given geohash beneath (within) the ellipse

        :param geohash: the geohash under review
        :param depth: maximal length of geohashes
        :return: list of geohashes within ellipse
        """
        to_process = {geohash: 1}
        ghl = []
        while len(to_process.keys()) > 0:
            g = [*to_process][0]
            to_process.pop(g)
            full_coverage, partial_coverage = self.is_geohash_covered_by_ellipse(g)
            if full_coverage:
                ghl = ghl + [g]
            elif partial_coverage and len(g) < depth:
                sub_geohashes = self.generate_list_of_children_geohashes(g)
                for sg in sub_geohashes:
                    to_process[sg] = 1
        return ghl

    def find_minimial_geohash_which_has_at_least_three_vertices_outside_ellipse(self, lat, long):
        """
        Finds the geohash which has at least one vertex inside the ellipse

        :param lat: Latitude for a point inside the ellipse
        :param long: Longitude for a point inside the ellipse
        :return: The smallest geohash which has only one vertex inside ellipse
        """
        for i in range(10, 1, -2):
            geohash = gh.encode(lat, long, i)
            if self.vertices_not_covered_by_ellipse_count(geohash) >= 3:
                return geohash

    def find_biggest_geohash_with_all_vertices_inside_ellipse(self, lat, long):
        """
        Finds the biggest geohash which has all vertices inside the ellipse

        :param lat: Latitude for a point inside the ellipse
        :param long: Longitude for a point inside the ellipse
        :return: The biggest geohash fitting inside the ellipse
        """
        biggest_ge = None
        for i in range(1, 12):
            geohash = gh.encode(lat, long, i)
            full, partial = self.is_geohash_covered_by_ellipse(geohash)
            if full:
                biggest_ge = geohash
                break
        return biggest_ge

    @staticmethod
    def generate_list_of_gh_neighbors(geohash):
        """
        Generates list of neighbors for the given geohash (same length).

        :param geohash: the geohash
        :return: list of neighbors in the following order west_gh, west_north_gh, north_gh, north_east_gh, east_gh,
        east_south_gh, south_gh, south_west_gh
        """
        lat, lon, lat_err, lon_err = gh.decode_exactly(geohash)
        west_gh = gh.encode(lat, lon - 2 * lon_err, len(geohash))
        west_north_gh = gh.encode(lat + 2 * lat_err, lon - 2 * lon_err, len(geohash))
        north_gh = gh.encode(lat + 2 * lat_err, lon, len(geohash))
        north_east_gh = gh.encode(lat + 2 * lat_err, lon + 2 * lon_err, len(geohash))
        east_gh = gh.encode(lat, lon + 2 * lon_err, len(geohash))
        east_south_gh = gh.encode(lat - 2 * lat_err, lon + 2 * lon_err, len(geohash))
        south_gh = gh.encode(lat, lon - 2 * lon_err, len(geohash))
        south_west_gh = gh.encode(lat - 2 * lat_err, lon - 2 * lon_err, len(geohash))
        return [west_gh, west_north_gh, north_gh, north_east_gh, east_gh, east_south_gh, south_gh, south_west_gh]

    def generate_geohash_coverage(self, rel_depth=1):
        """
        Generates geohash coverage (base 32) for the ellipse

        :param rel_depth: Howe much longer the geohashes should be relatively to the biggest geohash.
        :return: Returns list of geohashes approximating the ellipse
        """
        to_process = {}
        visited = {}
        gh_list = []

        geohash = self.find_biggest_geohash_with_all_vertices_inside_ellipse(self.lat, self.long)
        depth = len(geohash) + rel_depth
        to_process[geohash] = 1
        while len(to_process.keys()) > 0:
            g = [*to_process][0]
            to_process.pop(g)
            if visited.get(g, None) is None:
                visited[g] = 1
                full_coverage, partial_coverage = self.is_geohash_covered_by_ellipse(g)
                if partial_coverage:
                    for vg in self.generate_list_of_gh_neighbors(g):
                        if visited.get(vg, None) is None:
                            to_process[vg] = 1
                        if full_coverage:
                            gh_list = gh_list + [g]
                        else:
                            gh_list = gh_list + self.generate_geohash_children_coverage_per_geohash(g, depth=depth)
        return gh_list

    def generate_generous_geohash_coverage(self):
        """
        Generates generous geohash coverage (base 32) for the ellipse

        :return: Returns list of geohashes approximating the ellipse
        """
        to_process = {}
        visited = {}
        gh_list = []

        geohash = self.find_biggest_geohash_with_all_vertices_inside_ellipse(self.lat, self.long)
        to_process[geohash] = 1
        while len(to_process.keys()) > 0:
            g = [*to_process][0]
            to_process.pop(g)
            if visited.get(g, None) is None:
                visited[g] = 1
                full_coverage, partial_coverage = self.is_geohash_covered_by_ellipse(g)
                if partial_coverage:
                    for vg in self.generate_list_of_gh_neighbors(g):
                        if visited.get(vg, None) is None:
                            to_process[vg] = 1
                gh_list = gh_list + [g]
        return gh_list

    def estimate_probability_coverage(self):
        """
        Estimate probability coverage for each geohahs in generous geohash coverage.

        :return: Returns dictionary with geohashes and estimated probabilities
        """
        ggh = self.generate_generous_geohash_coverage()
        sample_size = 100 * len(ggh)
        gh_len = len(ggh[0])
        ggh_dict = {g: 0 for g in ggh}
        rp = np.random.multivariate_normal((0, 0), [[1, 0], [0, 1]], sample_size)
        scale = [[self.semiMajor / 2, 0], [0, self.semiMinor / 2]]
        r = [[self.cos_theta, self.sin_theta], [-self.sin_theta, self.cos_theta]]
        ep = rp.dot(scale).dot(r)
        rgh = [gh.encode(self.lat + lat_m * self.lat_dtom_ratio, self.long + long_m * self.long_dtom_ratio)[:gh_len]
               for lat_m, long_m in ep]
        for g in rgh:
            if ggh_dict.get(g, None) is not None:
                ggh_dict[g] = ggh_dict[g] + 1 / sample_size
        return ggh_dict

    def estimate_probability_coverage_with_fixed_geohash_depth(self, depth=5):
        """
        Estimate probability coverage for each geohahs in generous geohash coverage where
        geohashes have fixed size (length).

        :return: Returns dictionary with geohashes and estimated probabilities
        """

        def generate_subgoehashes(depth, gh_dict):
            tmp_gh_dic = {}
            keys = list(gh_dict.keys())
            for g in keys:
                for gh_plus in Ellipse.generate_list_of_children_geohashes(g):
                    tmp_gh_dic[gh_plus] = gh_dict[g] / 32
            if len(keys[0]) + 1 < depth:
                tmp_gh_dic = generate_subgoehashes(depth, tmp_gh_dic)
            return tmp_gh_dic

        ggh_dict = self.estimate_probability_coverage()
        fl_ggh_dict = {}
        for key in ggh_dict.keys():
            if len(key) == depth:
                fl_ggh_dict[key] = fl_ggh_dict.get(key, 0) + ggh_dict[key]
            elif len(key) < depth:
                children_dic = generate_subgoehashes(depth, {key: ggh_dict[key]})
                for k in children_dic.keys():
                    fl_ggh_dict[k] = fl_ggh_dict.get(key, 0) + children_dic[k]
            else:
                fl_ggh_dict[key[0:depth]] = fl_ggh_dict.get(key[0:depth], 0) + ggh_dict[key]
        return fl_ggh_dict

    def generate_geojson_for_probability_coverage_with_fixed_geohash_depth(self, depth=5):
        """
        Convert a list of geohash to a geojson feature collection
        :param geohash_list:
        :return:
        """
        features = []
        ghd = self.estimate_probability_coverage_with_fixed_geohash_depth(depth=depth)

        for g in ghd.keys():
            gh_decode = gh.decode_exactly(g)
            _box = {'s': gh_decode[0] - gh_decode[2],
                    'n': gh_decode[0] + gh_decode[2],
                    'e': gh_decode[1] + gh_decode[3],
                    'w': gh_decode[1] - gh_decode[3]}

            to_append = {
                "type": "Feature",
                "properties": {
                    "geohash": g,
                    "prob": ghd[g]
                },
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [
                        [
                            [_box["w"], _box["s"]],
                            [_box["e"], _box["s"]],
                            [_box["e"], _box["n"]],
                            [_box["w"], _box["n"]],
                            [_box["w"], _box["s"]],
                        ]
                    ]
                }
            }
            features += [to_append]

        feature_collection = {
            "type": "FeatureCollection",
            "features": features
        }

        return json.dumps(feature_collection)
