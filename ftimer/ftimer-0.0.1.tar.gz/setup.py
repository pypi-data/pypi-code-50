
from setuptools import setup
setup(
  name="ftimer", # Replace with your own username
  version="0.0.1",
  author="Milad Khaleghi",
  author_email="milad_khaleghi@live.com",
  description="A freelancere timer to track your working time",
  packages=['ftimer'],
  # long_description=long_description,
  # long_description_content_type="text/markdown",
  # url="https://github.com/pypa/sampleproject",
  # packages=setuptools.find_packages(),
  # classifiers=[
  #     "Programming Language :: Python :: 3",
  #     "License :: OSI Approved :: MIT License",
  #     "Operating System :: OS Independent",
  # ],
  # python_requires='>=3.6',

  entry_points={
    'console_scripts':[
      'ftimer=ftimer.main:ftimer',
    ]
  }

)