"""
actions when sub init in cli, including mkdir, touch files and render templates in templates fold
"""
import os, json


def env_init(path, conf=None): ## note conf here is not from config.json, since there is no such file at the phase
    ## the source of the conf here should be interactive cli or specify json file from sub init -f config.json
    if not conf:
        conf = default_conf()
    mkdirs(path, conf)
    render_config(path, conf)
    ## history should be prepared in preprocessor together with inputs files generation

def default_conf():
    conf = {}
    conf['inputs_dir'] = "inputs"
    conf['outputs_dir'] = "outputs"
    conf['inputs_prefix'] = "main"
    conf['outputs_prefix'] = "main"
    conf['check_inputs_prefix'] = "check"
    conf['check_outputs_prefox'] = "check"
    conf['resource_limit'] = {}
    return conf


def mkdirs(path, conf):
    os.mkdir(os.path.join(path, conf['inputs_dir']))
    os.mkdir(os.path.join(path, conf['outputs_dir']))
    os.mkdir(os.path.join(path, ".subway"))


def render_config(path, conf):
    with open(os.path.join(path, ".subway", "config.json"), "w") as f:
        json.dump(conf, f, indent=2)

## temporary tests
if __name__ == "__main__":
    env_init("/Users/shixin/Documents/newwork/practice/subway/dev2")