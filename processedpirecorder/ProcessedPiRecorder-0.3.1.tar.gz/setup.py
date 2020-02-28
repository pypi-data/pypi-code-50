with open("README.md", "r") as fh:
    long_description = fh.read()

import setuptools
setuptools.setup(
  name = 'ProcessedPiRecorder',         
  packages = ['ProcessedPiRecorder'],   
  version = '0.3.1',      
  license='GPLv3',        
  description = 'Multiprocessed picamera class for simpler and faster computer vision',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Matthew Davenport',      
  author_email = 'mdavenport@rockefeller.edu', 
  url = 'https://github.com/mattisabrat/ProcessedPiRecorder',
  install_requires=[            
          'picamera==1.13',
          'opencv-contrib-python==3.4.4.19',
          'tifffile==2019.7.26',
          'numpy==1.17.0',
          'imageio==2.6.1'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)' ,
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: POSIX :: Linux'
  ],
)
