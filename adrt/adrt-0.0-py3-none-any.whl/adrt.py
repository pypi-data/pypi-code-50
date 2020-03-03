import numpy as np

def density(n):
    nn = 2*n
    nnn = 3*n
    rn = np.float64(n)
    rnn = np.float64(2*n)

    da = np.zeros((3*n, n))
    for i in range(nnn):
        for j in range(n):
            val = 0.0
            if ((i+1 <= n) and (j+1 >= n-i)):
                val = 0.25
            elif ((i+1 <= n) and (j+1 < n-i)):
                val = 0.0
            elif ((i+1 >= n+1) and (i+1 <= nn) and (j+1 >= nn-i)):
                x = j+1
                val = (j+1) / rn
            elif ((i+1 >= n+1) and (i+1 <= nn) and (j+1 < nn-i)):
                val = 1.0
            elif (i+1 >= nn+1):
                val = 0.0

            da[i,j] = val
    return da

def drt(a):
    n = a.shape[0]
    nn, nnn = 2*n, 3*n

    da = np.zeros((nnn, a.shape[1]))
    dat = np.zeros((nnn,n))
    for i in range(0, nnn):
        for j in range(0, n):
            if ((i >= n) and (i+1 <= nn)):
                dat[i, j] = a[i-n, j]

    m = 2
    mh = 1
    while m <= n:
        for s in range(0, mh):
            for i in range(0, n, m):
                for h in range(0, nnn):
                    if (h+1 <= nnn-s):
                        da[h, i+2*s] = dat[h,i+s] + dat[h+s,i+mh+s]
                    if (h+1 <= nnn-s-1):
                        da[h, i+1+2*s] = dat[h,i+s] + dat[h+1+s,i+mh+s]

        dat = np.copy(da)
        m = 2*m
        mh = 2*mh
    return da

def pdrt(a,pl):
    a_sz1, a_sz2 = a.shape

    n = a_sz1
    nn = 2*n
    nnn = 3*n

    pn = pl*a_sz2
    pnn = 2*pl*n
    pnnn = 3*pl*n

    dat = np.zeros((pnnn, pn))
    for i in range(pnnn):
        for j in range(pn):
            if ((i+1 >= pn+1) and (i+1 <= pnn)):
                dat[i,j] = a[(i+1 - pn - 1)/pl, (j+1-1)/pl]

    da = np.zeros((3 * pl * a_sz1, pl * a_sz2))

    m = 2
    mh = m/2
    while (m <= pn):
        for s in range(mh):
            for i in range(0, pn, m):
                for h in range(pnnn):
                    if (h+1 <= pnnn-s):
                        da[h, i+1+2*s-1] = dat[h,i+s] + dat[h+s,i+mh+s]
                    if (h+1 <= pnnn-s-1):
                        da[h, i+2*s+1] = dat[h,i+s] + dat[h+s+1,i+mh+s]
        dat = np.copy(da)
        m = 2*m
        mh = 2*mh

    return da

def pdrtq(a,p,q,da):
    return None

def bdrtq(da,q,ba):
    return None

def bdrt(da):
    n = da.shape[1]
    nn, nnn = 2*n, 3*n

    bat = np.zeros((nnn,n))
    batwork = np.zeros((nnn,n))

    bat = np.copy(da)

    m = n
    while m >= 2:
        mh = m/2
        for h in range(0, nnn):
            for s in range(0, mh):
                for i in range(0, n, m):
                    batwork[h, i+s] = bat[h,i+2*s] + bat[h,i+2*s+1]
                    if ((h+1 >= 2) and (h+1+s <= nnn)):
                       batwork[h+s, i+s+mh] = bat[h,i+2*s] + bat[h-1,i+2*s+1]
                    elif (h == 0):
                       batwork[h+s, i+s+mh] = bat[h,i+2*s]
        bat = np.copy(batwork)
        m = m / 2

    ba = bat[n:nn,:]
    return ba

def drtaq(a,daa,dab,dac,dad):
    return None

def bdrtaq(daa,dab,dac,dad,ba):
    return None

def pdrtaq(a,pl,daa,dab,dac,dad):
    return None

def pdrtqaq(a,p,q,daa,dab,dac,dad):
    return None

def rbdrtaq(daa,dab,dac,dad,pl,rba):
    return None

def rbdrtqaq(daa,dab,dac,dad,pl,ql,rba):
    return None

def pmatmul(x,pl,ax):
    return None

def pmatmulq(x,pl,ql,ax):
    return None