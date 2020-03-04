import numpy as np
import pydicom
from scipy.interpolate import RegularGridInterpolator


class DoseGrid:
    def __init__(self, ds):
        self.ds = ds
        self.__set_axes()

        # x and z are swapped in the pixel_array
        self.dose_grid = np.swapaxes(self.ds.pixel_array * self.ds.DoseGridScaling, 0, 2)

    def __set_axes(self):
        self.x_axis = np.arange(self.ds.Columns) * self.ds.PixelSpacing[0] + self.ds.ImagePositionPatient[0]
        self.y_axis = np.arange(self.ds.Rows) * self.ds.PixelSpacing[1] + self.ds.ImagePositionPatient[1]
        self.z_axis = np.array(self.ds.GridFrameOffsetVector) + self.ds.ImagePositionPatient[2]

    def is_point_inside_grid(self, xyz):
        for a, axis in enumerate(self.axes):
            if not (axis[0] <= xyz[a] <= axis[-1]):
                return False
        return True

    def is_coincident(self, other):
        return self.ds.ImagePositionPatient == other.ds.ImagePositionPatient and \
               self.ds.pixel_array.shape == other.ds.pixel_array.shape and \
               self.ds.PixelSpacing == other.ds.PixelSpacing and \
               self.ds.GridFrameOffsetVector == other.ds.GridFrameOffsetVector

    def direct_sum(self, other):
        dose_sum = self.ds.pixel_array * self.ds.DoseGridScaling + other.ds.pixel_array * other.ds.DoseGridScaling
        self.set_pixel_array(dose_sum)

    def set_pixel_array(self, pixel_data):
        self.ds.BitsAllocated = 32
        self.ds.BitsStored = 32
        self.ds.HighBit = 31
        self.ds.PixelData = np.uint32(pixel_data / self.ds.DoseGridScaling).tostring()

    def update_pixel_array(self):
        self.set_pixel_array(np.swapaxes(self.dose_grid, 0, 2))

    @property
    def grid_size(self):
        return [self.ds.Columns, self.ds.Rows, len(self.ds.GridFrameOffsetVector)]

    @property
    def axes(self):
        return [self.x_axis, self.y_axis, self.z_axis]

    def get_xyz(self, ijk):
        """Convert an ijk coordinate into xyz space"""
        i, j, k = ijk[0], ijk[1], ijk[2]
        return np.array([self.x_axis[i], self.y_axis[j], self.z_axis[k]])

    def get_ijk(self, xyz):
        """Convert an xyz coordinate into ijk space"""
        return [int(np.interp(xyz[a], axis, np.arange(self.grid_size[a]))) for a, axis in enumerate(self.axes)]

    def add_dose(self, xyz, dose):
        if self.is_point_inside_grid(xyz):
            ijk = self.get_ijk(xyz)
            self.dose_grid[ijk[0], ijk[1], ijk[2]] += dose


class DoseInterpolator(DoseGrid):
    """Inherit DoseGrid, separate class so a RegularGridInterpolator isn't created for every DoseGrid"""
    def __init__(self, ds):
        DoseGrid.__init__(self, ds)
        self.interpolator = RegularGridInterpolator(points=self.axes, values=self.dose_grid, bounds_error=False)

    def get_dose(self, xyz):
        return self.interpolator([xyz])[0]

    def get_doses(self, list_of_xyz):
        list_of_xyz = [xyz for xyz in list_of_xyz if self.is_point_inside_grid(xyz)]
        return self.interpolator(list_of_xyz), list_of_xyz


def add_dose_grids(ds1, ds2):
    if type(ds1) is not pydicom.FileDataset:
        ds1 = pydicom.read_file(ds1)
    if type(ds2) is not pydicom.FileDataset:
        ds2 = pydicom.read_file(ds2)

    dose_1 = DoseGrid(ds1)
    dose_2 = DoseInterpolator(ds2)

    if dose_1.is_coincident(dose_2):

        print("PlanSum: Using direct summation")
        dose_1.direct_sum(dose_2)

    else:
        slice_count = float(len(dose_1.z_axis))
        for slice_counter, z in enumerate(dose_1.z_axis):
            print("%0.1f%%" % (100 * slice_counter / slice_count))
            points = []
            for x in dose_1.x_axis:
                for y in dose_1.y_axis:
                    points.append([x, y, z])
            doses, points = dose_2.get_doses(points)
            for p, point in enumerate(points):
                dose_1.add_dose(point, doses[p])

        dose_1.update_pixel_array()

    return dose_1.ds