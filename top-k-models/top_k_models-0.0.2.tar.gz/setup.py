import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
p_version = "0.0.2"

setuptools.setup(
    name="top_k_models", 
    version=p_version,
    author="Priscilla Chauke",
    author_email="priscilla.chk@gmail.com",
    description="Top-k classification and model selector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU General Public License v3.0",
    url="https://github.com/priscilla-chk/top_k_models",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['numpy','pandas','scikit-learn'],
)
