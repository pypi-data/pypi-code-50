from setuptools import setup

setup(
    name="meeshkan-hosted-secrets",
    version="0.3",
    description="Utility package to access Secret Manager secrets on meeshkan.io",
    url="https://github.com/meeshkan/meeshkan-hosted-secrets",
    author="Meeshkan Dev Team",
    author_email="dev@meeshkan.com",
    license="MIT",
    packages=["meeshkan_hosted_secrets"],
    zip_safe=False,
    install_requires=["google-cloud-secret-manager==0.1.1"],
)
