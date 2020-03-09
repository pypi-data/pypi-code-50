from ms_thermo.flame_params import FlameTable
from ms_thermo.yk_from_phi import yk_from_phi
import  pkg_resources

try:
	import cantera as ct
except ModuleNotFoundError:
	print('Cantera could not be loaded. Some functions may not work. Sorry about that..')
def tadia_table(t_fresh_gases, p_fresh_gases, phi, fuel = None):
	"""
	*Compute the adiabatic flame temperature of a premixed kero/air mixture from tables*

	:param t_fresh_gases: Temperature of the fresh gases [K]
	:type t_fresh_gases: float
	:param p_fresh_gases: Pressure of the fresh gases [Pa]
	:type p_fresh_gases: float
	:param phi: Equivalence ratio [-]
	:type phi: float
	:param fuel: Fuel considered
	:type fuel: string

	:returns: 
		- **t_burned_gases** - Temperature of the burned gases
		- **yk_burnt** - Dict of mass fractions of burnt gases
	"""

	case = FlameTable()

	mass_molar = {
			"C": 0.0120107,
			"H": 0.00100797,
			"O2": 0.0319988,
			"N2": 0.0280134
			}

	if fuel == None:
		fuel_table = pkg_resources.resource_filename(
            __name__, f'../INPUT/2S_KERO_BFER.h5')

		c_x = 10
		h_y = 20
		yk_fresh = yk_from_phi(phi, c_x, h_y)
		
		mass_mol_fuel = (c_x * mass_molar["C"] + h_y * mass_molar["H"])
		coeff_o2 = c_x + (h_y / 4)
		stoechio = coeff_o2 * mass_molar["O2"] / mass_mol_fuel

		yk_burnt = dict()
		yk_burnt['N2'] = yk_fresh['N2']

		if phi<=1: 
			yk_burnt["fuel"] = 0
			yk_burnt["O2"] = yk_fresh["O2"] - stoechio * yk_fresh["fuel"]
			yk_burnt["CO2"] = c_x * yk_fresh["fuel"] * (mass_molar["O2"] + mass_molar["C"]) / mass_mol_fuel
			yk_burnt["H2O"] = h_y / 2 * yk_fresh["fuel"] * (0.5 * mass_molar["O2"] + 2 * mass_molar["H"]) / mass_mol_fuel
		else:
			yk_burnt["fuel"] = yk_fresh["fuel"] - yk_fresh["O2"] / stoechio
			yk_burnt["O2"] = 0
			yk_burnt["CO2"] = (1 / ( 1 + h_y / (4 * c_x))) * yk_fresh["O2"] * (mass_molar["O2"] + mass_molar["C"]) / mass_molar["O2"]
			yk_burnt["H2O"] = (1 / (1 / 2 + 2 * c_x / h_y)) * yk_fresh["O2"] * (0.5 * mass_molar["O2"] + 2 * mass_molar["H"]) / mass_molar["O2"]

	else:
		fuel_table = pkg_resources.resource_filename(
            __name__, f'../INPUT/'+fuel+'.h5')

	case.read_table_hdf(fuel_table)
	case.get_params(phi, t_fresh_gases, p_fresh_gases)
	
	t_burned_gases = case.interpolated_data_dict['TEMPERATURE_BURNT'][0]

	return t_burned_gases, yk_burnt

def tadia_cantera(t_fresh_gases, p_fresh_gases, phi, fuel='CH4', cti_file='gri30.cti'):
	"""
	*Compute the adiabatic flame temperature of a premixed kero/air mixture from Cantera*

	:param t_fresh_gases: Temperature of the fresh gases [K]
	:type t_fresh_gases: float
	:param p_fresh_gases: Pressure of the fresh gases [Pa]
	:type p_fresh_gases: float
	:param phi: Equivalence ratio [-]
	:type phi: float
	:param fuel: Fuel considered
	:type fuel: string

	:returns: 
		- **t_burned_gases** - Temperature of the burned gases
		- **yk_burnt** - Dict of mass fractions of burnt gases

	.. note:: **Warning**: This function may not be available if you do not have cantera in your environment
	"""
	case = ct.Solution(cti_file)
	case.TP=t_fresh_gases,p_fresh_gases
	case.set_equivalence_ratio(phi,{fuel:1},{'O2': 1, 'N2': 3.76})
	case.equilibrate('HP')
	t_burned_gases = case.T
	yk_burnt = case.mass_fraction_dict()
	return t_burned_gases, yk_burnt
