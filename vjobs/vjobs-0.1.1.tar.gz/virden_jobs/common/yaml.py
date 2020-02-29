import yaml


def load(file):

    with open(file, 'r') as stream:
        return yaml.safe_load(stream)
