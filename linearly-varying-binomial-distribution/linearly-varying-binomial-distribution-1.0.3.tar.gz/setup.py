from setuptools import setup
from setuptools.extension import Extension

def main():
    with open("README.md", "r") as fh:
        long_description = fh.read()

    ext_module = Extension(
        "lvbdist._lvbdist",
        ["lvbdist/lvbdist_back.c", "lvbdist/lvbdistcalcs/prob_func.c"],
        include_dirs=["lvbdist", "lvbdist/lvbdistcalcs"],
        depends=["lvbdist/lvbdistcalcs/prob_func.h"]
    )

    setup(name="linearly-varying-binomial-distribution",
          version="1.0.3",
          description="computes ununiform step-increasing probability problems",
          long_description=long_description,
          long_description_content_type="text/markdown",
          author="cos",
          author_email="cleoold@gmail.com",
          packages=["lvbdist"],
          url="https://github.com/cleoold/linearly_varying_binomial_distribution_calcs_Python",
          classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
        ],
          include_package_data=True,
          ext_modules=[ext_module])

if __name__ == "__main__":
    main()
