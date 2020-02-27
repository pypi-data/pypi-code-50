import precept


class TopDrawerConfig(precept.Config):
    api_key = precept.ConfigProperty(
        auto_global=True, comment='Your bighugelabs.com api key',
        environ_name='BHL_API_KEY'
    )
