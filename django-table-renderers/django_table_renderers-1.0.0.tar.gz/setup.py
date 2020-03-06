import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_table_renderers",
    version="1.0.0",
    author="Josh Marshall",
    author_email="joshua.r.marshall.1991@gmail.com",
    description=(
        "Simple django rest framework renderers for converting python "
        "representations to tables to .xlsx or a group of .tgz'd .csv files."
    ),
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/anadon/django_table_renderers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Environment :: Other Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware",
    ],
    python_requires='>=3.6',
)
