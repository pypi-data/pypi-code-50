import setuptools
 
setuptools.setup(
    name="qualityforward",
    version="1.0",
    author="Atsushi Nakatsugawa",
    author_email="atsushi@moongift.jp",
    description="Python library for QualityForward API",
    long_description="This is python library for QualityForward API. QualityForward is cloud based test management service.",
    long_description_content_type="text/markdown",
    url="https://cloud.veriserve.co.jp/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
