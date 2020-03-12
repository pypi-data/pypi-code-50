import finac as f
import finac.api as api

import logging
import os
import yaml
from pathlib import Path

__version__ = '1.0.14'

dir_me = Path(__file__).absolute().parents[1]

f.core.logger = logging.getLogger('gunicorn.error')
api.logger = f.core.logger

fname = os.environ.get('FES_CONFIG')
if not fname or not Path(fname).exists():
    fname = f'{dir_me}/etc/fes.yml'
if not Path(fname).exists():
    fname = '/opt/fes/etc/fes.yml'
if not Path(fname).exists():
    fname = '/usr/local/etc/fes.yml'

with open(fname) as fh:
    config = yaml.load(fh.read())['fes']

if 'finac' in config:
    fc = config['finac']
    for k, v in fc.copy().items():
        if '-' in k:
            fc[k.replace('-', '_')] = v
            del fc[k]
f.init(**config.get('finac', {}))
api.real_ip_header = config.get('real-ip-header')
api.key = config['key']
app = api.app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
