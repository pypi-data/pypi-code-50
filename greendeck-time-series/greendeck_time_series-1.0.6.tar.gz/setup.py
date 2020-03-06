import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="greendeck_time_series",
    version="1.0.6",
    author="sambal shikhar",
    author_email="sambal@greendeck.com",
    description="Greendeck Time Series",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['greendeck_time_series', 'greendeck_time_series.src', 'greendeck_time_series.src.time_series'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'timesynth'
    ],
    include_package_data=True,
    zip_safe=False
)
