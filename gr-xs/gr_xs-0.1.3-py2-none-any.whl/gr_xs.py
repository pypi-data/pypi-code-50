from collections import namedtuple
from functools import partial
import numpy as np
from scipy.integrate import quad


MW = 80.379
MELEC = 0.511e-3
ER = MW**2/(2*MELEC)
GAMMAW = 2.085
GAMMA0 = 2*ER*GAMMAW/MW
ALPHA = 1/137.035999
A0 = 1/(MELEC*ALPHA)


Wavefunctions = namedtuple('Wavefunctions',
                           'f1s f2s f2p f3s f3p f4s f3d')
Orbitals = namedtuple('Orbitals',
                      'ne_1s ne_2s ne_2p ne_3s ne_3p ne_4s ne_3d')
Elements = namedtuple('Elements', 'H O Mg Si Ca Fe')
Element = namedtuple('Element', 'orbitals wavefunctions')


def build_orbitals(Z):
    ordering = Orbitals._fields
    max_e = {'s':2, 'p':6, 'd':10}
    
    stable_orbitals = [0]*len(ordering)
    curr = 0
    while Z:
        stable_orbitals[curr] = min(max_e[ordering[curr][-1]], Z)
        Z -= stable_orbitals[curr]
        curr += 1

    return Orbitals(*stable_orbitals)
            

def build_wfs(*args):
    lm2k2 = lambda k, mu: np.log(mu**2+k**2)
    f1s = lambda k, mu: 32/np.pi*np.exp(
        5*np.log(mu)+2*np.log(k)-4*lm2k2(k,mu))
    f2s = lambda k, mu: 32/(3*np.pi)*(3*mu**2*k-k**3)**2*np.exp(
        5*np.log(mu)-6*lm2k2(k,mu))
    f2p = lambda k, mu: 512/(3*np.pi)*np.exp(
        7*np.log(mu)+4*np.log(k)-6*lm2k2(k,mu))
    f3s = lambda k, mu: 1024/(5*np.pi)*(mu**3*k-mu*k**3)**2*np.exp(
        7*np.log(mu)-8*lm2k2(k,mu))
    f3p = lambda k, mu: 1024/(45*np.pi)*(5*mu**2*k**2-k**4)**2*np.exp(
        7*np.log(mu)-8*lm2k2(k,mu))
    f3d = lambda k, mu: 4096/(5*np.pi)*np.exp(
        9*np.log(mu)+6*np.log(k)-8*lm2k2(k,mu))
    f4s = lambda k, mu: 512/(35*np.pi)*(5*mu**4*k-10*mu**2*k**3+k**5)**2*np.exp(
        9*np.log(mu)-10*lm2k2(k,mu))

    dists = [f1s, f2s, f2p, f3s, f3p, f4s, f3d]
    return Wavefunctions(*[partial(f, mu=xi/A0) if xi>0 else lambda k: k*0 for f, xi in zip(dists,args)])


ELEMENTS = Elements(
    Element(build_orbitals(1), build_wfs(1, 0, 0, 0, 0, 0, 0)),
    Element(build_orbitals(8), build_wfs(7.66, 2.25, 2.23, 0, 0, 0, 0)),
    Element(build_orbitals(12), build_wfs(11.6, 3.7, 3.0, 1.1, 0, 0, 0)),
    Element(build_orbitals(14), build_wfs(13.6, 4.5, 5.0, 1.6, 1.4, 0, 0)),
    Element(build_orbitals(20), build_wfs(19.5, 6.9, 8.0, 3.2, 2.9, 1.1, 0)),
    Element(build_orbitals(26), build_wfs(25.4, 9.3, 11.0, 4.6, 4.3, 1.4, 3.7)))


def sigma_erest(enu):
    """ At-rest electron. Eq. (3)
    enu in GeV
    """
    _ = GAMMA0**2/4
    return _/((enu-ER)**2+_)


@np.vectorize
def sigma_edopp(enu, element='O'):
    """ Bound electron
    """
    elem = ELEMENTS.__getattribute__(element)
    Z = sum(elem.orbitals)
    F = lambda beta: np.sum([MELEC*ne*fk(beta*MELEC) for ne, fk in zip(elem.orbitals, elem.wavefunctions)])/Z
    integrand = lambda beta: F(beta)/beta*(
        np.arctan(2/GAMMA0*(enu*(1+beta)-ER))-np.arctan(2/GAMMA0*(enu*(1-beta)-ER)))
    return GAMMA0/(4*enu)*quad(integrand, 0, 1)[0]


if __name__=='__main__':
    for e, n in zip(ELEMENTS, ELEMENTS._fields):
        print(n, sigma_edopp(ER, n))
        for fk, orbital_name in zip(e.wavefunctions, e.wavefunctions._fields):
            print('...', orbital_name, quad(fk, 0, MELEC))
