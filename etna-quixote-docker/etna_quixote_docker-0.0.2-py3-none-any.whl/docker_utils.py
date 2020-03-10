from contextlib import contextmanager
import docker


@contextmanager
def docker_daemon_autocleanup():
    try:
        yield
    finally:
        client = docker.from_env()

        # Kill any remaining container
        for container in client.containers.list():
            container.kill()

        # Remove any remaining network
        for network in client.networks.list():
            if network.name not in ("none", "bridge", "host"):
                network.remove()
