import yaml
from pathlib import Path


DEFAULT_CONF_PATH = Path.home() / '.config' / 'waky' / 'waky.yml'


class Config:
    def __init__(self):
        try:
            with open(DEFAULT_CONF_PATH, "r") as file:
                conf = yaml.full_load(file)

                for item, doc in documents.items():
                    print(item, ":", doc)
        except FileNotFoundError:
            


if __name__ == "__main__":
    config = Config()
    config
