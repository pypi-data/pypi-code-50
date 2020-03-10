import setuptools
# from importlib_metadata import entry_points

setuptools.setup(
    name="coursetemplater",
    packages=setuptools.find_packages(),
    version="0.1",
    licence="MIT",
    description="Creates a directory layout for a subject/course file",
    author="CoolDudde4150",
    url="https://github.com/CoolDudde4150/coursetemplater",
    download_url="https://github.com/CoolDudde4150/coursetemplater/archive/v0.1.tar.gz",
    install_requires=[
        "mdtemplater"
    ],
    entry_points={
        "console_scripts": [
            "coursetemplater = coursetemplater.coursetemplate:main"
        ]
    }
)
