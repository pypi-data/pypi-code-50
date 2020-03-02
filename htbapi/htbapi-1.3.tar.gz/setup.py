from setuptools import setup

setup(
        name="htbapi",
        version="1.3",
        description="An unofficial API Wrapper for Hackthebox.",
        long_description=open("README.md", "r").read(),
        long_description_content_type="text/markdown",
        license="GPL",
        author="sw1tchbl4d3",
        author_email="jsimeze@pm.me",
        url="https://gitlab.com/sw1tchbl4d3/htbapi",
        packages=["htbapi"],
        install_requires=["requests"]
)
