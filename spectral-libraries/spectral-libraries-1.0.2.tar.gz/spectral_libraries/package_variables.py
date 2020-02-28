from os import path

package_name_pip = 'spectral-libraries'
qgis_plugin_name = 'Spectral Library Tool'

author = 'Ann Crabbé (KU Leuven); Benjamin Jakimow (HU Berlin)'
author_email = 'ann.crabbe@kuleuven.be'
short_version = '1.0'
long_version = '1.0.2'

bitbucket_home = 'https://bitbucket.org/kul-reseco/spectral-libraries'
bitbucket_src = 'https://bitbucket.org/kul-reseco/spectral-libraries/src'
bitbucket_issues = 'https://bitbucket.org/kul-reseco/spectral-libraries/issues?status=new&status=open'

read_the_docs = 'https://spectral-libraries.readthedocs.io'

keywords = ['ies', 'ear', 'masa', 'cob', 'emc', 'cres', 'square array', 'spectral library', 'remote sensing']

qgis_min_version = '3.6'

# read the contents of your README file
with open(path.join(path.join(path.dirname(__file__), '..'), 'README.md'), encoding='utf-8') as f:
    read_me = f.read()

read_me_lines = read_me.splitlines()

short_description = ' '.join(read_me_lines[3:5])
long_description = ' '.join(read_me_lines[3:24])

icon = 'images/lumos_h60.png'
qgis_category = 'Raster'