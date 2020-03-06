"""Thermal Calculation Tools
Notes
-----
The thermal calculation tools module supports various temperature related methods for SFE.
"""

#############
## IMPORTS ##
#############

import numpy as np
from scipy.interpolate import interp1d

############
## MODULE ##
############

def c_thermal_strain_EC(temp,aggregates='sil'):
	""" returns the total thermal eleongation (thermal strain), with reference to the length at 20°C, accord. EN 1992-1-2 (pp. 26)
	
	Parameters
	----------	
	Temp : float or np.array
		(array of) Temperature in range 20 - 1200 [°C]
		
	aggregates : String
		'sil'  = Siliceous aggregates (default)
		'calc' = Calcareous aggregates

	Returns
	-------
	Eps : float or np.array
		total thermal elongation [-]
		
	Example use
	-----------
	>>> import numpy as np
	>>> import magnelPy.SFE as sfe
	>>> Temp = np.arange(20,1101,20)
	>>> eps = sfe.ThermalTools.c_thermal_strain_EC(Temp,aggregates='calc')	
	"""
	
	out = -1.8e-4 + 9e-6*temp + 2.3e-11*temp**3 if aggregates=='sil' else -1.2e-4 + 6e-6*temp + 1.4e-11*temp**3
	out = np.clip(out,0,0.014) if aggregates=='sil' else np.clip(out,0,0.012) # clip off when max value is reached, in accordance with EN 1992-1-2
	
	return out


def c_density_EC_T(Temp,rho_concrete = 2400):
	""" concrete density at elevated temperature (influenced by water loss), accord. EN 1992-1-2 (pp. 28)
	
	Parameters
	----------	
	rho_concrete : float
		Concrete density at room temperature [kg/m3] (Default: 2400)
	
	Temp : float or np.array
		(array of) Temperature in range 20 - 1200 [°C]

	Returns
	-------
	rho_T : float or np.array
		(Reduced) density for concrete at temperature Temp [kg/m3]
	
	Example use
	-----------
	>>> import numpy as np
	>>> import magnelPy.SFE as sfe
	>>> Temp = np.arange(20,1101,20)
	>>> rho_c = 2300
	>>> rho_T = sfe.ThermalTools.c_density_EC_T(Temp,rho_c)				
	"""

	T_list = [20,115,200,400,1200]
	k_rho_list = [1,1,0.98,0.95,0.88] 
	k_rho_data = interp1d(T_list,k_rho_list)
	k_rho = k_rho_data(Temp)
	
	return(k_rho*rho_concrete)

	
def c_conductivity_EC_T(Temp, limit='lower'):
	""" concrete thermal conductivity at elevated temperature, accord. EN 1992-1-2 (pp. 28)
	
	Parameters
	----------	
	Temp : float or np.array
		(array of) Temperature in range 20 - 1200 [°C]
		
	limit : String
		'lower'  = Siliceous aggregates (default)
		'upper' = Calcareous aggregates

	Returns
	-------
	lambda_c : float or np.array
		 thermal conductivity of concrete [W/m K]
	 
	Example use
	-----------
	>>> import numpy as np
	>>> import magnelPy.SFE as sfe
	>>> Temp = np.arange(20,1101,20)
	>>> eps = sfe.ThermalTools.c_conductivity_EC_T(Temp)		 
	"""
	
	if limit == 'lower':
		return 1.36 - 0.136*(Temp/100) + 0.0057*(Temp/100)*(Temp/100)
	
	if limit == 'upper':
		return 2.00 - 0.2451*(Temp/100) + 0.0107*(Temp/100)*(Temp/100)

	
def c_specific_heat_EC_T(Temp, moisture = 3):
	""" concrete specific heat at elevated temperature, accord. EN 1992-1-2 (pp. 26-27)
	
	Parameters
	----------	
	Temp : float or np.array
		(array of) Temperature in range 20 - 1200 [°C]
		
	moisture : float (percentage)
		moisture content, percentage of concrete weight [w_%] in range 0 - 3 

	Returns
	-------
	c_p : float or np.array
		 specific heat of concrete [J/kg K]
	
	Example use
	-----------
	>>> import numpy as np
	>>> import magnelPy.SFE as sfe
	>>> Temp = np.arange(20,1101,20)
	>>> moisture_c = 2
	>>> eps = sfe.ThermalTools.c_specific_heat_EC_T(Temp,moisture_c)		 
	"""
		
	if moisture > 0:
		u_list = [0.0,1.5,3.0]
		cp_peak_list = [900,1470,2020]
		cp_peak_interp = interp1d(u_list,cp_peak_list) # assumes linear interpolation for moisture percentage values between 0 and 3% 
		cp_peak = cp_peak_interp(moisture)
		
		T_list = [20,99,100,115,200,400,1200]
		cp_list = [900,900,cp_peak,cp_peak,1000,1100,1100]
	if moisture == 0:
		T_list = [20,100,200,400,1200]
		cp_list = [900,900,1000,1100,1100]
		
	cp_interp = interp1d(T_list,cp_list)
	
	return cp_interp(Temp)

#########################
## STAND ALONE - DEBUG ##
#########################

if __name__ == "__main__":

	print("testing")
	
	Temp = np.arange(20,1101,20)
	rho_c = 2300
	rho_T = c_density_EC_T(Temp,rho_c)
	print(rho_T)
