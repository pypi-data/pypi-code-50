# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['r2c_isg',
 'r2c_isg.apis',
 'r2c_isg.functions',
 'r2c_isg.loaders',
 'r2c_isg.loaders.core',
 'r2c_isg.loaders.file',
 'r2c_isg.loaders.web',
 'r2c_isg.structures',
 'r2c_isg.structures.projects',
 'r2c_isg.structures.versions']

package_data = \
{'': ['*']}

install_requires = \
['click>=7.1.1,<8.0.0',
 'click_shell>=2.0,<3.0',
 'dill>=0.3.1,<0.4.0',
 'python-dotenv>=0.12.0,<0.13.0',
 'requests>=2.23.0,<3.0.0',
 'structures>=0.9.5,<0.10.0',
 'tqdm>=4.43.0,<5.0.0',
 'urllib3>=1.25.8,<2.0.0']

entry_points = \
{'console_scripts': ['r2c-isg = r2c_isg.cli:cli']}

setup_kwargs = {
    'name': 'r2c-inputset-generator',
    'version': '0.3.2',
    'description': 'An input set generator for R2C',
    'long_description': '# Input Set Generator\n\nThis is the input set generator for the R2C platform.\n\n## Installation\nTo install, simply `pip install r2c-inputset-generator`. Then run `r2c-isg` to load the shell.\n\n**Note:** This application caches HTTP requests to the various package registries in the terminal\'s current directory. Be sure to navigate to an appropriate directory before loading the shell, or use the command `set-api --nocache` inside the shell.\n\n## Quick Start\nTry the following command sequences:\n\n- Load the top 4,000 pypi projects by downloads in the last 365 days, sort by descending number of downloads, trim to the top 100 most downloaded, download project metadata and all versions, and generate an input set json.\n\n\t    load pypi list top4kyear\n\t    sort "desc download_count"\n\t    trim 100\n\t    get -mv all\n\t    set-meta -n test -v 1.0\n\t    export inputset.json\n\n- Load all npm projects, sample 100, download the latest versions, and generate an input set json.\n\n\t    load npm list allbydependents\n\t    sample 100\n\t    get -v latest\n\t    set-meta -n test -v 1.0\n\t    export inputset.json\n\n- Load a csv containing github urls and commit hashes, get project metadata and the latest versions, generate an input set json of type GitRepoCommit, remove all versions, and generate an input set json of type GitRepo.\n\n\t    load --columns "url v.commit" github file list_of_github_urls_and_commits.csv\n\t    get -mv latest\n\t    set-meta -n test -v 1.0\n\t    export inputset_1.json\n\t    trim -v 0\n\t    export inputset_2.json\n\n- Load a list of github repos from an organization name.\n\n\t    load github org netflix\n\n## Shell Usage\n\n#### Input/Output\n\n- **load** (OPTIONS) [noreg | github | npm | pypi] [WEBLIST_NAME | FILEPATH.csv]<br>\n\tGenerates a dataset from a weblist or a local file. The following weblists are available:\n    - Github: top1kstarred, top1kforked; the top 1,000 most starred or forked repos<br>\n    - NPM: allbydependents; **all** packages, sorted from most to fewest dependents count (caution: 1M+ projects... handle with care)<br>\n    - Pypi: top4kmonth and top4kyear; the top 4,000 most downloaded projects in the last 30/365 days\n\n\t**Options:**<br>\n    **-c --columns** "string of col names": A space-separated list of column names in a csv. Overrides default columns (name and version), as well as any headers listed in the file (headers in files begin with a \'!\'). The CSV reader recognizes the following column keywords: name, url, org, v.commit, v.version. All other columns are read in as project or version attributes.<br>\n    Example usage: --headers "name url downloads v.commit v.date".\n\n- **backup** (FILEPATH.p)<br>\n\tBacks up the dataset to a pickle file (defaults to ./dataset_name.p).\n\n- **restore** FILEPATH.p<br>\n\tRestores a dataset from a pickle file.\n\n- **import** [noreg | github | npm | pypi] FILEPATH.json<br>\n\tBuilds a dataset from an R2C input set.\n\n- **export** (FILEPATH.json)<br>\n\tExports a dataset to an R2C input set (defaults to ./dataset_name.json).\n\n#### Data Acquisition\n\n- **get** (OPTIONS)<br>\n\tDownloads project and version metadata from Github/NPM/Pypi.\n\n\t**Options:**<br>\n    **-m --metadata**: Gets metadata for all projects.<br>\n    **-v --versions** [all | latest]: Gets historical versions for all projects.\n\n#### Transformation\n\n- **trim** (OPTIONS) N<br>\n\tTrims the dataset to *n* projects or *n* versions per project.\n    \n    **Options**<br>\n    **-v --versions**: Binary flag; trims on versions instead of projects.\n\n- **sample** (OPTIONS) N<br>\n\tSamples *n* projects or *n* versions per project.\n    \n    **Options**<br>\n    **-v --versions**: Binary flag; sample versions instead of projects.\n\n- **sort** "[asc, desc] attributes [...]"<br>\n\tSorts the projects and versions based on a space-separated string of keywords. Valid keywords are:\n    - Any project attributes\n    - Any version attributes (prepend "v." to the attribute name)\n    - Any uuids (prepend "uuids." to the uuid name\n    - Any meta values (prepend "meta." to the meta name\n    - The words "asc" and "desc"\n    \n    All values are sorted in ascending order by default. The first keyword in the string is the primary sort key, the next the secondary, and so on.\n\n    Example: The string "uuids.name meta.url downloads desc v.version_str v.date" would sort the dataset by ascending project name, url, and download count; and descending version string and date (assuming those keys exist).\n\n\n#### Settings\n\n- **set-meta** (OPTIONS)<br>\n\tSets the dataset\'s metadata.\n\n\t**Options:**<br>\n\t**-n --name** NAME: Input set name. Must be set before the dataset can be exported.<br>\n    **-v --version** VERSION: Input set version. Must be set before the dataset can be exported.<br>\n    **-d --description** DESCRIPTION: Description string.<br>\n    **-r --readme** README: Markdown-formatted readme string.<br>\n    **-a --author** AUTHOR: Author name; defaults to git user.name.<br>\n    **-e --email** EMAIL: Author email; defaults to git user.email.<br>\n\n- **set-api** (OPTIONS)<br>\n\t**--cache_dir** CACHE_DIR: The path to the requests cache; defaults to ./.requests_cache.<br>\n    **--cache_timeout** DAYS: The number of days before a cached request goes stale.<br>\n    **--nocache**: Binary flag; disables request caching for this dataset.<br>\n    **--github_pat** GITHUB_PAT: A github personal access token, used to increase the max allowed hourly request rate from 60/hr to 5,000/hr. For instructions on how to obtain a token, see: [https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line). \n\n#### Visualization\n\n- **show**<br>\n\tConverts the dataset to a json file and loads it in the system\'s native json viewer.\n\n## Python Project\n\nYou can also import the package into your own project. Just import the Dataset structure, initialize it, and you\'re good to go!\n\n```\nfrom r2c_isg.structures import Dataset\n\nds = Dataset.import_inputset(\n    \'file.csv\' ~or~ \'weblist_name\',\n    registry=\'github\' ~or~ \'npm\' ~or~ \'pypi\',\n    cache_dir=path/to/cache/dir,      # optional; overrides ./.requests_cache\n    cache_timeout=int(days_in_cache), # optional; overrides 1 week cache timeout\n    nocache=True,                     # optional; disables caching\n    github_pat=your_github_pat        # optional; personal access token for github api\n)\n\nds.get_projects_meta()\n\nds.get_project_versions(historical=\'all\' ~or~ \'latest\')\n\nds.trim(\n    n,\n    on_versions=True\t# optional; defaults to False\n)\n\nds.sample(\n    n,\n    on_versions=True\t# optional; defaults to False\n)\n\nds.sort(\'string of sort parameters\')\n\nds.update(**{\'name\': \'you_dataset_name\', \'version\': \'your_dataset_version\'})\n\nds.export_inputset(\'your_inputset.json\')\n```\n\n## Troubleshooting\n\nIf you run into any issues, you can run the shell with the `--debug` flag enabled to get a full error message. Then reach out to `support@ret2.co` with the stack trace and the steps to reproduce the error.\n\n**Note:** If the issue is related to the "sample" command, be sure to seed the random number generator to ensure reproducibility.\n',
    'author': 'Return To Corporation',
    'author_email': 'hello@r2c.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://r2c.dev',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
