from setuptools import setup

setup(name='synaw_tools',
      version='0.1',
      package_dir={"": "src"},
      setup_requires=["setuptools>=40.0", "twine"],
      install_requires=["jinja2", "pyyaml"]
#      data_files=[
#            ('/etc/bash_completion.d/', ['extra/etc/bash_completion.d/synaw_tool']),
#      ],
)
