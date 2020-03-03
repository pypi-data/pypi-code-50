import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask_auth_service_mongo",
    version="0.0.5",
    author="Terminus",
    author_email="mateo.chaparro@zinobe.com",
    description="Flask authentication package with mongo.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/terminus-zinobe/flask-auth-service-mongo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'bandit',
        'bcrypt==3.1.7',
        'Cerberus==1.3.2',
        'flake8==3.7.8',
        'flask==1.1.1',
        'PyJWT==1.7.1',
        'pytest==5.2.1',
        'pytest-cov',
        'mongoengine==0.18.2',
        'mongomock==3.18.0',
        'radon',
        'sphinx',
        'sphinx-glpi-theme==0.3',
        'sphinxcontrib-httpdomain==1.7.0'
    ]
)
