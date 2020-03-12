import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="planajob",
    version="3.1.5",
    author="Terry Hughes",
    author_email="terryhugheskirkcudbright@yahoo.co.uk",
    description="A sales order and purchasing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

