from setuptools import setup, find_packages  # type: ignore

setup(
    name="antimait",
    version="0.1",
    description="antimait is a library made of tools to ease the implementation "
                "of IoT automation systems based on devices such as Arduino and ESP.",
    author="Gianmarco Marcello",
    author_email="g.marcello@antima.it",
    url="https://github.com/Antimait/antimait",
    python_requires=">=3.7",
    install_requires=["matplotlib", "pyserial", "typing_extensions"],
    packages=find_packages(exclude=["tests"]),
)
