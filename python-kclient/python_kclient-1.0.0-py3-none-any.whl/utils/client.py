import kclient


def with_bearer_token(token: str, debug: bool = False):
    cfg = kclient.Configuration()
    cfg.api_key['Authorization'] = token
    cfg.api_key_prefix['Authorization'] = 'Bearer'
    cfg.debug = debug
    return kclient.ApiClient(cfg)
