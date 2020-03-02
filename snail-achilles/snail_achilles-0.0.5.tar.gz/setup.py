import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="snail_achilles",
    version="0.0.5",
    author="AngeloLi",
    author_email="libiao_0303@live.com",
    description="Model file manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.woniubaoxian.com/ai/ai-achilles-service",
    packages=["achilles"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests>=2.23.0",
    ],
    python_requires='>=3.6',
    zip_safe=False,
)
