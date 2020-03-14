import json
import os


class PortageHome(object):
    def __init__(self, home, cfg):
        self.home = home
        self.cfg = cfg
        self.setup_cfg(cfg)

    def setup_cfg(self, cfg):
        if not os.path.exists(cfg):
            print('Initializing config file at {}'.format(cfg))
            os.makedirs(os.path.dirname(cfg), exist_ok=True)
            with open(cfg, 'w') as f:
                f.write(json.dumps({}))

    def print_configuration(self):
        log = 'PORTAGE CONFIGURATION\n'
        log += '\n'
        log += '  HOME={}\n'.format(self.home)
        log += '  CFG={}\n'.format(self.cfg)
        print(log)

    def print_summary(self):
        directories = sorted([x for x in os.listdir(self.home) if os.path.isdir(os.path.join(self.home, x))])

        for x in directories:
            print(x)
