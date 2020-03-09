import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="openstack_member_spammer_estimator",
    version="1.0.2",
    author="Sebastian Marcet",
    author_email="smarcet@gmail.com",
    description="Member Spam detector",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/OpenStackWeb/openstack_member_spammer_estimator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)