""" 
Diehl 1922 Standard Atmosphere constants

Main constants and formulas are are writed down in TABLE-1 from the official
report. Furthermore, the namespace for the variables follows the one used
in the paper.
"""

# Limit altitudes for the model
min_alt, max_alt = 0.00, 10000.00

# Temperature at sea-level in [K]
T0 = 288.00

# Pressure value at sea-level in [Pa]
p0 = 10330.00

# Density value at sea-level in [kg / m3]
rho0 = 1.225

# Gravity value (assumed to be constant) in [m / s2]
g = 9.806

# Temperature gradient absolute value in [K / m]
a = 0.0065

# Gas constant for air in [J / kg / K]
R = 29.27 * g
