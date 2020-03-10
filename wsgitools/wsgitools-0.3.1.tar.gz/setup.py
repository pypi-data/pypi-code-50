#!/usr/bin/env python

from distutils.core import setup

setup(name="wsgitools",
      version="0.3.1",
      description="a set of tools working with WSGI (see PEP 333)",
      author="Helmut Grohne",
      author_email="helmut@subdivi.de",
      url="http://subdivi.de/~helmut/wsgitools/",
      platforms = ["any"],
      license="GPL",
      keywords=["wsgi", "pep333", "scgi"],
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: No Input/Output (Daemon)",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Natural Language :: English",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Server"
      ],
      packages=["wsgitools", "wsgitools.scgi"])
