import setuptools

setuptools.setup(
    name='mapbook',
    version='0.0.3',
    description='Windows Manager for Jupyter Notebook',
    url='',
    author='Jiangping He',
    author_email='johnbin.ho@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    include_package_data=True,
    data_files=[
        # like `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/mapbook", [
            "mapbook/static/main.js",
        ]),
        # like `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/notebook.d", [
            "jupyter-config/nbconfig/notebook.d/mapbook.json"
        ]),
        # like `jupyter serverextension enable --sys-prefix`
        ("etc/jupyter/jupyter_notebook_config.d", [
            "jupyter-config/jupyter_notebook_config.d/mapbook.json"
        ])
    ],    
    zip_safe=False,
)
