import setuptools

setuptools.setup(name='sparse-pendulum',
    version='0.0.5',
    author="Christoper Glenn Wulur",
    author_email="christoper.glennwu@gmail.com",
    description="Open AI gym Pendulum Env with sparse rewards",
    packages=setuptools.find_packages(),
    install_requires=['gym']#And any other dependencies required
)
