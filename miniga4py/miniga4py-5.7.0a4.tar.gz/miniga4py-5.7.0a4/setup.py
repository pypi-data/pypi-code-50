"""
miniga4py Minimal Python bindings for the Global Arrays Toolkit library
=======================================================================

- miniga4py
    Minimal Python bindings for the Global Arrays Toolkit library

"""

import os
import sys
from distutils.spawn import find_executable
from distutils.sysconfig import get_config_vars
from subprocess import check_output
from setuptools import setup, Extension

PKGNAME = "miniga4py"
SUBVERSION = '0a4'
REQFILE = "requirements.txt"
EXECUTABLES = ["testminiga4py", ]
SCRIPTS = ['bin/%s' % sc for sc in EXECUTABLES]
__version__ = "5.7.%s" % SUBVERSION

if 'bdist_wheel' in sys.argv:
    sys.stderr.write("%s: this package cannot be built as a wheel\n" %
            PKGNAME)
    sys.exit(1)

# Check if all needed packages are already installed
missing = []
try:
    import globalarrays
except RuntimeError:
    pass
except ImportError:
    missing.append("globalarrays")
try:
    import numpy
except ImportError:
    missing.append("numpy")
try:
    import mpi4py
except ImportError:
    missing.append("mpi4py")

if missing:
    print("\n\nERROR!\n    %s must be already"
            " installed\n" % " ".join(missing))
    raise SystemExit("\n\n Please run\n"
            "    pip3 install %s\n and then run again this command.\n"
            % " ".join(missing))
else:
    from Cython.Build import cythonize

# Avoid name clash for scripts
ok = True
conflicting = []
for ex in EXECUTABLES:
    executable = find_executable(ex)
    if executable:
        ok = False
        with open(executable) as the_file:
            try:
                for line in open(executable):
                    if ("This script belongs to Python package %s"
                            % PKGNAME in line):
                        # This executable belong to this package
                        ok = True
                        break
            except UnicodeDecodeError:
                pass
        if not ok:
            conflicting.append(executable)
if not ok:
    raise SystemExit("\nWARNING!\n"
            "Installation is incompatible with the following files:\n"
            " --> %s\nPlease resolve conflict before retrying.\n"
            "*** Installation aborted ***" % conflicting)

#------------------------------------------------------------------------------
# Check for VIRTUAL_ENV
if 'VIRTUAL_ENV' in os.environ:
    ga_bin_path = os.path.join(os.environ.get('VIRTUAL_ENV'),
                       'lib',
                       'python%d.%d' % sys.version_info[:2],
                       'site-packages', 'globalarrays', 'bin')
else:
    ga_bin_path = None

#------------------------------------------------------------------------------
GA_CONFIG = find_executable("ga-config", ga_bin_path)
ga_cc = check_output([GA_CONFIG, "-cc"]).decode().strip()
ga_cppflags = check_output([GA_CONFIG, "--cppflags"]).decode().strip()
ga_ldflags = check_output([GA_CONFIG, "--ldflags"]).decode().strip()
ga_clibs = check_output([GA_CONFIG, "--libs"]).decode().strip()
if 'CC' not in os.environ:
    os.environ['CC'] = ga_cc
if 'LDSHARED' not in os.environ:
    # take a lucky guess and reuse the same flags Python used
    flags = get_config_vars('LDSHARED')[0].strip().split()
    assert flags
    flags[0] = ga_cc
    os.environ['LDSHARED'] = ' '.join(flags)
if 'ARCHFLAGS' not in os.environ:
    os.environ['ARCHFLAGS'] = ''

# On osx, '-framework Accelerate' doesn't link the actual LAPACK and BLAS
# libraries. Locate them manually if GA was configured to use them.
linalg_include = []
linalg_library = []
linalg_lib = []
if 'Accelerate' in ga_clibs or 'vecLib' in ga_clibs:
    path = ("/System/Library/Frameworks/Accelerate.framework/Frameworks"
            "/vecLib.framework/Versions/A")
    linalg_include = []
    if os.path.exists(path):
        linalg_library = [path]
        linalg_lib = ["LAPACK", "BLAS"]
    # remove '-framework Accelerate' from flags
    ga_clibs = ga_clibs.replace("-framework", "")
    ga_clibs = ga_clibs.replace("Accelerate", "")
    ga_clibs = ga_clibs.replace("vecLib", "")

include_dirs = [numpy.get_include(), mpi4py.get_include()]
library_dirs = []
libraries = []

# add the GA stuff
for part in ga_cppflags.split():
    part = part.strip()
    include_dirs.append(part.replace("-I", ""))
for part in ga_ldflags.split():
    part = part.strip()
    library_dirs.append(part.replace("-L", ""))
for part in ga_clibs.split():
    part = part.strip()
    if '-L' in part:
        library_dirs.append(part.replace("-L", ""))
    elif '-l' in part:
        libraries.append(part.replace("-l", ""))

include_dirs.extend(linalg_include)
library_dirs.extend(linalg_library)
libraries.extend(linalg_lib)

include_dirs.append(".")

extensions = [
    Extension(
        name="miniga4py.ga",
        sources=["miniga4py/ga.pyx"],
        include_dirs=include_dirs,
        library_dirs=library_dirs,
        libraries=libraries
        ),
    ]
ext_modules = cythonize(extensions, include_path=include_dirs)

#==============================================================================
description = __doc__.split('\n')[1:-1][0]
classifiers = """
Development Status :: 3 - Alpha
Intended Audience :: Developers
Intended Audience :: Science/Research
License :: OSI Approved :: BSD License
Operating System :: POSIX
Programming Language :: C
Programming Language :: C++
Programming Language :: Fortran
Programming Language :: Python
Topic :: Scientific/Engineering
Topic :: Software Development :: Libraries
"""

with open(REQFILE) as fp:
    requirements = fp.read()

setup(name=PKGNAME,
        version=__version__,
        install_requires=requirements,
        description=description,
        long_description=open("README.md", "r").read(),
        long_description_content_type='text/markdown',
        classifiers=classifiers.split('\n')[1:-1],
        keywords=[PKGNAME, 'MPI', 'GlobalArrays'],
        platforms=['POSIX'],
        license='BSD',
        scripts=SCRIPTS,
        include_package_data=True,
        url='https://github.com/GlobalArrays/ga4py',
        download_url='https://github.com/GlobalArrays/ga4py/tree/feature/py3',
        author='Roberto Vidmar',
        author_email='rvidmar@inogs.it',
        maintainer='Roberto Vidmar',
        maintainer_email='rvidmar@inogs.it',
        packages=[PKGNAME],
        ext_modules=ext_modules,
        )
