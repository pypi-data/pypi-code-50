import setuptools

setuptools.setup(
    name="json2pytocol",
    version="0.0.1",
    author="Gabriel Piacenti",
    author_email="piacenti10@gmail.com",
    description="Generate Python Protocol Classes From Json",
    long_description="Generate Python Protocol Classes From Json",
    long_description_content_type="text/plain",
    packages=setuptools.find_packages(),
    install_requires=[
        "dotmap"
    ],
    test_require=["pytest"],
    entry_points={
        'console_scripts': [
            'json2pytocol = json2pytocol.json_to_python_protocol:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
