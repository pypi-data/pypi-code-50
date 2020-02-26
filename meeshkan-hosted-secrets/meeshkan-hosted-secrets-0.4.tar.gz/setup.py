import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()


setup(
    name="meeshkan-hosted-secrets",
    version="0.4",
    description="Utility package to access Secret Manager on meeshkan.io",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/meeshkan/meeshkan-hosted-secrets",
    author="Meeshkan Dev Team",
    author_email="dev@meeshkan.com",
    license="MIT",
    packages=["meeshkan_hosted_secrets"],
    zip_safe=False,
    install_requires=["google-cloud-secret-manager==0.1.1"],
)
