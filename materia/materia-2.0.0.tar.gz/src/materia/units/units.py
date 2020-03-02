import scipy.constants
from .unit import Unit

# UNITLESS
unitless = Unit()

# QUANTITY

mole = mol = Unit(prefactor=scipy.constants.N_A, number=1)

# LENGTH
meter = m = Unit(length=1)
centimeter = cm = 1e-2 * meter
millimeter = mm = 1e-3 * meter
micrometer = micron = 1e-6 * meter
nanometer = nm = 1e-9 * meter
angstrom = 1e-10 * meter
bohr = au_length = scipy.constants.value("Bohr radius") * meter
picometer = pm = 1e-12 * meter
femtometer = fm = 1e-15 * meter
attometer = 1e-18 * meter
kilometer = km = 1e3 * meter
astronomical_unit = au = 1.495978707e11 * meter

# MASS
kilogram = kg = Unit(mass=1)
gram = g = 1e-3 * kilogram
milligram = mg = 1e-6 * kilogram
microgram = 1e-9 * kilogram
amu = scipy.constants.value("atomic mass constant") * kilogram
electron_mass = scipy.constants.m_e * kilogram

# TIME
second = s = Unit(time=1)
millisecond = ms = 1e-3 * second
microsecond = 1e-6 * second
nanosecond = ns = 1e-9 * second
picosecond = ps = 1e-12 * second
femtosecond = fs = 1e-15 * second
au_time = (
    scipy.constants.value("Bohr radius")
    / (scipy.constants.fine_structure * scipy.constants.c)
) * second
attosecond = 1e-18 * second
minute = min = 60 * second
hour = h = 60 * minute
day = d = 24 * hour

# CURRENT
ampere = amp = Unit(electric_current=1)

# TEMPERATURE
kelvin = Unit(absolute_temperature=1)

# NUMBER
mole = Unit(number=1)

# LUMINOUS INTENSITY
candela = Unit(luminous_intensity=1)

# AREA
hectare = ha = 1e4 * (meter ** 2)

# VOLUME
milliliter = ml = centimeter ** 3
liter = L = 1e3 * milliliter
au_volume = au_length ** 3

# CHARGE
coulomb = ampere * second
e = fundamental_charge = au_charge = scipy.constants.e * coulomb

# CGS CHARGE
# FIXME: is it really okay to convert from CGS to SI like this?
statcoulomb = statC = franklin = Fr = electrostatic_unit = esu = coulomb / (
    10 * scipy.constants.c
)

# FORCE
newton = kilogram * meter / (second ** 2)

# PRESSURE
pascal = newton / (meter ** 2)

# ENERGY
joule = newton * meter
calorie = cal = 4.184 * joule
kilocalorie = kcal = calorie * 1e3
electronvolt = ev = eV = scipy.constants.e * joule
hartree = au_energy = (
    scipy.constants.value("electron mass energy equivalent")
    * scipy.constants.fine_structure ** 2
) * joule
rydberg = hartree / 2

# POWER
watt = joule / second

# ELECTRIC POTENTIAL
volt = joule / coulomb

# CAPACITANCE
farad = coulomb / volt

# RESISTANCE
ohm = volt / ampere

# CONDUCTANCE
siemens = 1 / ohm

# MAGNETIC FLUX
weber = volt * second

# MAGNETIC FLUX DENSITY
telsa = weber / (meter ** 2)

# INDUCTANCE
henry = weber / ampere

# ABSORBED DOSE
gray = joule / kilogram

# DIPOLE MOMENT
# FIXME: is it really okay to convert from CGS to SI like this?
debye = (1e-21 / scipy.constants.c) * coulomb * meter
au_dipole_moment = e * bohr

# FREQUENCY
hertz = 1 / second
au_frequency = (
    scipy.constants.fine_structure
    * scipy.constants.c
    / scipy.constants.value("Bohr radius")
) * hertz

# ANGULAR FREQUENCY
radian_per_second = 2 * scipy.constants.pi * hertz
au_angular_frequency = 2 * scipy.constants.pi * au_frequency

# # PLANAR ANGLE
# radian = rad = units.Unit()
# degree = (scipy.constants.pi/180)*radian
#
# # SOLID ANGLE
# steradian = sr = units.Unit()
