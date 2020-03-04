from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="GML",
    version="2.0.0",
    description="AUTO Machine Learning & AUTO Feature Engineering with many powerful tools.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Muhammad4hmed/Ghalat-Machine-Learning",
    author="Muhammad Ahmed",
    author_email="m.ahmed.memonn@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["GML"],
    include_package_data=True,
    install_requires=['scikit-learn','xgboost','catboost','Keras','lightgbm','autofeat'],
    
)
