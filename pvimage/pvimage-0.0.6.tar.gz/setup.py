from setuptools import setup

setup(name='pvimage',
      version='0.0.6',
      description='package for pv image analysis and machine learning modeling',
      url='http://engineering.case.edu/centers/sdle/',
      author='Ahmad Maroof Karimi, Benjamin G. Pierce, Justin S. Fada, Nicholas A. Parrilla, Roger H. French, Jennifer L. Braid',
      author_email='axk962@case.edu, jlbraid@sandia.gov',
      license='Apache License v2',
      packages=['pvimage'],
      package_dir={'pvimage': './pvimage'},
      package_data={'pvimage': ['files/data/Minimodules/*','files/data/FullSizeModules/*','files/tutorials/*','files/data/out','README.rst']},
      python_requires='>=3.6.5',
      install_requires=['markdown', 'pyhull','opencv-python','scipy','scikit-image','glob2'],
      include_package_data=True,
      zip_safe=False)
