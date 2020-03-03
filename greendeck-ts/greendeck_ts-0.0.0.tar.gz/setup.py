import setuptools

# with open("README.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name = "greendeck_ts",
    __version__ = "1.0.1",
    author = "sambal shikhar",
    author_email = "sambal@greendeck.co",
    url = "",
    packages=['gd_generator', 'gd_generator.src'],
)

