import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="greendeck-redis",
    version="1.0.2",
    author="yashvardhan srivastava",
    author_email="yash@greendeck.com",
    description="Greendeck Redis Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yash6992",
    packages=['greendeck_redis', 'greendeck_redis.src', 'greendeck_redis.src.redis'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'redis'
    ],
    include_package_data=True,
    zip_safe=False
)
