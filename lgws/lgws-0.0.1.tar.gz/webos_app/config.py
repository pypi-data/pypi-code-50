class Config(object):
    DEBUG=False
    TESTING=False
    LGTV_PATH="~/.config/lgtv"

class DevConfig(Config):
    DEBUG=True

class ProdConfig(Config):
    pass

class TestConfig(Config):
    TESTING=True