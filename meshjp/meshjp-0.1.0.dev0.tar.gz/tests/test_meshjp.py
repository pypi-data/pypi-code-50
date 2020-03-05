#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import shapely.geometry

from meshjp import containing_mesh, mesh_coord, mesh_cover, contained_mesh


class TestMeshjp(unittest.TestCase):
    def test_containing_mesh(self):
        lon, lat = 139.7514729, 35.7055263
        m1 = containing_mesh(lon, lat, level=1)
        m2 = containing_mesh(lon, lat, level=2)
        m3 = containing_mesh(lon, lat, level=3)
        m4 = containing_mesh(lon, lat, level=4)
        m5 = containing_mesh(lon, lat, level=5)
        m6 = containing_mesh(lon, lat, level=6)
        self.assertEqual(m1, 5339)
        self.assertEqual(m2, 533946)
        self.assertEqual(m3, 53394640)
        self.assertEqual(m4, 533946403)
        self.assertEqual(m5, 5339464031)
        self.assertEqual(m6, 53394640313)
        
        m1b = containing_mesh(lon, lat, level="80km")
        m2b = containing_mesh(lon, lat, level="10km")
        m3b = containing_mesh(lon, lat, level="1km")
        m4b = containing_mesh(lon, lat, level="500m")
        m5b = containing_mesh(lon, lat, level="250m")
        m6b = containing_mesh(lon, lat, level="125m")
        m4c = containing_mesh(lon, lat, level="1/2")
        m5c = containing_mesh(lon, lat, level="1/4")
        m6c = containing_mesh(lon, lat, level="1/8")
        m4d = containing_mesh(lon, lat, level="half")
        m5d = containing_mesh(lon, lat, level="quarter")
        m6d = containing_mesh(lon, lat, level="oneeighth")
        self.assertEqual(m1, m1b)
        self.assertEqual(m2, m2b)
        self.assertEqual(m3, m3b)
        self.assertEqual(m4, m4b)
        self.assertEqual(m5, m5b)
        self.assertEqual(m6, m6b)
        self.assertEqual(m4, m4c)
        self.assertEqual(m5, m5c)
        self.assertEqual(m6, m6c)
        self.assertEqual(m4, m4d)
        self.assertEqual(m5, m5d)
        self.assertEqual(m6, m6d)


    def test_mesh_coord(self):
        mesh = 533946403
        coord = mesh_coord(mesh)
        expect = (139.75, 35.70416666666667, 139.75625, 35.70833333333334)
        for c, e in zip(coord, expect):
            self.assertAlmostEqual(c, e, msg="%f != %f" % (c, e))


    def test_mesh_cover(self):
        g = shapely.geometry.Polygon([
            [139.75403845310208, 35.70740106395741],
            [139.7508305311203, 35.707309588931416],
            [139.75007951259613, 35.70476131387285],
            [139.75265979766846, 35.703942363738165],
            [139.7538185119629, 35.70414710206052],
            [139.75427448749542, 35.70596358712732],
            [139.75403845310208, 35.70740106395741]
        ])
        meshes, fracs = mesh_cover(g, level="125m")
        
        expect = set([5339464013, 5339464031, 5339464033,
                      5339464014, 5339464032, 5339464034])
        self.assertTrue(set(meshes), expect)
    
    
    def test_contained_mesh(self):
        g = shapely.geometry.Polygon([
            [139.75403845310208, 35.70740106395741],
            [139.7508305311203, 35.707309588931416],
            [139.75007951259613, 35.70476131387285],
            [139.75265979766846, 35.703942363738165],
            [139.7538185119629, 35.70414710206052],
            [139.75427448749542, 35.70596358712732],
            [139.75403845310208, 35.70740106395741]
        ])
        meshes = contained_mesh(g, level="125m")
        expect = set([53394640314, 53394640332])
        self.assertTrue(set(meshes), expect)

    

if __name__ == '__main__':
    unittest.main()