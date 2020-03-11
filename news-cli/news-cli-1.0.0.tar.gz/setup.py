from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="news-cli",
    version='1.0.0',
    packages=find_packages(),
    package_data={'common': ['app_settings.json']},
    include_package_data=True,
    author='Shubhi Rani & Rohan Singh',
    description="A cli app to get news snapshots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/ygivenx/the-local-news",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    author_email='shubhirohan@yandex.com',
    install_requires=[
        'Click', 'prettytable', 'requests',
    ],
    entry_points={
        'console_scripts': ['news=interface.cli.cli:main']
    }
)
