import quixote
import quixote.build.pip as pip
from quixote.build.installs import install_docker_cli
import time

blueprint = quixote.Blueprint(
    name="aaa",
    author="bbb"
)


@quixote.builder
def install_docker():
    install_docker_cli()
    pip.install("docker")


@quixote.inspector
def test():
    print("OK")
