#!/usr/bin/env python
"""
Author:Noboru Yamamoto, KEK, Japan (c) 2009-2013

contact info: http://gofer.kek.jp/
or https://plus.google.com/i/xW1BWwWsj3s:2rbmfOGOM4c

Thanks to:
   Dr. Shuei Yamada(KEK, Japan) for improved vxi11scan.py

Revision Info:
$Author: noboru $
$Date: 2020/02/28 00:48:54 $ (UTC)
$HGdate: Fri, 28 Feb 2020 09:48:54 +0900 $
$Header: /Users/noboru/src/python/VXI11/PyVXI11-Current/setup.py,v 9191f6782927 2020/02/28 00:48:54 noboru $
$Id: setup.py,v 9191f6782927 2020/02/28 00:48:54 noboru $
$RCSfile: setup.py,v $
$Revision: 9191f6782927 $
$Source: /Users/noboru/src/python/VXI11/PyVXI11-Current/setup.py,v $
2020/02/27 : add io_timeout parameters in write.
2020/02/27 : new tag. 1.15
"""
import os,platform,re,sys,os.path

from Cython.Distutils.extension import Extension
from Cython.Distutils import build_ext
from Cython.Build import cythonize

# python2/python3
extra=dict()

# if sys.version_info >= (3,):
#     extra['use_2to3'] = True
    
try:
   from distutils.command.build_py import build_py_2to3 as build_py #for Python3
except ImportError:
   from distutils.command.build_py import build_py     # for Python2

from distutils.core import setup
#from distutils.extension import Extension

# macros managedd by mercurial keyword extension
#
HGTag="$HGTag: 1.15.13-9191f6782927 $"
HGdate="$HGdate: Fri, 28 Feb 2020 09:48:54 +0900 $" #(rfc822date)
#HGTagShort="$HGTagShort: 1.15.13 $"
from hgstamp import HGTagShort
HGlastlog="$lastlog: confirmed SRQ-SVC is working $"
HGcheckedin="$checked in by: Noboru Yamamoto <noboru.yamamoto@kek.jp> $"
#

#release = os.popen("hg log -r tip --template '{latesttag}.{latesttagdistance}-{node|short}'").read()
release=HGTag
rev=HGTag[HGTag.index(":")+1:HGTag.index("-")].strip()
#

sysname=platform.system()

if re.match("Darwin.*",sysname):
    RPCLIB=["rpcsvc"]
elif re.match("CYGWIN.*",sysname):
    RPCLIB=["rpc"]
else:
    RPCLIB=None

try:
    os.stat("./VXI11.h")
    os.stat("./VXI11_svc.c")
    os.stat("./VXI11_clnt.c")
    os.stat("./VXI11_xdr.c")
except OSError:
    os.system("rpcgen -C -h VXI11.rpcl -o VXI11.h")
    os.system("rpcgen -C -m -L VXI11.rpcl -o VXI11_svc.c")
    os.system("rpcgen -C -l VXI11.rpcl -o VXI11_clnt.c")
    os.system("rpcgen -C -c VXI11.rpcl -o VXI11_xdr.c")
    # use of "-N" option should be considered 2013.11.5 NY

ext_modules=[]

# cVXI11-2.pyx and cVXI11-3.pyx are hard links to cVXI11.pyx
cVXI11_source_PY2="cVXI11_2.pyx"
cVXI11_source_PY3="cVXI11_3.pyx"

if sys.version_info >= (3,):
   PY3=True
   cVXI11_source=cVXI11_source_PY3
else:
   PY3=False
   cVXI11_source=cVXI11_source_PY2
    
if not os.path.exists(cVXI11_source):
   os.link("cVXI11.pyx", cVXI11_source)
elif not os.path.samefile("cVXI11.pyx", cVXI11_source):
   os.remove(cVXI11_source)
   os.link("cVXI11.pyx", cVXI11_source)
   
ext_modules.append(Extension("cVXI11", 
                             [ cVXI11_source, # Cython source. i.e. .pyx
                               "VXI11_clnt.c", "VXI11_xdr.c", #"VXI11_svc.c", 
                               "createAbtChannel.c",
                               "cPMAP.cpp",
                             ]
                             ,libraries=RPCLIB
                             ,depends=["cVXI11.pxd"] # Cython interface file
                             ,language="c++"
                             ,cython_cplus=True
                             ,undef_macros=["CFLAGS"]
                             ,extra_compile_args=["-I/usr/include/tirpc"],
))


## if you  like to compare cython version with swig-version, uncomment the 
## following lines. You must have swig in your path.
# ext_modules.append(Extension("_VXI11",["VXI11.i","VXI11_clnt.c","VXI11_xdr.c"]
#                     ,swig_opts=["-O","-nortti"]
#                     ,libraries=RPCLIB
#                     ))

ext_modules=cythonize(
   ext_modules,
   compiler_directives={"language_level":"3" if PY3 else "2"},
)

setup(name="PyVXI11",
      version=rev,
      author="Noboru Yamamoto, KEK, JAPAN",
      author_email = "Noboru.YAMAMOTO@kek.jp",
      description='A Cython based Python module to control devices over VXI11 protocol.',
      url="http://www-cont.j-parc.jp/",
      classifiers=['Programming Language :: Python',
                   'Programming Language :: Cython',
                   'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
                   ],
      ext_modules=ext_modules,
      cmdclass = {'build_ext': build_ext,
                  # 'build_py':build_py  # for 2to3 
      },
      py_modules=[
          "RebootLanGbib","AgilentDSO",
          "TekOSC","TekDPO","LeCroy",
          "vxi11Exceptions","cVXI11_revision","hgstamp",
          #"vxi11scan","VXI11","vxi11Device",
      ],
      **extra
)
