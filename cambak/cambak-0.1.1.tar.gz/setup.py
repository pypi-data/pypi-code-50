# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cambak', 'cambak.cameras']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['cambak = cambak:main_cli']}

setup_kwargs = {
    'name': 'cambak',
    'version': '0.1.1',
    'description': 'Simple tool for automating the derushing process of your cameras',
    'long_description': '# CamBak\nThis small tool automate the derushing process of your SD Cards for all your\ncameras.\n\nCamBak sort all your files from your SD Card per date, camera and per type of\nmedia and copy it to your computer or on a network volume. Here\'s is the\ndestination architecture:\n```\n/ *destination_folder*\n├── *date_of_shots (example: 2020-02-13)*\n│\xa0\xa0 └── *camera_name*\n│\xa0\xa0     ├── Pictures\n│\xa0\xa0     ├── RAW\n│\xa0\xa0     └── Videos\n```\n\n## Supported cameras architectures\n * Sony (tested with NEX6 and HDR-AS series, a6400 and AS100V)\n\nIf a camera is not supported, you can create a new file on the `cameras`\nfolder with the brand name, add a class inherited of `Camera` and add each\npaths and extensions for each type of medias (glog can be used for paths).\n\nHere\'s is an example for Sony NEX cameras (file `Sony.py`):\n```python\nclass SonyNex(Camera):\n    """General support for Sony NEX cameras (Alpha 5, 6, 7 and 9)"""\n\n    img_folders = ["DCIM/*MSDCF"]\n    raw_folders = img_folders\n    vid_folders = ["PRIVATE/M4ROOT/CLIP"]\n\n    img_extensions = [".JPG"]\n    raw_extensions = [".ARW"]\n    vid_extensions = [".MP4"]\n```\n\n## Usage\n```\n➜ python cambak --help\nusage: cambak [-h] -t TYPE -n NAME [-f] src dest\n\npositional arguments:\n  src                   Source folder (mounted card/usb camera volume)\n  dest                  Destination folder (local, network volume)\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -t TYPE, --type TYPE  Type of camera\n  -n NAME, --name NAME  Name of the camera\n  -f, --force           Override if file already exists in the dest folder\n```\n\nExample:\n```bash\ncambak /mnt/sd-card /mnt/moon-smb/cam-backups -t SonyNex -n A6400\n```\n\n## Installation\nWIP',
    'author': 'Michael Vieira',
    'author_email': 'github@mvieira.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Themimitoof/cambak.git',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)
