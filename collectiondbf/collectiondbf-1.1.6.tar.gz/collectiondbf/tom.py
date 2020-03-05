import requests
from blackfynn import Blackfynn

import os
import sys
import platform
import argparse
import json
import appdirs
from pathlib import Path
def config_file():
    CONFIG_DIR = Path(appdirs.user_config_dir(appname='collectiondbf'))  # magic
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    config = CONFIG_DIR / 'config.json'
    if config.exists():
        with config.open('r') as f:
            return json.load(f)
    else:
        return False

config = config_file()
bf = Blackfynn(api_token=config['token'], api_secret=config['secret'])
col = bf.get('N:collection:54cb8ead-b5e0-4687-8f98-45c49f65ab24')
for file in col.items:
    file_type = get_file_type(file.s3_key)
    response = request.get(file.url)
    if response.status_code == 200:
        sys.stdout.write('\rDownloading file: %s' % file.name)
        f = open(os.path.join(file_path, col.name, file.name + '.' + file_type), 'wb')
        f.write(response.content)
        sys.stdout.flush()