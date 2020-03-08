import shaonutil
import json
import wheel

with open('config.json', 'r') as f:
    distros_dict = json.load(f)

"""
parsed_json = (json.loads('config.json'))
print(json.dumps(parsed_json, indent=4, sort_keys=True))
"""

project_name = distros_dict['project_name']
version_name = distros_dict['version_name']
author_name = distros_dict['author_name']
author_email_name = distros_dict['author_email_name']
tag_list = distros_dict['tag_list']
console_script_needed = eval(distros_dict['console_script_needed'])


console_scripts_string = """
  entry_points={
      'console_scripts': [
          '"""+project_name+"""="""+project_name+"""."""+project_name+""":main',
      ],
  },"""

string_ = f"""#from distutils.core import setup
from setuptools import setup
from os import path

# read the contents of your README file
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = '"""+project_name+"""',
  packages = ['"""+project_name+"""'],
  setup_requires=['wheel'],
  version = '"""+version_name+"""',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = '"""+author_name+"""',
  author_email = '"""+author_email_name+"""',
  url = 'https://github.com/ShaonMajumder/"""+project_name+"""',
  download_url = 'https://github.com/ShaonMajumder/"""+project_name+"""/archive/"""+version_name+""".tar.gz',
  keywords = """+str(tag_list)+""",
  classifiers = [],"""+ (console_scripts_string if console_script_needed else """""") +"""
)
"""

shaonutil.file.write_file("output_setup.py", string_,mode="w")