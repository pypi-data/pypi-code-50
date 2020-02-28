import setuptools


class NumpyExtension(setuptools.Extension):
    def __init__(self, *args, **kwargs):
        self.__include_dirs = []
        super().__init__(*args, **kwargs)

    @property
    def include_dirs(self):
        import numpy

        return self.__include_dirs + [numpy.get_include()]

    @include_dirs.setter
    def include_dirs(self, dirs):
        self.__include_dirs = dirs


setuptools.setup(
    name="sqlite_numpy",
    use_scm_version=True,
    description="Fast SQLite to numpy array loader",
    author="Sébastien Grignard",
    author_email="pub@amakaze.org",
    url="https://gitlab.com/sgrignard/sqlite_numpy",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.7",
    ext_modules=[
        NumpyExtension(
            "sqlite_numpy.core",
            sources=["core.c", "interface.pyx", "interface.pxd"],
            libraries=["sqlite3"],
        )
    ],
    setup_requires=["cython", "numpy", "setuptools_scm"],
    tests_require=["pytest"],
    install_requires=["numpy"],
)
