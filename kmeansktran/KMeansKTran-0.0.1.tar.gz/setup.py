import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KMeansKTran", 
    version="0.0.1",
    author="Kevin Tran",
    author_email="KTranKHS@gmail.com",
    description="K-Means Clustering Package to return best K using Silhouette Analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KTranKHS/KMeans_BCM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
    ],
    python_requires='>=3.7.4',
)