"""IO routines of VTK."""
from collections import OrderedDict, defaultdict
from functools import singledispatch
from os import fspath

import vtk
from numpy import array, asanyarray, prod, ravel, squeeze

from .models import (
    Hexahedron,
    Point,
    PolyData,
    Polygon,
    Polyhedron,
    PolyLine,
    RectilinearGrid,
    UnstructuredGrid,
)

__all__ = ["dump"]


def _get_data_mode(data_mode):
    available_data_modes = {
        "ascii": vtk.vtkXMLWriter.Ascii,  # pylint: disable=no-member
        "binary": vtk.vtkXMLWriter.Binary,  # pylint: disable=no-member
        "appended": vtk.vtkXMLWriter.Appended,  # pylint: disable=no-member
    }
    if data_mode not in available_data_modes:
        raise ValueError(
            f'Invalid data mode "{data_mode}", allowed values are '
            f"{', '.join(available_data_modes)}"
        )
    return available_data_modes[data_mode]


def _get_cell_data_array_rectilinear_grid(field_name, field):
    field = asanyarray(field)
    field_data = vtk.vtkDoubleArray()  # pylint: disable=no-member
    field_data.SetName(field_name)
    field_data.SetNumberOfComponents(int(prod(field.shape[3:])))
    for k in range(field.shape[2]):
        for j in range(field.shape[1]):
            for i in range(field.shape[0]):
                entry = field[i, j, k]
                field_data.InsertNextTuple(ravel(entry, order="C"))
    return field_data


@singledispatch
def dump(obj, file, data_mode="binary"):
    """Dump `obj` to `file`."""
    raise NotImplementedError(
        f"Dumping an object of type {type(obj)} is not yet implemented."
    )


@dump.register(RectilinearGrid)
def _(obj, file, data_mode="binary"):
    rectilinear_grid = vtk.vtkRectilinearGrid()  # pylint: disable=no-member

    rectilinear_grid.SetDimensions([len(bin_) for bin_ in obj.bins])

    x_coordinates = vtk.vtkDoubleArray()  # pylint: disable=no-member
    for x_value in obj.bins[0]:
        x_coordinates.InsertNextTuple([x_value])
    rectilinear_grid.SetXCoordinates(x_coordinates)

    y_coordinates = vtk.vtkDoubleArray()  # pylint: disable=no-member
    for y_value in obj.bins[1]:
        y_coordinates.InsertNextTuple([y_value])
    rectilinear_grid.SetYCoordinates(y_coordinates)

    z_coordinates = vtk.vtkDoubleArray()  # pylint: disable=no-member
    for z_value in obj.bins[2]:
        z_coordinates.InsertNextTuple([z_value])
    rectilinear_grid.SetZCoordinates(z_coordinates)

    for field_name, field in obj.cell_data.items():
        field_data = _get_cell_data_array_rectilinear_grid(field_name, field)
        rectilinear_grid.GetCellData().AddArray(field_data)

    writer = vtk.vtkXMLRectilinearGridWriter()  # pylint: disable=no-member
    writer.SetFileName(file)
    writer.SetInputData(rectilinear_grid)
    writer.SetDataMode(_get_data_mode(data_mode))
    writer.Write()


def _get_poly_line(line, points, point_ids):
    poly_line = vtk.vtkPolyLine()  # pylint: disable=no-member
    poly_line.GetPointIds().SetNumberOfIds(len(line.vertices))
    for i_vertex, vertex in enumerate(line.vertices):
        try:
            point_id = point_ids[vertex]
        except KeyError:
            points.InsertNextPoint(*vertex.coordinates)
            point_ids[vertex] = len(point_ids)
            point_id = point_ids[vertex]
        poly_line.GetPointIds().SetId(i_vertex, point_id)
    return poly_line


def _get_polygon(polygon, points, point_ids):
    polygon_ = vtk.vtkPolygon()  # pylint: disable=no-member
    polygon_.GetPointIds().SetNumberOfIds(len(polygon.vertices))
    for i_vertex, vertex in enumerate(polygon.vertices):
        try:
            point_id = point_ids[vertex]
        except KeyError:
            points.InsertNextPoint(*vertex.coordinates)
            point_ids[vertex] = len(point_ids)
            point_id = point_ids[vertex]
        polygon_.GetPointIds().SetId(i_vertex, point_id)
    return polygon_


def _get_field_data(field_name, field):
    field = array(field)
    field_data = vtk.vtkDoubleArray()  # pylint: disable=no-member
    field_data.SetName(field_name)
    field_data.SetNumberOfComponents(int(prod(field.shape[1:])))
    for entry in field:
        field_data.InsertNextTuple(ravel(entry, order="C"))
    return field_data


def _get_lines(piece, points, point_ids):
    lines = vtk.vtkCellArray()  # pylint: disable=no-member
    for line in piece.lines:
        if isinstance(line, PolyLine):
            lines.InsertNextCell(
                _get_poly_line(line=line, points=points, point_ids=point_ids)
            )
        else:
            raise NotImplementedError()
    return lines


def _get_polygons(piece, points, point_ids):
    polygons = vtk.vtkCellArray()  # pylint: disable=no-member
    for polygon in piece.polygons:
        if isinstance(polygon, Polygon):
            polygons.InsertNextCell(
                _get_polygon(polygon=polygon, points=points, point_ids=point_ids)
            )
        else:
            raise NotImplementedError()
    return polygons


@dump.register(PolyData)
def _(obj, file, data_mode="binary"):
    poly_data = vtk.vtkPolyData()  # pylint: disable=no-member

    point_ids = OrderedDict()
    points = vtk.vtkPoints()  # pylint: disable=no-member

    lines = _get_lines(piece=obj.piece[0], points=points, point_ids=point_ids)
    polygons = _get_polygons(piece=obj.piece[0], points=points, point_ids=point_ids)

    poly_data.SetPoints(points)
    poly_data.SetLines(lines)
    poly_data.SetPolys(polygons)

    point_data = defaultdict(list)
    for point in point_ids:
        for field_name, field_value in point.data.items():
            point_data[field_name].append(field_value)

    for field_name, field in point_data.items():
        poly_data.GetPointData().AddArray(
            _get_field_data(field_name=field_name, field=field)
        )

    writer = vtk.vtkXMLPolyDataWriter()  # pylint: disable=no-member
    writer.SetFileName(file)
    writer.SetInputData(poly_data)
    writer.SetDataMode(_get_data_mode(data_mode))
    writer.Write()


def _get_cell_type_and_ids(cell, points, point_ids):
    if isinstance(cell, Polyhedron):
        cell_type = vtk.VTK_POLYHEDRON  # pylint: disable=no-member

        point_id_list = vtk.vtkIdList()  # pylint: disable=no-member
        point_id_list.InsertNextId(len(cell.faces))
        for face in cell.faces:
            point_id_list.InsertNextId(len(face))
            for vertex in face:
                try:
                    point_id = point_ids[vertex]
                except KeyError:
                    points.InsertNextPoint(*vertex.coordinates)
                    point_ids[vertex] = len(point_ids)
                    point_id = point_ids[vertex]
                point_id_list.InsertNextId(point_id)
    else:
        raise NotImplementedError()
    return cell_type, point_ids


@dump.register(UnstructuredGrid)
def _(obj, file, data_mode="binary"):
    unstructured_grid = vtk.vtkUnstructuredGrid()  # pylint: disable=no-member

    point_ids = OrderedDict()
    points = vtk.vtkPoints()  # pylint: disable=no-member

    cell_types_and_ids = []
    cell_data = defaultdict(list)
    for cell in obj.cells:
        cell_types_and_ids.append(
            _get_cell_type_and_ids(cell=cell, points=points, point_ids=point_ids)
        )

        for field_name, field_value in cell.data.items():
            cell_data[field_name].append(field_value)

    unstructured_grid.SetPoints(points)
    for cell_type, point_id_list in cell_types_and_ids:
        unstructured_grid.InsertNextCell(cell_type, point_id_list)

    for field_name, field in cell_data.items():
        unstructured_grid.GetCellData().AddArray(
            _get_field_data(field_name=field_name, field=field)
        )

    writer = vtk.vtkXMLUnstructuredGridWriter()  # pylint: disable=no-member
    writer.SetFileName(file)
    writer.SetInputData(unstructured_grid)
    writer.SetDataMode(_get_data_mode(data_mode))
    writer.Write()


def _load_points(vtk_object):
    if not (
        isinstance(vtk_object, vtk.vtkDataSet)  # pylint: disable=no-member
        and isinstance(vtk_object, vtk.vtkPointSet)  # pylint: disable=no-member
    ):
        raise TypeError("Object is not of the type we need.")

    points = []
    points_vtk = vtk_object.GetPoints()
    point_data_vtk = vtk_object.GetPointData()
    for i_point in range(points_vtk.GetNumberOfPoints()):
        point_vtk = points_vtk.GetPoint(i_point)

        point_data = {}
        for i_array in range(point_data_vtk.GetNumberOfArrays()):
            array_name = point_data_vtk.GetArrayName(i_array)
            array_vtk = point_data_vtk.GetAbstractArray(array_name)
            assert points_vtk.GetNumberOfPoints() == array_vtk.GetNumberOfTuples()

            value = array_vtk.GetTuple(i_point)
            point_data[array_name] = squeeze(value)

        point = Point(coordinates=asanyarray(point_vtk), data=point_data)
        points.append(point)
    return points


_CELL_MAP = {vtk.vtkHexahedron: Hexahedron}  # pylint: disable=no-member


def _load_cells(vtk_object, points):
    if not (
        isinstance(vtk_object, (vtk.vtkUnstructuredGrid,))  # pylint: disable=no-member
    ):
        raise TypeError("Object is not of the type we need.")

    cells = []
    cell_data_vtk = vtk_object.GetCellData()
    for i_cell in range(vtk_object.GetNumberOfCells()):
        cell_vtk = vtk_object.GetCell(i_cell)

        cell_data = {}
        for i_array in range(cell_data_vtk.GetNumberOfArrays()):
            array_name = cell_data_vtk.GetArrayName(i_array)
            array_vtk = cell_data_vtk.GetAbstractArray(array_name)
            assert vtk_object.GetNumberOfCells() == array_vtk.GetNumberOfTuples()

            value = array_vtk.GetTuple(i_cell)
            cell_data[array_name] = squeeze(value)

        cell = _CELL_MAP[type(cell_vtk)].from_vtk_cell(
            vtk_cell=cell_vtk, points=points, data=cell_data
        )
        cells.append(cell)
    return cells


def _load_unstructured_grid_from_xml(file):
    reader = vtk.vtkXMLUnstructuredGridReader()  # pylint: disable=no-member
    reader.SetFileName(fspath(file))
    reader.Update()

    unstructured_grid_vtk = reader.GetOutput()

    points = _load_points(unstructured_grid_vtk)
    cells = _load_cells(unstructured_grid_vtk, points)
    return UnstructuredGrid(cells=cells)


_SUPPORTED_READERS = {
    vtk.vtkXMLUnstructuredGridReader: (  # pylint: disable=no-member
        _load_unstructured_grid_from_xml
    )
}


def load(file):
    """Load VTK objects from the file `fp`."""
    for reader_class, load_func in _SUPPORTED_READERS.items():
        if reader_class().CanReadFile(fspath(file)):
            return load_func(file)
    raise NotImplementedError(f"Unable to determine format of {file}.")
