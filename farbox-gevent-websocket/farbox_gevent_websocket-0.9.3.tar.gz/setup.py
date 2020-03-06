from setuptools import setup, find_packages


version = __import__('geventwebsocket').get_version()

setup(
    name="farbox_gevent_websocket",
    version=version,
    url="https://bitbucket.org/Jeffrey/gevent-websocket",
    author="Jeffrey Gelens",
    author_email="jeffrey@noppo.pro",
    description=("A FarBox flavored Websocket simple frame for gevent pywsgi server (by Jeffrey's gevent-websocket)"),
    #long_description=open("README.rst").read(),
    download_url="https://bitbucket.org/Jeffrey/gevent-websocket",
    packages=find_packages(exclude=["examples", "tests"]),
    license=open('LICENSE').read(),
    zip_safe=False,
    install_requires=("gevent"),
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
