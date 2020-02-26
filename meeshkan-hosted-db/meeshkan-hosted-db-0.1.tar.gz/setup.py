import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


setup(
    name="meeshkan-hosted-db",
    version="0.1",
    description="Utility package to access a Cloud SQL database on meeshkan.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meeshkan/meeshkan-hosted-db",
    author="Meeshkan Dev Team",
    author_email="dev@meeshkan.com",
    license="MIT",
    packages=["meeshkan_hosted_db"],
    zip_safe=False,
    install_requires=["meeshkan-hosted-secrets==0.4", "psycopg2-binary==2.8.4"],
)
