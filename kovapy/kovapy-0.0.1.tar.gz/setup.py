from setuptools import setup

setup(
    name='kovapy',
    version='0.0.1',
    description=
    'Kova Robotics Utilities Package. This is how I take over the world.',
    py_modules=["kovapy"],
    package_dir={'': 'src'},
    install_requires=[
        "slackclient ~= 2.5.0",
    ],
    url="http://www.kova.co.za",
    author="William Van Loggerenberg",
    author_email="will@kova.co.za",
)
