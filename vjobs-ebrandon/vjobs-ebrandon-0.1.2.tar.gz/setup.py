import setuptools


setuptools.setup(
    name='vjobs-ebrandon',
    version='0.1.2',
    url='https://gitlab.com/flaxking/vjobs-ebrandon',
    author='flaxking',
    author_email='flaxking@digitalnostril.com',
    description='Collects jobs from ebrandon.ca for vjobs',
    long_description='Collects jobs from ebrandon.ca for vjobs',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['vjobs >= 0.1.0'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
