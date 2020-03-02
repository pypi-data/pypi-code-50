# import matplotlib.collections
# import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg, scipy.spatial

import materia
from materia.utils import memoize


class TimeSeries:
    def __init__(self, time, series):
        super().__init__()
        self.timeseries = materia.utils.TimeSeries(x=time, y=series)

    @property
    @memoize
    def dt(self):
        return self.timeseries.dt()

    @property
    @memoize
    def T(self):
        return self.timeseries.T()

    def damp(self, final_damp_value=1e-4):
        self.timeseries.damp(final_damp_value=final_damp_value)

    def fourier_transform(self, pad_len=None):
        # FIXME: figure out what to do with fft_freq giving linear frequencies rather than angular frequencies
        return self.timeseries.fourier_transform(pad_len=pad_len)


class Spectrum:
    def __init__(self, x, y):
        super.__init__()
        self.spectrum = materia.utils.Spectrum(x=x, y=y)

    def match(self, match_to, in_place=True, interp_method="cubic_spline"):
        return self.spectrum.match(
            match_to=match_to, in_place=in_place, interp_method=interp_method
        )

    # simple linear extrapolation
    def extrapolate(self, x_extrap_to, in_place=True):
        return self.spectrum.extrapolate(x_extrap_to=x_extrap_to, in_place=in_place)

    def interpolate(self, x_interp_to, in_place=True, method="cubic_spline"):
        return self.spectrum.interpolate(
            x_interp_to=x_interp_to, in_place=in_place, method=method
        )

    def plot(self):
        return self.spectrum.plot()


class Volume:
    def __init__(self, volume):
        self.volume = volume


class Orbitals:
    def __init__(self):
        super().__init__()


class ExcitationEnergies:
    def __init__(self, excitation_energies, oscillator_strengths):
        self.energies = excitation_energies
        self.strengths = oscillator_strengths

    # def plot_stick_spectrum(self):
    #     linecoll = matplotlib.collections.LineCollection(
    #         ((eng, 0), (eng, s)) for eng, s in zip(self.energies, self.strengths)
    #     )
    #     fig, ax = plt.subplots()
    #     ax.add_collection(linecoll)
    #     plt.scatter(self.energies, self.strengths)

    #     plt.show()

    def broaden_spectrum(self, fwhm):
        def f(engs):
            return sum(
                strength * np.exp(-np.log(2) * (2 * (engs - eng) / fwhm) ** 2)
                for eng, strength in zip(self.energies, self.strengths)
            )

        return f

    # def plot_broadened_spectrum(self, fwhm, energies):
    #     fig, ax = plt.subplots()
    #     plt.plot(energies, self.broaden_spectrum(fwhm=fwhm)(energies))

    #     plt.show()

    def molar_absorptivities(self):
        return (
            3
            * np.pi
            * materia.mole.prefactor
            * materia.fundamental_charge.prefactor ** 2
            * self.strengths
            / (
                2e3
                * np.log(10)
                * materia.electron_mass.prefactor
                * np.array([eng.value for eng in self.energies])
            )
        )

    def broaden_molar_absorptivities(self, fwhm):
        def f(engs):
            return sum(
                strength * np.exp(-np.log(2) * (2 * (engs - eng) / fwhm) ** 2)
                for eng, strength in zip(self.energies, self.molar_absorptivities())
            )

        return f

    # def plot_broadened_molar_absorptivities(self, fwhm, energies):
    #     fig, ax = plt.subplots()
    #     plt.plot(energies, self.broaden_molar_absorptivities(fwhm=fwhm)(energies))

    #     plt.show()

    # plt.plot(1240/energies,)

    # def stick_spectrum(self):
    #     # FIXME: just completely fix
    #     def f(w,w0,s):
    #         return np.exp(-((w-w0)/s)**2)
    #     sum(A*f(w=w,w0=W,s=0.5) for A,W in zip(a,ws))
    #     #self._parse()


class Response:
    def __init__(self, applied_field):
        super().__init__()
        self.applied_field = applied_field


class Dipole:
    def __init__(self, dipole_moment):
        super().__init__()
        # dipole_moment.value should be 3x1 column vector
        self.dipole_moment = dipole_moment

    @property
    @memoize
    def norm(self):
        norm_value = np.linalg.norm(self.dipole_moment.value)
        norm_unit = self.dipole_moment.unit

        return materia.Qty(value=norm_value, unit=norm_unit)


class TDDipole(TimeSeries):
    def __init__(self, time, tddipole, applied_field=None):
        super().__init__(time=time, series=tddipole)
        self.tddipole = materia.utils.TimeSeries(x=time, y=tddipole)
        # # tddipole_norm.value should be 1xNt matrix where Nt is number of time steps
        # # tddipole_dir should be 3xNt matrix where Nt is number of time steps and each column is a unit direction vector
        # super().__init__()
        # self.tddipole_moment

    @property
    @memoize
    def dt(self):
        return self.tddipole.dt()

    @property
    @memoize
    def T(self):
        return self.tddipole.T()

    def damp(self, final_damp_value=1e-4):
        self.tddipole.damp(final_damp_value=final_damp_value)

    @property
    @memoize
    def fourier_transform(self, pad_len=None):
        return self.tddipole.fourier_transform(pad_len=pad_len)


class Polarizability:
    def __init__(self, polarizability_tensor, applied_field=None):
        super().__init__()

        self.polarizability_tensor = polarizability_tensor
        self.applied_field = None

    @property
    @memoize
    def isotropic(self):
        isotropic_value = np.trace(a=self.polarizability_tensor.value) / 3
        isotropic_unit = self.polarizability_tensor.unit

        return materia.Qty(value=isotropic_value, unit=isotropic_unit)

    @property
    @memoize
    def anisotropy(self):
        aniso_value = np.sqrt(
            np.trace(
                a=self.polarizability_tensor.value @ self.polarizability_tensor.value
            )
            - 3 * self.isotropic.value ** 2
        )
        aniso_unit = self.polarizability_tensor.unit

        return materia.Qty(value=aniso_value, unit=aniso_unit)

    @property
    @memoize
    def eigenvalues(self):
        return materia.Qty(
            value=np.linalg.eigvals(a=self.polarizability_tensor),
            unit=self.polarizability_tensor.unit,
        )


class TDPolarizability(TimeSeries):
    def __init__(self, time, td_polarizability):
        super().__init__(time=time, series=td_polarizability)

    @property
    @memoize
    def dt(self):
        return self.tddipole.dt()

    @property
    @memoize
    def T(self):
        return self.tddipole.T()

    def damp(self, final_damp_value=1e-4):
        self.tddipole.damp(final_damp_value=final_damp_value)

    @property
    @memoize
    def fourier_transform(self, pad_len=None):
        return self.tddipole.fourier_transform(pad_len=pad_len)


class Permittivity:
    def __init__(self, permittivity):
        self.permittivity = permittivity


class ElectronicExcitation:
    def __init__(
        self,
        excitation_energy,
        oscillator_strength=None,
        transition_moment=None,
        multiplicity=None,
        total_energy=None,
        contributions=None,
    ):
        self.excitation_energy = excitation_energy
        self.oscillator_strength = oscillator_strength
        self.transition_moment = transition_moment
        self.multiplicity = multiplicity
        self.total_energy = total_energy
        self.contributions = contributions


# class ElectronicExcitationContribution:
#     def __init__(self, initial_orbital_occupancy, final_orbital_occupancy, amplitude)
