import jwt
import requests


class AtlantisClient:
    """Cliente HTTP para comunicação com Atlantis

    :param str atlantis_url: Endereço da API do serviço Atlantis
    :param str client_id: ID do cliente cadastrado no Atlantis
    """

    def __init__(self, atlantis_url, client_id):
        self.atlantis_url = atlantis_url
        self.client_id = client_id

    def issue_token(self, code, client_secret):
        """Realiza a troca do code pelo token

        Exemplo:

        .. code-block:: python

            from stl_sdk.torpedo import AtlantisClient

            client = AtlantisClient('https://accounts.spacetimeanalytics.com', 'client_id_abc123')
            token = client.issue_token('code123abc', 'id123abc')

        :param code: Código concedido pelo Atlantis via redirect (authorization_code)
        :type code: str
        :param client_secret: Secret do cliente cadastrado no Atlantis
        :type client_secret: str
        :return: Dicionário com os tokens: ``access_token``, ``id_token`` e ``refresh_token``
        :rtype: dict
        """
        response = requests.post(
            '{}/token'.format(self.atlantis_url),
            data={
                'code': code,
                'client_id': self.client_id,
                'client_secret': client_secret
            },
            params={
                'grant_type': 'authorization_code'
            })
        response.raise_for_status()
        return response.json()

    def get_public_key(self):
        """Obtém a chave pública do Atlantis para validação do token de acesso

        :return: Chave pública
        :rtype: str
        """
        response = requests.get('{}/key'.format(self.atlantis_url))
        response.raise_for_status()
        return response.json()

    def validate_token(self, token):
        """Valida token de acesso do usuário

        Exemplo:

        .. code-block:: python

            from stl_sdk.torpedo import AtlantisClient

            client = AtlantisClient('https://accounts.spacetimeanalytics.com', 'client_id_abc123')
            token_payload = client.validate_token('tokenJwT')

        :param token: Token JWT do usuário gerado pelo Atlantis
        :type token: str
        :raises InvalidTokenError: Se o token estiver expirado ou alterado
        :return: Retorna o payload do token JWT
        :rtype: dict
        """
        public_key = self.get_public_key()

        try:
            return jwt.decode(token, public_key, audience=self.client_id)
        except Exception as err:
            raise InvalidTokenError(err)


class InvalidTokenError(RuntimeError):
    pass
