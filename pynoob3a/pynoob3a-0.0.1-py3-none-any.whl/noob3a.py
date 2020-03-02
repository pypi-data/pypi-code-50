#!/usr/bin/env python
'''
Usage:
  ./noob3a.py [options]

Options:
  --help -h               This help.
  --mktest-data=D -D D    Output test-data.
'''
import numpy as np;
from struct import pack,unpack;
import os;

__dt = 'float32'
def _pint(i): return pack("i",i);
def _upint(f): return unpack("i",f.read(4))[0];
def output_centered(fname, X,Y,Z,D,order=None):
    psh = (len(Z), len(Y), len(X));
    if order != 'flip':
        psh = (len(X), len(Y), len(Z));
    if D.shape != psh:
        raise ValueError("invalid shape of D ({} vs ({})".format(D.shape,psh));
    D = D.astype(__dt);
    X = np.array(X).astype(__dt);
    Y = np.array(Y).astype(__dt);
    Z = np.array(Z).astype(__dt);
    with open(fname, "wb") as f:
        f.write(_pint(len(X)));
        f.write(memoryview(X));
        f.write(_pint(len(Y)));
        f.write(memoryview(Y));
        f.write(_pint(len(Z)));
        f.write(memoryview(Z));
        L = D.shape[0]*D.shape[1]*D.shape[2];
        f.write(_pint(L));
        f.write(memoryview(D));

def load_centered(fname,order=None):
    with open(fname, "rb") as f:
        xl = _upint(f);
        x  = np.fromfile(f,dtype=__dt,count=xl);
        yl = _upint(f);
        y  = np.fromfile(f,dtype=__dt,count=yl);
        zl = _upint(f);
        z  = np.fromfile(f,dtype=__dt,count=zl);
        Dl = _upint(f);
        if Dl != xl*yl*zl:
            raise ValueError("invalid file ({} = {}*{}*{})".format(Dl,zl,yl,xl));
        D = np.fromfile(f,dtype=__dt, count=Dl);
        if order == 'flip':
            D = D.reshape(zl,yl,xl);
        else:
            D = D.reshape(zl,yl,xl);
    return x,y,z,D;

def mktestdata():
    x=np.array([-1.0,0.0,1.0]).astype(__dt);
    y=np.array([ 0.5,0.5,1.5]).astype(__dt);
    z=np.array([ 0.0,0.5,2.5]).astype(__dt);
    Z,Y,X = np.meshgrid(z,y,z,indexing='ij');
    D = np.sqrt(X**2+Y**2 + Z);
    return x,y,z,D;
        

def test1(fnametest):
    x,y,z,D = mktestdata();
    output_centered(fnametest, x,y,z,D);
    xp,yp,zp,Dp = load_centered(fnametest);
    out = np.max(Dp != D );
    out|= np.max(x  != xp);
    out|= np.max(y  != yp);
    out|= np.max(z  != zp);
    if out:
        raise ValueError("test failed");
    os.remove(fnametest);
    print("test passed");



if __name__ == "__main__":
    from docopt import docopt;
    opts = docopt(__doc__,help=True);
    test1("tmp.dat");
    if opts['--mktest-data']:
        x,y,z,D=mktestdata();
        output_centered(opts['--mktest-data'],x,y,z,D);
    pass;
