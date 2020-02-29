import requests


def buscar_avatar(usuario):
    """
    Busca um avatar de um usuário no Github

    :param usuario: string com nome de um usuário no Github
    :return: str com link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('marvinsilva'))
