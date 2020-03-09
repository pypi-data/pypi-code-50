from setuptools import setup, find_packages

setup(
    name='wxcloudsdk', 
    version='0.0.3', 
    keywords='wechat miniprogram http sdk api', 
    description='Wechat miniprogram http api tools', 
    license='MIT License', 
    url='',
    author='typingcat', 
    author_email='liuchunyao0321@gmail.com',
    packages=find_packages(), 
    include_package_data=True,
    platforms='any', 
    install_requires=["requests"],
    python_requires='>=3.6'
)