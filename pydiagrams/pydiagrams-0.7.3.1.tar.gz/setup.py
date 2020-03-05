import setuptools

# References for setup tools:
#  https://setuptools.readthedocs.io/en/latest/
# Building and Distributing Packages with Setuptools: https://setuptools.readthedocs.io/en/latest/setuptools.html

with open('pydiagrams/README.md', 'rt') as f:
    long_description = f.read()

setuptools.setup(
      name='pydiagrams',
      version='0.7.3.1',
      author='Matthew Billington',
      author_email='mbillington@gmail.com',
      description='Generate software diagrams using Python syntax',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/billingtonm/pydiagrams',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires = ['colour', 'pillow', 'plantuml'],
      # entry points defines the command line version
      entry_points = {},
      zip_safe=False,
      include_package_data=True,
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python :: 3.8',
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            'Intended Audience :: Developers',
            'Environment :: Console',
            'Topic :: Software Development',
      ],      
      python_requires='>=3.8',
      )
