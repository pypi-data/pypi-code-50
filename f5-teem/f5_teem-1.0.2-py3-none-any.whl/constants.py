""" Constants used throughout this package """

VERSION = '1.0.2'

USER_AGENT = 'f5-teem-python/%s' % (VERSION)
HTTP = {
    'VERIFY': True,
    'TIMEOUT': {
        'DEFAULT': 5
    }
}

ENVIRONMENTS = {
    'published': ['production', 'staging'],
    'env_var': 'F5_TEEM_API_ENVIRONMENT'
}
ENDPOINTS = {
    'anonymous': {
        'production': {
            'endpoint': 'product.apis.f5.com',
            'api_key': 'mmhJU2sCd63BznXAXDh4kxLIyfIMm3Ar'
        },
        'staging': {
            'endpoint': 'product-tst.apis.f5networks.net',
            'api_key': None # client MUST provide API key for non-prod
        }
    }
}
