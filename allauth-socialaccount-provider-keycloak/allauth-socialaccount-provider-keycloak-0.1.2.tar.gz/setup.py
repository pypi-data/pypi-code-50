import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="allauth-socialaccount-provider-keycloak",
    version="0.1.2",
    author="Félix José Hernández",
    author_email="info@felixjosehernandez.es",
    description="allauth oauth2 provider for Keycloak",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fherdom/allauth-socialaccount-provider-keycloak",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
