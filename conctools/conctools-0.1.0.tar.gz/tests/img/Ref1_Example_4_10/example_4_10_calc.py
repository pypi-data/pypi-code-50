
from math import pi

Es = 200000
fyk = 500
fck = 25
alpha_cc = 0.85
eps_c3 = 0.00175

# ----------------------------------------
# With reduced strain for pure compression
# ----------------------------------------
'''
This is how it should be done as far as I read EN-1992-1-2 and the
descriptions in "Reinforced concrete design example 4.10"
'''
a25 = pi*25**2/4
a32 = pi*32**2/4

Fc = alpha_cc * fck/1.5 * 350 * 450 / 1000

eps_t = eps_c3 * (99999 - 60) / (99999 - 450/2)
eps_b = eps_c3 * (99999 - 390) / (99999 - 450/2)
sigma_t = eps_t * Es
sigma_b = eps_b * Es

Ast = 2 * a25 * sigma_t / 1000
Asb = 2 * a32 * sigma_b / 1000

N = Fc + Ast + Asb

# --------------------------------------------
# Calculation as done in Example 4.10 directly
# --------------------------------------------
'''
Even though the text and equations in the example states to use eps_c3,
the numbers indicate that the standard eps_cu3=0.0035 was used.

This has the rebars yielding in compression at the point of compression
failure. Something which should not happen acc. to EN-1992-1-1, as the
concrete will crush before that, namely at eps_c3 (which is often lower than
eps_fy).
'''
Fc_example = 0.567 * 25 * 350 * 450 / 1000
Ast_example = 0.87 * 500 * 2 * a25 / 1000
Asb_example = 0.87 * 500 * 2 * a32 / 1000
N_example = Fc_example + Ast_example + Asb_example

# -------------------------------------------------------------------------
# "Exact" numerical calc assuming all steel yielding at compression failure
# -------------------------------------------------------------------------
'''
This calculation tries to use floats with many decimals to get an "exact"
solution for the value in the example.

This has the rebars yielding in compression at the point of compression
failure. Something which should not happen acc. to EN-1992-1-1, as the
concrete will crush before that, namely at eps_c3 (which is often lower than
eps_fy).
'''
Ast_yield = 2*a25*500/1.15 / 1000
Asb_yield = 2*a32*500/1.15 / 1000
N_yield = Fc + Ast_yield + Asb_yield

print(f'N               = {N:.1f} kN')
print(f'N_example       = {N_example:.1f} kN')
print(f'N_yield (exact) = {N_yield:.1f} kN')
