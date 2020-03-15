import json
import os

from xportage.default_reference import reference as default_reference
from xportage.reading_raw.get_reader import get_reader_cls


class XPortageHome(object):
    def __init__(self, home, cfg, force=False):
        self.home = home
        self.cfg_path = cfg
        self.cfg = self.setup_cfg(cfg, force=force)

    def setup_cfg(self, cfg, force=False):
        if not os.path.exists(cfg) or force:
            print('Initializing config file at {}'.format(cfg))
            os.makedirs(os.path.dirname(cfg), exist_ok=True)
            with open(cfg, 'w') as f:
                cfg_data = {}
                cfg_data['reference'] = default_reference
                f.write(json.dumps(cfg_data, sort_keys=True, indent=4))

        with open(cfg) as f:
            return json.loads(f.read())

    def print_configuration(self):
        log = 'XPORTAGE CONFIGURATION\n'
        log += '\n'
        log += '  HOME={}\n'.format(self.home)
        log += '  CFG={}\n'.format(self.cfg_path)
        print(log)

    def print_summary(self):
        directories = sorted([x for x in os.listdir(self.home) if os.path.isdir(os.path.join(self.home, x))])

        print('HOME DIRECTORIES\n')
        for x in directories:
            print(x)
        print('')

    def get_ref(self, ref_name):
        return self.cfg['reference']['sources'][ref_name]

    def download(self, ref=None, ref_name=None):
        if ref_name is not None:
            assert ref is None, 'Should only specify one of ref or ref_name.'
            ref = self.get_ref(ref_name)
        print('Downloading ref with name {}.'.format(ref['name']))
        tmp_dir = os.path.join(self.home, 'tmp')
        os.makedirs(tmp_dir, exist_ok=True)

        target = os.path.join(self.home, ref['name'] + '.raw')
        if os.path.exists(target):
            print('Already downloaded.')
            return

        # Download.
        os.system('cd {} && wget {}'.format(tmp_dir, ref['url']))

        # Unpack.
        my_tmp = 'my_tmp-{}'.format(ref['name'])
        os.system('cd {} && {}'.format(tmp_dir, ref['unpack'].format(tmp=my_tmp)))

        mv_from = os.path.join(tmp_dir, my_tmp)
        mv_to = target
        os.system('mv {} {}'.format(mv_from, mv_to))

        # Cleanup.
        os.system('cd {} && {}'.format(tmp_dir, ref['cleanup']))

    def preprocess(self, ref=None, ref_name=None):
        if ref_name is not None:
            assert ref is None, 'Should only specify one of ref or ref_name.'
            ref = self.get_ref(ref_name)
        print('Preprocessing ref with name {}.'.format(ref['name']))
        raw_dir = os.path.join(self.home, ref['name'] + '.raw')
        out_dir = os.path.join(self.home, ref['name'] + '.preprocess')
        os.makedirs(out_dir, exist_ok=True)

        reader = get_reader_cls(ref['name'])()

        for x in ref['splits']:
            path = os.path.join(raw_dir, x['path'])
            dataset = reader.read(path)

            out_data = os.path.join(out_dir, '{}.data.jsonl'.format(x['name']))
            print('writing {}'.format(out_data))
            with open(out_data, 'w') as f:
                keys = list(dataset['data'].keys())
                length = None
                for k in keys:
                    if length is None:
                        length = len(dataset['data'][k])
                    assert length == len(dataset['data'][k])
                for i in range(length):
                    ex = {}
                    for k in keys:
                        ex[k] = dataset['data'][k][i]
                    f.write(json.dumps(ex, sort_keys=True) + '\n')

            out_metadata = os.path.join(out_dir, '{}.metadata.json'.format(x['name']))
            print('writing {}'.format(out_metadata))
            with open(out_metadata, 'w') as f:
                f.write(json.dumps(dataset['metadata'], sort_keys=True, indent=4))
