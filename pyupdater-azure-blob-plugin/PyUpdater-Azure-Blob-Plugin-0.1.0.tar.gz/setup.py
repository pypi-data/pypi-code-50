from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="PyUpdater-Azure-Blob-Plugin",
    version="0.1.0",
    description="Azure Blob Storage plugin for PyUpdater",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Tom Hill",
    author_email="tomhill98@me.com",
    url="https://github.com/hill/PyUpdater-Azure-Blob-Plugin",
    platforms=["Any"],
    install_requires=["azure-storage-blob"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Environment :: Console",
    ],
    provides=["pyupdater.plugins",],
    entry_points={
        "pyupdater.plugins.upload": [
            "azure_blob_storage = azure_uploader:AzureBlobStorageUploader",
        ]
    },
    py_modules=["azure_uploader"],
    include_package_data=True,
)
