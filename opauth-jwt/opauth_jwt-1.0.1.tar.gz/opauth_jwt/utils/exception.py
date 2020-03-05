
class JWTAuthenticationFailedException(Exception):
    def __init__(self, detail='JWT authentication failed!', *args: object, **kwargs: object) -> None:
        self.detail = detail
        super().__init__(*args, **kwargs)
