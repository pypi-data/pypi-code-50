import copy

import geoformat


def bbox_extent_to_2d_bbox_extent(bbox_extent):
    mid_idx = int(len(bbox_extent) / 2)
    bbox = (bbox_extent[0], bbox_extent[1], bbox_extent[mid_idx], bbox_extent[mid_idx + 1])

    return bbox


def geometry_type_to_2d_geometry_type(geometry_type):
    if 'POINT' in geometry_type.upper():
        new_geometry_type = 'Point'
    elif 'LINESTRING' in geometry_type.upper():
        new_geometry_type = 'Linestring'
    elif 'POLYGON' in geometry_type.upper():
        new_geometry_type = 'Polygon'
    elif 'GEOMETRY' in geometry_type.upper():
        new_geometry_type = 'Geometry'
    else:
        print("Geometry type unknown")

    if 'MULTI' in geometry_type.upper():
        new_geometry_type = 'Multi' + new_geometry_type

    return new_geometry_type


def coordinates_to_2d_coordinates(coordinates):
    def convert_to_2d(coordinates):

        if isinstance(coordinates[0][0], (int, float)):
            return tuple((coordinate[0], coordinate[1]) for coordinate in coordinates)
        elif isinstance(coordinates[0][0], (tuple, list)):
            new_coordinates = [None] * len(coordinates)
            for i_coord, under_coordinates in enumerate(coordinates):
                new_coordinates[i_coord] = convert_to_2d(under_coordinates)
            return new_coordinates
        else:
            print('error your geometry in input is not correct')

    return convert_to_2d(coordinates)


def geometry_to_2d_geometry(geometry, bbox=True):
    geometry_collection = geometry_to_geometry_collection(geometry, bbox=bbox,
                                                                    geometry_type_filter=geometry['type'])
    for i_geom, geom in enumerate(geometry_collection['geometries']):
        new_geometry_type = geometry_type_to_2d_geometry_type(geom['type'])
        new_geometry = {'type': new_geometry_type}
        new_geometry['coordinates'] = coordinates_to_2d_coordinates(geom['coordinates'])
        if bbox:
            if 'bbox' in geom:
                bbox = bbox_extent_to_2d_bbox_extent(geom['bbox'])
            else:
                bbox = geoformat.coordinates_to_bbox(new_geometry['coordinates'])

            new_geometry['bbox'] = bbox

        geometry_collection['geometries'][i_geom] = new_geometry

    if geometry['type'].upper() == 'GEOMETRYCOLLECTION':
        return geometry_collection
    else:
        return geometry_collection['geometries'][0]


def geolayer_to_2d_geolayer(input_geolayer):
    new_geolayer = {'features': {}, 'metadata': copy.deepcopy(input_geolayer['metadata'])}
    input_geometry_type = input_geolayer['metadata']['geometry_ref']['type']
    if isinstance(input_geometry_type, (list, tuple)):
        new_geometry_type = []
        for geom_type in input_geometry_type:
            new_geometry_type.append(geometry_type_to_2d_geometry_type(geom_type))
    else:
        new_geometry_type = geometry_type_to_2d_geometry_type(input_geometry_type)
    new_geolayer['metadata']['geometry_ref']['type'] = new_geometry_type

    if 'extent' in new_geolayer['metadata']['geometry_ref']:
        bbox_extent = True
    else:
        bbox_extent = False

    for i_feat in input_geolayer['features']:
        input_feature = input_geolayer['features'][i_feat]
        if 'feature_serialize' in input_geolayer['metadata']:
            if input_geolayer['metadata']['feature_serialize'] == True:
                input_feature = eval(input_feature)

        output_feature = copy.deepcopy(input_feature)

        if 'geometry' in input_feature:
            input_geometry = input_feature['geometry']
            new_geometry = geometry_to_2d_geometry(input_geometry, bbox=bbox_extent)
            output_feature['geometry'] = new_geometry

        if 'feature_serialize' in input_geolayer['metadata']:
            if input_geolayer['metadata']['feature_serialize'] == True:
                output_feature = str(output_feature)

        new_geolayer['features'][i_feat] = output_feature

    return new_geolayer


def envelope_to_bbox(envelope):
    """
    Convert envelope to bbox
        format (x_min, y_min, x_max, y_max)
    :param envelope:
    :return: (x_min, y_min, x_max, y_max)
    """

    return envelope[0], envelope[2], envelope[1], envelope[3]


def bbox_to_envelope(bbox):
    """
    Convert bbox to envelope
        format (x_min, x_max, y_min, y_max)
    :param bbox:
    :return: (x_min, x_max, y_min, y_max)
    """

    return bbox[0], bbox[2], bbox[1], bbox[3]


def geometry_to_geometry_collection(geometry, geometry_type_filter=None, bbox=True):
    """
    Transform a geometry to GeometryCollection
    """
    if geometry_type_filter:
        if isinstance(geometry_type_filter, str):
            geometry_type_filter = {geometry_type_filter.upper()}
        elif isinstance(geometry_type_filter, (list, tuple, set)):
            set_geom_type = set([])
            for geometry_type in geometry_type_filter:
                set_geom_type.update(set([geometry_type.upper()]))
            geometry_type_filter = set_geom_type
        else:
            print('geometry_type_filter must be a geometry type or a list of geometry type')
    else:
        geometry_type_filter = geoformat.GEOFORMAT_GEOMETRY_TYPE

    geometry_type = geometry['type']
    if geometry_type.upper() != 'GEOMETRYCOLLECTION':
        if geometry_type.upper() in geometry_type_filter:
            geometry_collection = {'type': 'GeometryCollection', 'geometries': [geometry]}
            if bbox:
                if 'bbox' in geometry:
                    bbox = geometry['bbox']
                else:
                    bbox = geoformat.coordinates_to_bbox(geometry['coordinates'])
                geometry_collection['bbox'] = bbox

            return geometry_collection
        else:
            print('geometry type non compatible with geometry in geoformat_lib :', geometry_type_filter )

    if geometry_type.upper() == 'GEOMETRYCOLLECTION':
        geometry_list = []
        if bbox:
            bbox_geometry_collection = None
        for geometry in geometry['geometries']:
            if geometry['type'].upper() in geometry_type_filter:
                if bbox:
                    if not 'bbox' in geometry:
                        bbox = geoformat.coordinates_to_bbox(geometry['coordinates'])
                        if not bbox_geometry_collection:
                            bbox_geometry_collection = bbox
                        else:
                            bbox_geometry_collection = geoformat.bbox_union(bbox_geometry_collection, bbox)
                        geometry['bbox'] = bbox

                geometry_list.append(geometry)
        geometry_collection = {'type': 'GeometryCollection', 'geometries': geometry_list}
        if bbox:
            geometry_collection['bbox'] = bbox_geometry_collection

        return geometry_collection


def format_coordinates(coordinates_list, format_type=None, precision=None):
    """convert list coordinates to tuple and change precision of coordinates"""
    tmp_list = [None] * len(coordinates_list)
    for i_coord, coordinates in enumerate(coordinates_list):
        if isinstance(coordinates, (int, float)):
            if isinstance(precision, int):
                # TODO if same coordinates that precedent then don't write coordinates
                coordinates = round(coordinates, precision)
            coord_tuple = coordinates
        elif isinstance(coordinates, (list, tuple)):
            coord_tuple = format_coordinates(coordinates)
            if format_type:
                coord_tuple = format_type(coord_tuple)
        else:
            raise TypeError('must be list or tuple containing int or float')
        tmp_list[i_coord] = coord_tuple

    if format_type:
        tmp_list = format_type(tmp_list)

    return tmp_list
