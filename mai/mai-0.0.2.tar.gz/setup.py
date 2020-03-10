from setuptools import find_packages, setup, Command

setup(name='mai',
        version='0.0.2',
        author="hcyx",
        author_email='whghcyx@outlook.com',
        url='https://gitee.com/whghcyx/sai',
        packages=find_packages(exclude=('code', 'data', 'test','*.ipynb', '*.bat')),
        install_requires=["torchsummaryX", "flyai"],
      )