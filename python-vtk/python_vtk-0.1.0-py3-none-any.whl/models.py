"""Models used in VTK."""
from attr import attrib, attrs

__all__ = [
    "Hexahedron",
    "Point",
    "PolyData",
    "Polygon",
    "Polyhedron",
    "PolyLine",
    "RectilinearGrid",
    "UnstructuredGrid",
]


@attrs
class UnstructuredGrid:
    """An unstructured grid."""

    cells = attrib(factory=list)


@attrs
class PolyData:
    """A poly data collection."""

    @attrs
    class Piece:
        """A piece within a poly data."""

        lines = attrib(factory=list)
        polygons = attrib(factory=list)

    pieces = attrib(factory=lambda: [PolyData.Piece()])


@attrs(cmp=False)
class Point:
    """A point."""

    coordinates = attrib()
    data = attrib(factory=dict)


@attrs
class PolyLine:
    """A poly line."""

    vertices = attrib()


@attrs
class Polygon:
    """A polygon."""

    vertices = attrib()


@attrs
class Hexahedron:
    """A hexahedron."""

    vertices = attrib()
    data = attrib(factory=dict)

    @classmethod
    def from_vtk_cell(cls, vtk_cell, points, data=None):
        """Generate a hexahedron from VTK cells."""
        kwargs = {}
        if data is not None:
            kwargs["data"] = data

        vertices = []
        point_ids = vtk_cell.GetPointIds()
        for i_point in range(vtk_cell.GetNumberOfPoints()):
            vertices.append(points[point_ids.GetId(i_point)])
        return cls(vertices=vertices, **kwargs)


@attrs
class Polyhedron:
    """A polyhedron."""

    faces = attrib()
    data = attrib(factory=dict)


@attrs
class RectilinearGrid:
    """A rectilinear grid."""

    bins = attrib()
    cell_data = attrib(factory=dict)
