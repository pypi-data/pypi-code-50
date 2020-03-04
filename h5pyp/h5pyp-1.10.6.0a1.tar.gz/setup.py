"""
HDF5 Parallel Library and h5py Python bindings
==============================================

- h5pyp
    Python bindings for the Parallel HDF5 library

"""

import os
import sys
from distutils.spawn import find_executable
from distutils.dir_util import mkpath
from distutils import log
from setuptools.command.install import install as Install
from setuptools import setup

PKGNAME = "h5pyp"
SUBVERSION = '0a1'
REQFILE = "requirements.txt"
CONFIGURE_OPTIONS = "--enable-parallel --enable-shared".split()
EXECUTABLES = ["test_hdf5_parallel", "h5pyp_dump"]
SCRIPTS = ['bin/%s' % sc for sc in EXECUTABLES]
__INIT__ = """
# Author:  Roberto Vidmar
# Contact: rvidmar@inogs.it

raise RuntimeError("Module cannot be imported, it provides only the"
        " HDF5 parallel library")
"""

#------------------------------------------------------------------------------
def hdf5lib():
    return [f for f in os.listdir('.') if f.startswith("hdf5-")][0]

#------------------------------------------------------------------------------
def version():
    return "%s.%s" % (hdf5lib().lstrip("hdf5-"), SUBVERSION)

#------------------------------------------------------------------------------
def bootstrap():
    # Generate package __init__.py file
    pkgdir = os.path.join('config', 'pypi')
    if not os.path.exists(pkgdir):
        mkpath(pkgdir)
    pkgfile = os.path.join(pkgdir, '__init__.py')
    fh = open(pkgfile, 'w')
    fh.write(__INIT__)
    fh.close()

#------------------------------------------------------------------------------
def execute(command):
    """ Execute system command and exit on error
    """
    status = os.system(command)
    if status != 0:
        raise RuntimeError(status)

#------------------------------------------------------------------------------
def configure(prefix, dry_run=False):
    log.info('Configuring %s for %s...' % (PKGNAME, prefix))
    sys.stderr.write("prefix=%s\n" % prefix)
    options = ["--prefix=%s" % prefix]
    options.extend(CONFIGURE_OPTIONS)

    log.info('configure options:')
    for opt in options:
        log.info(' ' * 4 + opt)
    # Run ga configure
    if dry_run:
        return

    # Swtich to package source dir
    os.chdir(hdf5lib())

    command = ['./configure'] + options
    execute(" ".join(command))
    log.debug("\n\n%s configured.\n" % PKGNAME)

#------------------------------------------------------------------------------
def build(dry_run=False):
    log.info('Building %s...' % PKGNAME)
    if dry_run:
        return

    make = find_executable('make')
    execute(make)
    log.debug("\n\n%s built.\n" % PKGNAME)

#------------------------------------------------------------------------------
def install(dry_run=False):
    log.info('Installing %s...' % PKGNAME)
    if dry_run:
        return

    make = find_executable('make')
    execute("%s install" % make)
    log.debug("\n\n%s installed.\n" % PKGNAME)

#------------------------------------------------------------------------------
#==============================================================================
class Context:
    def __init__(self):
        # Save arguments
        self.sys_argv = sys.argv[:]
        # And current direcory
        self.cwd = os.getcwd()

    def enter(self):
        del sys.argv[1:]
        return self

    def exit(self):
        # Restore arguments
        sys.argv[:] = self.sys_argv
        # And directory
        os.chdir(self.cwd)

#==============================================================================
class CustomInstall(Install):
    """Custom handler for the 'install' command
    """
    def initialize_options(self):
        super().initialize_options()
        self.optimize = 1

    def finalize_options(self):
        super().finalize_options()
        self.install_lib = self.install_platlib
        self.install_libbase = self.install_lib

    def run(self):
        # self.install_lib is .../venv/lib/python3.6/site-packages/
        root_dir = os.path.abspath(self.install_lib)
        prefix = os.path.join(root_dir, PKGNAME)
        ctx = Context().enter()
        try:
            configure(prefix, self.dry_run)
            build(self.dry_run)
            install(self.dry_run)
        finally:
            ctx.exit()

        self.outputs = []
        # These are the installed files
        for dirpath, _, filenames in os.walk(prefix):
            for fn in filenames:
                self.outputs.append(os.path.join(dirpath, fn))
        super().run()
        os.environ['CC'] = "mpicc"
        #WARNING! --install-option does not work with setuptools 39.0.1
        execute('pip3 install'
            ' --install-option="configure"'
            ' --install-option="--mpi"'
            ' --install-option="--hdf5=%s"'
            ' h5py' % prefix)

    def get_outputs(self):
        outputs = getattr(self, 'outputs', [])
        outputs += super().get_outputs()
        return outputs

#==============================================================================
# Check for already installed h5py
if 'egg_info' in sys.argv and '--egg-base' in sys.argv:
    # pip3 install yelds
    #sys.argv=['-c', 'egg_info', '--egg-base', 'pip-egg-info']
    try:
        import h5py
    except ImportError:
        pass
    else:
        print("setup.py invoked with sys.argv=%s" % sys.argv)
        raise OSError("h5py already installed!\n\n"
                " Aborting..... Please uninstall h5py first.")

if 'bdist_wheel' in sys.argv:
    sys.stderr.write("%s: this package cannot be built as a wheel\n"
            % PKGNAME)
    sys.exit(1)

# Avoid name clash for scripts
ok = True
conflicting = []
for ex in EXECUTABLES:
    executable = find_executable(ex)
    if executable:
        ok = False
        with open(executable) as the_file:
            try:
                for line in the_file:
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

bootstrap()

with open(REQFILE) as fp:
    requirements = fp.read()

setup(name=PKGNAME,
        version=version(),
        install_requires=requirements,
        description=description,
        long_description=open("README.md", "r").read(),
        long_description_content_type='text/markdown',
        classifiers=classifiers.split('\n')[1:-1],
        keywords=['HDF5', 'MPI'],
        platforms=['POSIX'],
        #license=open("LICENSE.txt", "r").read(),
        license='BSD',
        scripts=SCRIPTS,
        include_package_data=True,
        url='https://www.hdfgroup.org/',
        download_url='https://www.hdfgroup.org/downloads/',

        author='The HDF Group',
        author_email='help@hdfgroup.org',
        maintainer='Roberto Vidmar',
        maintainer_email='rvidmar@inogs.it',

        packages=[PKGNAME],
        package_dir={PKGNAME: 'config/pypi'},
        cmdclass={'install': CustomInstall},
        )
