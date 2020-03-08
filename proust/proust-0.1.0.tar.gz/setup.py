from setuptools import find_packages, setup

setup(
    name="proust",
    version="0.1.0",
    author="Daniel Suo",
    author_email="danielsuo@gmail.com",
    description="A package for time series analysis",
    url="https://github.com/danielsuo/proust",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=["timeseries", "time", "series", "analysis"],
    python_requires=">=3.5",
    install_requires=[
        "numpy",
        "scipy",
        "cython",
        "jax",
        "jaxlib",
        "scikit-learn",
        "matplotlib",
    ],
    extras_require={
        "dev": [
            "flake8",
            "flake8-print",
            "flake8-bugbear",
            "mypy",
            "pytest",
            "pytest-xdist",
            "pytest-cov",
            "pylint",
            "black",
            "isort",
            "autoflake",
            "pre-commit",
            "pydocstring-coverage",
            "bumpversion",
        ]
    },
)
