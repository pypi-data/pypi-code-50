from os import path

package_name_pip = 'spectral-libraries'
qgis_plugin_name = 'Spectral Library Tool'
read_the_docs_name = 'SpectralLibraries'

author = 'Ann Crabbé (KU Leuven); Benjamin Jakimow (HU Berlin)'
author_doc = 'Ann Crabbé (KU Leuven)'
author_email = 'ann.crabbe@kuleuven.be'
author_copyright = '2020, Ann Crabbé'
short_version = '1.0'
long_version = '1.0.4'

bitbucket_home = 'https://bitbucket.org/kul-reseco/spectral-libraries'
bitbucket_src = 'https://bitbucket.org/kul-reseco/spectral-libraries/src'
bitbucket_issues = 'https://bitbucket.org/kul-reseco/spectral-libraries/issues'

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

sphinx_title = 'Spectral Library Tool Documentation'
