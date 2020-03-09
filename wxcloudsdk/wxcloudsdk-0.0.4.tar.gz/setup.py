from setuptools import setup, find_packages

setup(
    name='wxcloudsdk', 
    version='0.0.4', 
    keywords='wechat miniprogram http sdk api', 
    description='Wechat miniprogram http api tools', 
    long_description='README.md',
    long_description_content_type='text/markdown',
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