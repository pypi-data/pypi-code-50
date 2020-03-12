import finac as f
import finac.api as api

import logging
import os
import yaml

__version__ = '1.0.17'

f.core.logger = logging.getLogger('gunicorn.error')
api.logger = f.core.logger

with open(os.environ.get('FES_CONFIG')) as fh:
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
