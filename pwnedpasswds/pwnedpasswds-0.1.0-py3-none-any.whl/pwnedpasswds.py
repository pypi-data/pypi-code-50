import hashlib

import click
import requests


def hash_passwd(passwd):
    """Hash a password with SHA1 and return the digest split into [:5], [5:]

    :param passwd: password to hash

    :return: digest[:5], digest[5:]
    """
    hash_digest = hashlib.sha1(passwd.encode("utf-8")).hexdigest().upper()
    return hash_digest[:5], hash_digest[5:]


def check_passwd(passwd):
    """Check to see if a password appears in the pwned passwords database

    :param passwd: password to check
    :type passwd: str

    :return: amount of times password appears. -1 if there was an error
    :rtype: int
    """

    hash_head, hash_tail = hash_passwd(passwd)
    url = f"https://api.pwnedpasswords.com/range/{hash_head}"
    r = requests.get(url)

    if r.status_code == 200:
        hash_tails = r.text.split("\n")
        for ht in hash_tails:
            tail, count = ht.split(":")
            if tail == hash_tail:
                return count
        return 0
    return -1


@click.command()
@click.argument("passwd", required=False)
def cli(passwd):
    if passwd:
        click.echo(check_passwd(passwd))
    else:
        stdin = click.open_file("-", "r")
        while (passwd := stdin.readline().strip()) != "":
            result = check_passwd(passwd)
            click.echo(result)
