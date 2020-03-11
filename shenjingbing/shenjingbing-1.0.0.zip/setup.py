from setuptools import setup


def readme_file():
    with open("README.rst",encoding="utf-8") as rf:
        return rf.read()




setup(name="shenjingbing",version="1.0.0",description="this is a lihailihai lib",packages=["sztestlib"],py_modules=["Tool"],
      author="dameinu",author_email="2796185835@qq.com",long_description=readme_file(),license="MIT"
      )