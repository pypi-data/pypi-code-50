from setuptools import setup, find_packages

setup(
    name="bilibili-live-recorder",
    version="0.1",
    packages=find_packages("src"),
    platforms=["unix"],
    install_requires=["requests", "loguru"],
    entry_points={"console_script": ["blr = src.main"]},
    author="yuzao",
    description="This is an script used to record bilibili live stream",
    keywords="bilibili live",
    license='MIT',
)
