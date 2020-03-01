from setuptools import setup, find_packages


requirements = ["numpy", "scipy", "napari>=0.2.12", "tifffile"]


setup(
    name="surfcut",
    version="0.0.1",
    description="Automated 3D cell detection and registration of whole-brain images",
    install_requires=requirements,
    python_requires=">=3.6",
    packages=find_packages(),
    entry_points={"console_scripts": ["surfcut = surfcut.run:main",]},
    include_package_data=True,
    zip_safe=False,
)
