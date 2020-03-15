import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="basicpy2captcha",
    version="1.0.0",
    author="xWorthless",
    author_email="xworthlesscode@gmail.com",
    description="A basic python 2captcha.com modulee",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xWorthless/py2captcha",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)