import click
import pyzipper

@click.command()
@click.option("-p", "--password", required=True)
@click.argument("zipfile", nargs=1, required=True)
@click.argument("dst", default=None, nargs=1, required=False)
def unzip(password, zipfile, dst):
    """Unzip AES encrypted zip file.
    """
    with pyzipper.AESZipFile(zipfile) as package:
        package.setpassword(password.encode("utf-8"))
        package.extractall(dst)

if __name__ == "__main__":
    unzip()
