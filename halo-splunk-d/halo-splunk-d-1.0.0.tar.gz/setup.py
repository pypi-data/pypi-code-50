from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
long_description = 'Halo Splunk plugin Package made \
    for a demo of its making for the Halo Splunk Integration.' 
  
setup( 
        name ='halo-splunk-d', 
        version ='1.0.0', 
        author ='Tom Miller', 
        author_email ='tmiller@cloudpassage.com', 
        url ='https://github.com/cloudpassage/splunk-halo-python', 
        description ='Package for Halo Splunk plugin.', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'hspi = halo_splunk.hspi:main'
            ] 
        }, 
        classifiers =( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        keywords ='halo splunk plugin python package halo_splunk', 
        install_requires = requirements, 
        zip_safe = False
) 
