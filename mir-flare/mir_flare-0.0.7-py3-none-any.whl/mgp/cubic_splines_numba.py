from numba import jit, njit
import time
import numpy as np
from numpy import zeros, array

from math import floor
from numpy import empty


@njit(cache=True)
def eval_cubic_spline_1(a, b, orders, coefs, point):
    M0 = orders[0]
    start0 = a[0]
    dinv0 = (orders[0]-1.0)/(b[0]-a[0])
    x0 = point[0]
    u0 = (x0 - start0)*dinv0
    i0 = int( floor( u0 ) )
    i0 = max( min(i0,M0-2), 0 )
    t0 = u0-i0
    tp0_0 = t0*t0*t0;  tp0_1 = t0*t0;  tp0_2 = t0;  tp0_3 = 1.0;

    Phi0_0 = 0
    Phi0_1 = 0
    Phi0_2 = 0
    Phi0_3 = 0
    if t0 < 0:
        Phi0_0 = dAd[0,3]*t0 + Ad[0,3]
        Phi0_1 = dAd[1,3]*t0 + Ad[1,3]
        Phi0_2 = dAd[2,3]*t0 + Ad[2,3]
        Phi0_3 = dAd[3,3]*t0 + Ad[3,3]
    elif t0 > 1:
        Phi0_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t0-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
        Phi0_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t0-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
        Phi0_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t0-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
        Phi0_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t0-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
    else:
        Phi0_0 = (Ad[0,0]*tp0_0 + Ad[0,1]*tp0_1 + Ad[0,2]*tp0_2 + Ad[0,3]*tp0_3)
        Phi0_1 = (Ad[1,0]*tp0_0 + Ad[1,1]*tp0_1 + Ad[1,2]*tp0_2 + Ad[1,3]*tp0_3)
        Phi0_2 = (Ad[2,0]*tp0_0 + Ad[2,1]*tp0_1 + Ad[2,2]*tp0_2 + Ad[2,3]*tp0_3)
        Phi0_3 = (Ad[3,0]*tp0_0 + Ad[3,1]*tp0_1 + Ad[3,2]*tp0_2 + Ad[3,3]*tp0_3)

    t = Phi0_0*(coefs[i0+0]) + Phi0_1*(coefs[i0+1]) + Phi0_2*(coefs[i0+2]) + Phi0_3*(coefs[i0+3])
    return t

@njit(cache=True)
def eval_cubic_spline_2(a, b, orders, coefs, point):

    M0 = orders[0]
    start0 = a[0]
    dinv0 = (orders[0]-1.0)/(b[0]-a[0])
    M1 = orders[1]
    start1 = a[1]
    dinv1 = (orders[1]-1.0)/(b[1]-a[1])
    x0 = point[0]
    x1 = point[1]
    u0 = (x0 - start0)*dinv0
    i0 = int( floor( u0 ) )
    i0 = max( min(i0,M0-2), 0 )
    t0 = u0-i0
    u1 = (x1 - start1)*dinv1
    i1 = int( floor( u1 ) )
    i1 = max( min(i1,M1-2), 0 )
    t1 = u1-i1

    tp0_0 = t0*t0*t0;  tp0_1 = t0*t0;  tp0_2 = t0;  tp0_3 = 1.0;
    tp1_0 = t1*t1*t1;  tp1_1 = t1*t1;  tp1_2 = t1;  tp1_3 = 1.0;
    Phi0_0 = 0
    Phi0_1 = 0
    Phi0_2 = 0
    Phi0_3 = 0
    if t0 < 0:
        Phi0_0 = dAd[0,3]*t0 + Ad[0,3]
        Phi0_1 = dAd[1,3]*t0 + Ad[1,3]
        Phi0_2 = dAd[2,3]*t0 + Ad[2,3]
        Phi0_3 = dAd[3,3]*t0 + Ad[3,3]
    elif t0 > 1:
        Phi0_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t0-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
        Phi0_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t0-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
        Phi0_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t0-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
        Phi0_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t0-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
    else:
        Phi0_0 = (Ad[0,0]*tp0_0 + Ad[0,1]*tp0_1 + Ad[0,2]*tp0_2 + Ad[0,3]*tp0_3)
        Phi0_1 = (Ad[1,0]*tp0_0 + Ad[1,1]*tp0_1 + Ad[1,2]*tp0_2 + Ad[1,3]*tp0_3)
        Phi0_2 = (Ad[2,0]*tp0_0 + Ad[2,1]*tp0_1 + Ad[2,2]*tp0_2 + Ad[2,3]*tp0_3)
        Phi0_3 = (Ad[3,0]*tp0_0 + Ad[3,1]*tp0_1 + Ad[3,2]*tp0_2 + Ad[3,3]*tp0_3)

    Phi1_0 = 0
    Phi1_1 = 0
    Phi1_2 = 0
    Phi1_3 = 0
    if t1 < 0:
        Phi1_0 = dAd[0,3]*t1 + Ad[0,3]
        Phi1_1 = dAd[1,3]*t1 + Ad[1,3]
        Phi1_2 = dAd[2,3]*t1 + Ad[2,3]
        Phi1_3 = dAd[3,3]*t1 + Ad[3,3]
    elif t1 > 1:
        Phi1_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t1-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
        Phi1_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t1-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
        Phi1_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t1-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
        Phi1_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t1-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
    else:
        Phi1_0 = (Ad[0,0]*tp1_0 + Ad[0,1]*tp1_1 + Ad[0,2]*tp1_2 + Ad[0,3]*tp1_3)
        Phi1_1 = (Ad[1,0]*tp1_0 + Ad[1,1]*tp1_1 + Ad[1,2]*tp1_2 + Ad[1,3]*tp1_3)
        Phi1_2 = (Ad[2,0]*tp1_0 + Ad[2,1]*tp1_1 + Ad[2,2]*tp1_2 + Ad[2,3]*tp1_3)
        Phi1_3 = (Ad[3,0]*tp1_0 + Ad[3,1]*tp1_1 + Ad[3,2]*tp1_2 + Ad[3,3]*tp1_3)
    t = Phi0_0*(Phi1_0*(coefs[i0+0,i1+0]) + \
        Phi1_1*(coefs[i0+0,i1+1]) + \
        Phi1_2*(coefs[i0+0,i1+2]) + \
        Phi1_3*(coefs[i0+0,i1+3])) + \
        Phi0_1*(Phi1_0*(coefs[i0+1,i1+0]) + \
        Phi1_1*(coefs[i0+1,i1+1]) + \
        Phi1_2*(coefs[i0+1,i1+2]) + \
        Phi1_3*(coefs[i0+1,i1+3])) + \
        Phi0_2*(Phi1_0*(coefs[i0+2,i1+0]) + \
        Phi1_1*(coefs[i0+2,i1+1]) + \
        Phi1_2*(coefs[i0+2,i1+2]) + \
        Phi1_3*(coefs[i0+2,i1+3])) + \
        Phi0_3*(Phi1_0*(coefs[i0+3,i1+0]) + \
        Phi1_1*(coefs[i0+3,i1+1]) + \
        Phi1_2*(coefs[i0+3,i1+2]) + \
        Phi1_3*(coefs[i0+3,i1+3]))
    return t

@njit(cache=True)
def eval_cubic_spline_3(a, b, orders, coefs, point):

    M0 = orders[0]
    start0 = a[0]
    dinv0 = (orders[0]-1.0)/(b[0]-a[0])
    M1 = orders[1]
    start1 = a[1]
    dinv1 = (orders[1]-1.0)/(b[1]-a[1])
    M2 = orders[2]
    start2 = a[2]
    dinv2 = (orders[2]-1.0)/(b[2]-a[2])
    x0 = point[0]
    x1 = point[1]
    x2 = point[2]
    u0 = (x0 - start0)*dinv0
    i0 = int( floor( u0 ) )
    i0 = max( min(i0,M0-2), 0 )
    t0 = u0-i0
    u1 = (x1 - start1)*dinv1
    i1 = int( floor( u1 ) )
    i1 = max( min(i1,M1-2), 0 )
    t1 = u1-i1
    u2 = (x2 - start2)*dinv2
    i2 = int( floor( u2 ) )
    i2 = max( min(i2,M2-2), 0 )
    t2 = u2-i2
    tp0_0 = t0*t0*t0;  tp0_1 = t0*t0;  tp0_2 = t0;  tp0_3 = 1.0;
    tp1_0 = t1*t1*t1;  tp1_1 = t1*t1;  tp1_2 = t1;  tp1_3 = 1.0;
    tp2_0 = t2*t2*t2;  tp2_1 = t2*t2;  tp2_2 = t2;  tp2_3 = 1.0;
    Phi0_0 = 0
    Phi0_1 = 0
    Phi0_2 = 0
    Phi0_3 = 0
    if t0 < 0:
        Phi0_0 = dAd[0,3]*t0 + Ad[0,3]
        Phi0_1 = dAd[1,3]*t0 + Ad[1,3]
        Phi0_2 = dAd[2,3]*t0 + Ad[2,3]
        Phi0_3 = dAd[3,3]*t0 + Ad[3,3]
    elif t0 > 1:
        Phi0_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t0-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
        Phi0_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t0-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
        Phi0_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t0-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
        Phi0_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t0-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
    else:
        Phi0_0 = (Ad[0,0]*tp0_0 + Ad[0,1]*tp0_1 + Ad[0,2]*tp0_2 + Ad[0,3]*tp0_3)
        Phi0_1 = (Ad[1,0]*tp0_0 + Ad[1,1]*tp0_1 + Ad[1,2]*tp0_2 + Ad[1,3]*tp0_3)
        Phi0_2 = (Ad[2,0]*tp0_0 + Ad[2,1]*tp0_1 + Ad[2,2]*tp0_2 + Ad[2,3]*tp0_3)
        Phi0_3 = (Ad[3,0]*tp0_0 + Ad[3,1]*tp0_1 + Ad[3,2]*tp0_2 + Ad[3,3]*tp0_3)

    Phi1_0 = 0
    Phi1_1 = 0
    Phi1_2 = 0
    Phi1_3 = 0
    if t1 < 0:
        Phi1_0 = dAd[0,3]*t1 + Ad[0,3]
        Phi1_1 = dAd[1,3]*t1 + Ad[1,3]
        Phi1_2 = dAd[2,3]*t1 + Ad[2,3]
        Phi1_3 = dAd[3,3]*t1 + Ad[3,3]
    elif t1 > 1:
        Phi1_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t1-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
        Phi1_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t1-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
        Phi1_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t1-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
        Phi1_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t1-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
    else:
        Phi1_0 = (Ad[0,0]*tp1_0 + Ad[0,1]*tp1_1 + Ad[0,2]*tp1_2 + Ad[0,3]*tp1_3)
        Phi1_1 = (Ad[1,0]*tp1_0 + Ad[1,1]*tp1_1 + Ad[1,2]*tp1_2 + Ad[1,3]*tp1_3)
        Phi1_2 = (Ad[2,0]*tp1_0 + Ad[2,1]*tp1_1 + Ad[2,2]*tp1_2 + Ad[2,3]*tp1_3)
        Phi1_3 = (Ad[3,0]*tp1_0 + Ad[3,1]*tp1_1 + Ad[3,2]*tp1_2 + Ad[3,3]*tp1_3)

    Phi2_0 = 0
    Phi2_1 = 0
    Phi2_2 = 0
    Phi2_3 = 0
    if t2 < 0:
        Phi2_0 = dAd[0,3]*t2 + Ad[0,3]
        Phi2_1 = dAd[1,3]*t2 + Ad[1,3]
        Phi2_2 = dAd[2,3]*t2 + Ad[2,3]
        Phi2_3 = dAd[3,3]*t2 + Ad[3,3]
    elif t2 > 1:
        Phi2_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t2-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
        Phi2_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t2-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
        Phi2_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t2-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
        Phi2_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t2-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
    else:
        Phi2_0 = (Ad[0,0]*tp2_0 + Ad[0,1]*tp2_1 + Ad[0,2]*tp2_2 + Ad[0,3]*tp2_3)
        Phi2_1 = (Ad[1,0]*tp2_0 + Ad[1,1]*tp2_1 + Ad[1,2]*tp2_2 + Ad[1,3]*tp2_3)
        Phi2_2 = (Ad[2,0]*tp2_0 + Ad[2,1]*tp2_1 + Ad[2,2]*tp2_2 + Ad[2,3]*tp2_3)
        Phi2_3 = (Ad[3,0]*tp2_0 + Ad[3,1]*tp2_1 + Ad[3,2]*tp2_2 + Ad[3,3]*tp2_3)


    t = Phi0_0*(Phi1_0*(Phi2_0*(coefs[i0+0,i1+0,i2+0]) + Phi2_1*(coefs[i0+0,i1+0,i2+1]) + Phi2_2*(coefs[i0+0,i1+0,i2+2]) + Phi2_3*(coefs[i0+0,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+0,i1+1,i2+0]) + Phi2_1*(coefs[i0+0,i1+1,i2+1]) + Phi2_2*(coefs[i0+0,i1+1,i2+2]) + Phi2_3*(coefs[i0+0,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+0,i1+2,i2+0]) + Phi2_1*(coefs[i0+0,i1+2,i2+1]) + Phi2_2*(coefs[i0+0,i1+2,i2+2]) + Phi2_3*(coefs[i0+0,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+0,i1+3,i2+0]) + Phi2_1*(coefs[i0+0,i1+3,i2+1]) + Phi2_2*(coefs[i0+0,i1+3,i2+2]) + Phi2_3*(coefs[i0+0,i1+3,i2+3]))) + Phi0_1*(Phi1_0*(Phi2_0*(coefs[i0+1,i1+0,i2+0]) + Phi2_1*(coefs[i0+1,i1+0,i2+1]) + Phi2_2*(coefs[i0+1,i1+0,i2+2]) + Phi2_3*(coefs[i0+1,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+1,i1+1,i2+0]) + Phi2_1*(coefs[i0+1,i1+1,i2+1]) + Phi2_2*(coefs[i0+1,i1+1,i2+2]) + Phi2_3*(coefs[i0+1,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+1,i1+2,i2+0]) + Phi2_1*(coefs[i0+1,i1+2,i2+1]) + Phi2_2*(coefs[i0+1,i1+2,i2+2]) + Phi2_3*(coefs[i0+1,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+1,i1+3,i2+0]) + Phi2_1*(coefs[i0+1,i1+3,i2+1]) + Phi2_2*(coefs[i0+1,i1+3,i2+2]) + Phi2_3*(coefs[i0+1,i1+3,i2+3]))) + Phi0_2*(Phi1_0*(Phi2_0*(coefs[i0+2,i1+0,i2+0]) + Phi2_1*(coefs[i0+2,i1+0,i2+1]) + Phi2_2*(coefs[i0+2,i1+0,i2+2]) + Phi2_3*(coefs[i0+2,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+2,i1+1,i2+0]) + Phi2_1*(coefs[i0+2,i1+1,i2+1]) + Phi2_2*(coefs[i0+2,i1+1,i2+2]) + Phi2_3*(coefs[i0+2,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+2,i1+2,i2+0]) + Phi2_1*(coefs[i0+2,i1+2,i2+1]) + Phi2_2*(coefs[i0+2,i1+2,i2+2]) + Phi2_3*(coefs[i0+2,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+2,i1+3,i2+0]) + Phi2_1*(coefs[i0+2,i1+3,i2+1]) + Phi2_2*(coefs[i0+2,i1+3,i2+2]) + Phi2_3*(coefs[i0+2,i1+3,i2+3]))) + Phi0_3*(Phi1_0*(Phi2_0*(coefs[i0+3,i1+0,i2+0]) + Phi2_1*(coefs[i0+3,i1+0,i2+1]) + Phi2_2*(coefs[i0+3,i1+0,i2+2]) + Phi2_3*(coefs[i0+3,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+3,i1+1,i2+0]) + Phi2_1*(coefs[i0+3,i1+1,i2+1]) + Phi2_2*(coefs[i0+3,i1+1,i2+2]) + Phi2_3*(coefs[i0+3,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+3,i1+2,i2+0]) + Phi2_1*(coefs[i0+3,i1+2,i2+1]) + Phi2_2*(coefs[i0+3,i1+2,i2+2]) + Phi2_3*(coefs[i0+3,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+3,i1+3,i2+0]) + Phi2_1*(coefs[i0+3,i1+3,i2+1]) + Phi2_2*(coefs[i0+3,i1+3,i2+2]) + Phi2_3*(coefs[i0+3,i1+3,i2+3])))
    return t

@njit(cache=True)
def vec_eval_cubic_spline_1(a, b, orders, coefs, points, out):

    d = a.shape[0]
    N = points.shape[0]

    for n in range(N):

        x0 = points[n,0]
        M0 = orders[0]
        start0 = a[0]
        dinv0 = (orders[0]-1.0)/(b[0]-a[0])
        u0 = (x0 - start0)*dinv0
        i0 = int( floor( u0 ) )
        i0 = max( min(i0,M0-2), 0 )
        t0 = u0-i0
        tp0_0 = t0*t0*t0;  tp0_1 = t0*t0;  tp0_2 = t0;  tp0_3 = 1.0;
        Phi0_0 = 0
        Phi0_1 = 0
        Phi0_2 = 0
        Phi0_3 = 0
        if t0 < 0:
            Phi0_0 = dAd[0,3]*t0 + Ad[0,3]
            Phi0_1 = dAd[1,3]*t0 + Ad[1,3]
            Phi0_2 = dAd[2,3]*t0 + Ad[2,3]
            Phi0_3 = dAd[3,3]*t0 + Ad[3,3]
        elif t0 > 1:
            Phi0_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t0-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
            Phi0_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t0-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
            Phi0_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t0-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
            Phi0_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t0-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
        else:
            Phi0_0 = (Ad[0,0]*tp0_0 + Ad[0,1]*tp0_1 + Ad[0,2]*tp0_2 + Ad[0,3]*tp0_3)
            Phi0_1 = (Ad[1,0]*tp0_0 + Ad[1,1]*tp0_1 + Ad[1,2]*tp0_2 + Ad[1,3]*tp0_3)
            Phi0_2 = (Ad[2,0]*tp0_0 + Ad[2,1]*tp0_1 + Ad[2,2]*tp0_2 + Ad[2,3]*tp0_3)
            Phi0_3 = (Ad[3,0]*tp0_0 + Ad[3,1]*tp0_1 + Ad[3,2]*tp0_2 + Ad[3,3]*tp0_3)


        out[n] = Phi0_0*(coefs[i0+0]) + Phi0_1*(coefs[i0+1]) + Phi0_2*(coefs[i0+2]) + Phi0_3*(coefs[i0+3])

@njit(cache=True)
def vec_eval_cubic_spline_2(a, b, orders, coefs, points, out):

    d = a.shape[0]
    N = points.shape[0]

    for n in range(N):

        x0 = points[n,0]
        x1 = points[n,1]
        M0 = orders[0]
        start0 = a[0]
        dinv0 = (orders[0]-1.0)/(b[0]-a[0])
        M1 = orders[1]
        start1 = a[1]
        dinv1 = (orders[1]-1.0)/(b[1]-a[1])
        u0 = (x0 - start0)*dinv0
        i0 = int( floor( u0 ) )
        i0 = max( min(i0,M0-2), 0 )
        t0 = u0-i0
        u1 = (x1 - start1)*dinv1
        i1 = int( floor( u1 ) )
        i1 = max( min(i1,M1-2), 0 )
        t1 = u1-i1
        tp0_0 = t0*t0*t0;  tp0_1 = t0*t0;  tp0_2 = t0;  tp0_3 = 1.0;
        tp1_0 = t1*t1*t1;  tp1_1 = t1*t1;  tp1_2 = t1;  tp1_3 = 1.0;
        Phi0_0 = 0
        Phi0_1 = 0
        Phi0_2 = 0
        Phi0_3 = 0
        if t0 < 0:
            Phi0_0 = dAd[0,3]*t0 + Ad[0,3]
            Phi0_1 = dAd[1,3]*t0 + Ad[1,3]
            Phi0_2 = dAd[2,3]*t0 + Ad[2,3]
            Phi0_3 = dAd[3,3]*t0 + Ad[3,3]
        elif t0 > 1:
            Phi0_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t0-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
            Phi0_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t0-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
            Phi0_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t0-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
            Phi0_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t0-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
        else:
            Phi0_0 = (Ad[0,0]*tp0_0 + Ad[0,1]*tp0_1 + Ad[0,2]*tp0_2 + Ad[0,3]*tp0_3)
            Phi0_1 = (Ad[1,0]*tp0_0 + Ad[1,1]*tp0_1 + Ad[1,2]*tp0_2 + Ad[1,3]*tp0_3)
            Phi0_2 = (Ad[2,0]*tp0_0 + Ad[2,1]*tp0_1 + Ad[2,2]*tp0_2 + Ad[2,3]*tp0_3)
            Phi0_3 = (Ad[3,0]*tp0_0 + Ad[3,1]*tp0_1 + Ad[3,2]*tp0_2 + Ad[3,3]*tp0_3)

        Phi1_0 = 0
        Phi1_1 = 0
        Phi1_2 = 0
        Phi1_3 = 0
        if t1 < 0:
            Phi1_0 = dAd[0,3]*t1 + Ad[0,3]
            Phi1_1 = dAd[1,3]*t1 + Ad[1,3]
            Phi1_2 = dAd[2,3]*t1 + Ad[2,3]
            Phi1_3 = dAd[3,3]*t1 + Ad[3,3]
        elif t1 > 1:
            Phi1_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t1-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
            Phi1_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t1-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
            Phi1_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t1-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
            Phi1_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t1-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
        else:
            Phi1_0 = (Ad[0,0]*tp1_0 + Ad[0,1]*tp1_1 + Ad[0,2]*tp1_2 + Ad[0,3]*tp1_3)
            Phi1_1 = (Ad[1,0]*tp1_0 + Ad[1,1]*tp1_1 + Ad[1,2]*tp1_2 + Ad[1,3]*tp1_3)
            Phi1_2 = (Ad[2,0]*tp1_0 + Ad[2,1]*tp1_1 + Ad[2,2]*tp1_2 + Ad[2,3]*tp1_3)
            Phi1_3 = (Ad[3,0]*tp1_0 + Ad[3,1]*tp1_1 + Ad[3,2]*tp1_2 + Ad[3,3]*tp1_3)


        out[n] = Phi0_0*(Phi1_0*(coefs[i0+0,i1+0]) + Phi1_1*(coefs[i0+0,i1+1]) + Phi1_2*(coefs[i0+0,i1+2]) + Phi1_3*(coefs[i0+0,i1+3])) + Phi0_1*(Phi1_0*(coefs[i0+1,i1+0]) + Phi1_1*(coefs[i0+1,i1+1]) + Phi1_2*(coefs[i0+1,i1+2]) + Phi1_3*(coefs[i0+1,i1+3])) + Phi0_2*(Phi1_0*(coefs[i0+2,i1+0]) + Phi1_1*(coefs[i0+2,i1+1]) + Phi1_2*(coefs[i0+2,i1+2]) + Phi1_3*(coefs[i0+2,i1+3])) + Phi0_3*(Phi1_0*(coefs[i0+3,i1+0]) + Phi1_1*(coefs[i0+3,i1+1]) + Phi1_2*(coefs[i0+3,i1+2]) + Phi1_3*(coefs[i0+3,i1+3]))

@njit(cache=True)
def vec_eval_cubic_spline_3(a, b, orders, coefs, points, out):

    d = a.shape[0]
    N = points.shape[0]

    for n in range(N):

        x0 = points[n,0]
        x1 = points[n,1]
        x2 = points[n,2]
        M0 = orders[0]
        start0 = a[0]
        dinv0 = (orders[0]-1.0)/(b[0]-a[0])
        M1 = orders[1]
        start1 = a[1]
        dinv1 = (orders[1]-1.0)/(b[1]-a[1])
        M2 = orders[2]
        start2 = a[2]
        dinv2 = (orders[2]-1.0)/(b[2]-a[2])
        u0 = (x0 - start0)*dinv0
        i0 = int( floor( u0 ) )
        i0 = max( min(i0,M0-2), 0 )
        t0 = u0-i0
        u1 = (x1 - start1)*dinv1
        i1 = int( floor( u1 ) )
        i1 = max( min(i1,M1-2), 0 )
        t1 = u1-i1
        u2 = (x2 - start2)*dinv2
        i2 = int( floor( u2 ) )
        i2 = max( min(i2,M2-2), 0 )
        t2 = u2-i2
        tp0_0 = t0*t0*t0;  tp0_1 = t0*t0;  tp0_2 = t0;  tp0_3 = 1.0;
        tp1_0 = t1*t1*t1;  tp1_1 = t1*t1;  tp1_2 = t1;  tp1_3 = 1.0;
        tp2_0 = t2*t2*t2;  tp2_1 = t2*t2;  tp2_2 = t2;  tp2_3 = 1.0;
        Phi0_0 = 0
        Phi0_1 = 0
        Phi0_2 = 0
        Phi0_3 = 0
        if t0 < 0:
            Phi0_0 = dAd[0,3]*t0 + Ad[0,3]
            Phi0_1 = dAd[1,3]*t0 + Ad[1,3]
            Phi0_2 = dAd[2,3]*t0 + Ad[2,3]
            Phi0_3 = dAd[3,3]*t0 + Ad[3,3]
        elif t0 > 1:
            Phi0_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t0-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
            Phi0_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t0-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
            Phi0_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t0-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
            Phi0_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t0-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
        else:
            Phi0_0 = (Ad[0,0]*tp0_0 + Ad[0,1]*tp0_1 + Ad[0,2]*tp0_2 + Ad[0,3]*tp0_3)
            Phi0_1 = (Ad[1,0]*tp0_0 + Ad[1,1]*tp0_1 + Ad[1,2]*tp0_2 + Ad[1,3]*tp0_3)
            Phi0_2 = (Ad[2,0]*tp0_0 + Ad[2,1]*tp0_1 + Ad[2,2]*tp0_2 + Ad[2,3]*tp0_3)
            Phi0_3 = (Ad[3,0]*tp0_0 + Ad[3,1]*tp0_1 + Ad[3,2]*tp0_2 + Ad[3,3]*tp0_3)

        Phi1_0 = 0
        Phi1_1 = 0
        Phi1_2 = 0
        Phi1_3 = 0
        if t1 < 0:
            Phi1_0 = dAd[0,3]*t1 + Ad[0,3]
            Phi1_1 = dAd[1,3]*t1 + Ad[1,3]
            Phi1_2 = dAd[2,3]*t1 + Ad[2,3]
            Phi1_3 = dAd[3,3]*t1 + Ad[3,3]
        elif t1 > 1:
            Phi1_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t1-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
            Phi1_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t1-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
            Phi1_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t1-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
            Phi1_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t1-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
        else:
            Phi1_0 = (Ad[0,0]*tp1_0 + Ad[0,1]*tp1_1 + Ad[0,2]*tp1_2 + Ad[0,3]*tp1_3)
            Phi1_1 = (Ad[1,0]*tp1_0 + Ad[1,1]*tp1_1 + Ad[1,2]*tp1_2 + Ad[1,3]*tp1_3)
            Phi1_2 = (Ad[2,0]*tp1_0 + Ad[2,1]*tp1_1 + Ad[2,2]*tp1_2 + Ad[2,3]*tp1_3)
            Phi1_3 = (Ad[3,0]*tp1_0 + Ad[3,1]*tp1_1 + Ad[3,2]*tp1_2 + Ad[3,3]*tp1_3)

        Phi2_0 = 0
        Phi2_1 = 0
        Phi2_2 = 0
        Phi2_3 = 0
        if t2 < 0:
            Phi2_0 = dAd[0,3]*t2 + Ad[0,3]
            Phi2_1 = dAd[1,3]*t2 + Ad[1,3]
            Phi2_2 = dAd[2,3]*t2 + Ad[2,3]
            Phi2_3 = dAd[3,3]*t2 + Ad[3,3]
        elif t2 > 1:
            Phi2_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t2-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
            Phi2_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t2-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
            Phi2_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t2-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
            Phi2_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t2-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
        else:
            Phi2_0 = (Ad[0,0]*tp2_0 + Ad[0,1]*tp2_1 + Ad[0,2]*tp2_2 + Ad[0,3]*tp2_3)
            Phi2_1 = (Ad[1,0]*tp2_0 + Ad[1,1]*tp2_1 + Ad[1,2]*tp2_2 + Ad[1,3]*tp2_3)
            Phi2_2 = (Ad[2,0]*tp2_0 + Ad[2,1]*tp2_1 + Ad[2,2]*tp2_2 + Ad[2,3]*tp2_3)
            Phi2_3 = (Ad[3,0]*tp2_0 + Ad[3,1]*tp2_1 + Ad[3,2]*tp2_2 + Ad[3,3]*tp2_3)


        out[n] = Phi0_0*(Phi1_0*(Phi2_0*(coefs[i0+0,i1+0,i2+0]) + Phi2_1*(coefs[i0+0,i1+0,i2+1]) + Phi2_2*(coefs[i0+0,i1+0,i2+2]) + Phi2_3*(coefs[i0+0,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+0,i1+1,i2+0]) + Phi2_1*(coefs[i0+0,i1+1,i2+1]) + Phi2_2*(coefs[i0+0,i1+1,i2+2]) + Phi2_3*(coefs[i0+0,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+0,i1+2,i2+0]) + Phi2_1*(coefs[i0+0,i1+2,i2+1]) + Phi2_2*(coefs[i0+0,i1+2,i2+2]) + Phi2_3*(coefs[i0+0,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+0,i1+3,i2+0]) + Phi2_1*(coefs[i0+0,i1+3,i2+1]) + Phi2_2*(coefs[i0+0,i1+3,i2+2]) + Phi2_3*(coefs[i0+0,i1+3,i2+3]))) + Phi0_1*(Phi1_0*(Phi2_0*(coefs[i0+1,i1+0,i2+0]) + Phi2_1*(coefs[i0+1,i1+0,i2+1]) + Phi2_2*(coefs[i0+1,i1+0,i2+2]) + Phi2_3*(coefs[i0+1,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+1,i1+1,i2+0]) + Phi2_1*(coefs[i0+1,i1+1,i2+1]) + Phi2_2*(coefs[i0+1,i1+1,i2+2]) + Phi2_3*(coefs[i0+1,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+1,i1+2,i2+0]) + Phi2_1*(coefs[i0+1,i1+2,i2+1]) + Phi2_2*(coefs[i0+1,i1+2,i2+2]) + Phi2_3*(coefs[i0+1,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+1,i1+3,i2+0]) + Phi2_1*(coefs[i0+1,i1+3,i2+1]) + Phi2_2*(coefs[i0+1,i1+3,i2+2]) + Phi2_3*(coefs[i0+1,i1+3,i2+3]))) + Phi0_2*(Phi1_0*(Phi2_0*(coefs[i0+2,i1+0,i2+0]) + Phi2_1*(coefs[i0+2,i1+0,i2+1]) + Phi2_2*(coefs[i0+2,i1+0,i2+2]) + Phi2_3*(coefs[i0+2,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+2,i1+1,i2+0]) + Phi2_1*(coefs[i0+2,i1+1,i2+1]) + Phi2_2*(coefs[i0+2,i1+1,i2+2]) + Phi2_3*(coefs[i0+2,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+2,i1+2,i2+0]) + Phi2_1*(coefs[i0+2,i1+2,i2+1]) + Phi2_2*(coefs[i0+2,i1+2,i2+2]) + Phi2_3*(coefs[i0+2,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+2,i1+3,i2+0]) + Phi2_1*(coefs[i0+2,i1+3,i2+1]) + Phi2_2*(coefs[i0+2,i1+3,i2+2]) + Phi2_3*(coefs[i0+2,i1+3,i2+3]))) + Phi0_3*(Phi1_0*(Phi2_0*(coefs[i0+3,i1+0,i2+0]) + Phi2_1*(coefs[i0+3,i1+0,i2+1]) + Phi2_2*(coefs[i0+3,i1+0,i2+2]) + Phi2_3*(coefs[i0+3,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+3,i1+1,i2+0]) + Phi2_1*(coefs[i0+3,i1+1,i2+1]) + Phi2_2*(coefs[i0+3,i1+1,i2+2]) + Phi2_3*(coefs[i0+3,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+3,i1+2,i2+0]) + Phi2_1*(coefs[i0+3,i1+2,i2+1]) + Phi2_2*(coefs[i0+3,i1+2,i2+2]) + Phi2_3*(coefs[i0+3,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+3,i1+3,i2+0]) + Phi2_1*(coefs[i0+3,i1+3,i2+1]) + Phi2_2*(coefs[i0+3,i1+3,i2+2]) + Phi2_3*(coefs[i0+3,i1+3,i2+3])))


# used by njitted routines (frozen)
basis = np.array([1.0 / 6.0, 2.0 / 3.0, 1.0 / 6.0, 0.0])


@njit(cache=True)
def solve_deriv_interp_1d(bands, coefs):

    M = coefs.shape[0] - 2

    # Solve interpolating equations
    # First and last rows are different

    bands[0, 1] /= bands[0, 0]
    bands[0, 2] /= bands[0, 0]
    bands[0, 3] /= bands[0, 0]
    bands[0, 0] = 1.0
    bands[1, 1] -= bands[1, 0] * bands[0, 1]
    bands[1, 2] -= bands[1, 0] * bands[0, 2]
    bands[1, 3] -= bands[1, 0] * bands[0, 3]
    bands[0, 0] = 0.0
    bands[1, 2] /= bands[1, 1]
    bands[1, 3] /= bands[1, 1]
    bands[1, 1] = 1.0

    # Now do rows 2 through M+1
    for row in range(2, M + 1):
        bands[row, 1] -= bands[row, 0] * bands[row - 1, 2]
        bands[row, 3] -= bands[row, 0] * bands[row - 1, 3]
        bands[row, 2] /= bands[row, 1]
        bands[row, 3] /= bands[row, 1]
        bands[row, 0] = 0.0
        bands[row, 1] = 1.0

    # Do last row
    bands[M + 1, 1] -= bands[M + 1, 0] * bands[M - 1, 2]
    bands[M + 1, 3] -= bands[M + 1, 0] * bands[M - 1, 3]
    bands[M + 1, 2] -= bands[M + 1, 1] * bands[M, 2]
    bands[M + 1, 3] -= bands[M + 1, 1] * bands[M, 3]
    bands[M + 1, 3] /= bands[M + 1, 2]
    bands[M + 1, 2] = 1.0
    coefs[M + 1] = bands[(M + 1), 3]
    # Now back substitute up
    for row in range(M, 0, -1):
        coefs[row] = bands[row, 3] - bands[row, 2] * coefs[row + 1]

    # Finish with first row
    coefs[0] = bands[0, 3] - bands[0, 1] * coefs[1] - bands[0, 2] * coefs[2]



@njit(cache=True)
def find_coefs_1d(delta_inv, M, data, coefs):

    bands = np.zeros((M + 2, 4))

    # Setup boundary conditions
    abcd_left = np.zeros(4)
    abcd_right = np.zeros(4)

    # Left boundary
    abcd_left[0] = 1.0 * delta_inv * delta_inv
    abcd_left[1] = -2.0 * delta_inv * delta_inv
    abcd_left[2] = 1.0 * delta_inv * delta_inv
    abcd_left[3] = 0

    # Right boundary
    abcd_right[0] = 1.0 * delta_inv * delta_inv
    abcd_right[1] = -2.0 * delta_inv * delta_inv
    abcd_right[2] = 1.0 * delta_inv * delta_inv
    abcd_right[3] = 0

    for i in range(4):
        bands[0, i] = abcd_left[i]
        bands[M + 1, i] = abcd_right[i]

    for i in range(M):
        for j in range(3):
            bands[i + 1, j] = basis[j]
            bands[i + 1, 3] = data[i]

    solve_deriv_interp_1d(bands, coefs)


@njit(cache=True)
def filter_coeffs_1d(dinv, data):
    M = data.shape[0]
    N = M + 2

    coefs = np.zeros(N)
    find_coefs_1d(dinv[0], M, data, coefs)

    return coefs


@njit(cache=True)
def filter_coeffs_2d(dinv, data):

    Mx = data.shape[0]
    My = data.shape[1]

    Nx = Mx + 2
    Ny = My + 2

    coefs = np.zeros((Nx, Ny))

    # First, solve in the X-direction
    for iy in range(My):
        # print(data[:,iy].size)
        # print(spline.coefs[:,iy].size)
        find_coefs_1d(dinv[0], Mx, data[:, iy], coefs[:, iy])

    # Now, solve in the Y-direction
    for ix in range(Nx):
        find_coefs_1d(dinv[1], My, coefs[ix,:], coefs[ix,:])

    return coefs


@njit(cache=True)
def filter_coeffs_3d(dinv, data):

    Mx = data.shape[0]
    My = data.shape[1]
    Mz = data.shape[2]

    Nx = Mx + 2
    Ny = My + 2
    Nz = Mz + 2

    coefs = np.zeros((Nx, Ny, Nz))

    for iy in range(My):
        for iz in range(Mz):
            find_coefs_1d(dinv[0], Mx, data[:, iy, iz], coefs[:, iy, iz])

    # Now, solve in the Y-direction
    for ix in range(Nx):
        for iz in range(Mz):
            find_coefs_1d(dinv[1], My, coefs[ix,:, iz], coefs[ix,:, iz])

    # Now, solve in the Z-direction
    for ix in range(Nx):
        for iy in range(Ny):
            find_coefs_1d(dinv[2], Mz, coefs[ix, iy,:], coefs[ix, iy,:])

    return coefs


def filter_coeffs(smin, smax, orders, data):
    global Ad
    Ad = array([
    #      t^3       t^2        t        1
       [-1.0/6.0,  3.0/6.0, -3.0/6.0, 1.0/6.0],
       [ 3.0/6.0, -6.0/6.0,  0.0/6.0, 4.0/6.0],
       [-3.0/6.0,  3.0/6.0,  3.0/6.0, 1.0/6.0],
       [ 1.0/6.0,  0.0/6.0,  0.0/6.0, 0.0/6.0]
    ])
    
    global dAd
    dAd = zeros((4,4))
    for i in range(1,4):
        Ad_i = Ad[:, i-1]
        dAd[:,i] = (4-i) * Ad_i
    
    global d2Ad
    d2Ad = zeros((4,4))
    for i in range(1,4):
        dAd_i = dAd[:, i-1]
        d2Ad[:,i] = (4-i) * dAd_i

    smin = np.array(smin, dtype=float)
    smax = np.array(smax, dtype=float)
    dinv = (smax - smin) / orders
    data = data.reshape(orders)
    return filter_data(dinv, data)


def filter_data(dinv, data):
    if len(dinv) == 1:
        return filter_coeffs_1d(dinv, data)
    elif len(dinv) == 2:
        return filter_coeffs_2d(dinv, data)
    elif len(dinv) == 3:
        return filter_coeffs_3d(dinv, data)

