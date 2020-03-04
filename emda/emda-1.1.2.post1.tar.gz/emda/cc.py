# Overall correlation - real space
def cc_overall(arr1, arr2):
    import numpy as np
    cov3_AB = loc3_AB - loc3_A * loc3_B
    var3_A = loc3_A2 - loc3_A**2
    var3_B = loc3_B2 - loc3_B**2
    cov3_AB_ma = ma.masked_less_equal(cov3_AB,0.0)
    var3_A_ma = ma.masked_less_equal(var3_A,0.0)
    var3_B_ma = ma.masked_less_equal(var3_B,0.0)
    cc_realsp_ma = cov3_AB_ma / np.sqrt(var3_A_ma * var3_B_ma)
    halfmaps_cc = cc_realsp_ma.filled(0.0)
    fullmap_cc = 2 * halfmaps_cc / (1.0 + halfmaps_cc)
    return cc