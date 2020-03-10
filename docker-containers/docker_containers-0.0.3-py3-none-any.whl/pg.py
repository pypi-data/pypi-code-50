import asyncio
import logging
from typing import Optional

from asyncpg.pool import Pool, create_pool

from .container import DockerContainer
from .utils import wait_is_ready, inside_container

__all__ = ('PostgresContainer',)

logger = logging.getLogger(__name__)


async def check_db_pool(dsn, **kwargs):
    pool = await create_pool(dsn=dsn, **kwargs)
    await pool.close()


class PostgresContainer(DockerContainer):

    def __init__(self, user: str, password: str,
                 database: Optional[str] = None,
                 image="postgres:11-alpine",
                 port_to_expose: int = 5432):
        super(PostgresContainer, self).__init__(image=image)
        self.user = user
        self.password = password
        self.database = database or user
        self.port_to_expose = port_to_expose

    def _connect(self):
        def connect_db():
            url = self.get_connection_url()
            loop = asyncio.get_event_loop()
            loop.run_until_complete(check_db_pool(url))

        wait_is_ready(connect_db)

    def start(self):
        self._configure()
        super().start()
        self.reload()
        try:
            self._connect()
        except:
            self.stop()
            raise

        return self

    def _configure(self):
        self.with_exposed_ports(self.port_to_expose)
        self.with_env("POSTGRES_USER", self.user)
        self.with_env("POSTGRES_PASSWORD", self.password)
        self.with_env("POSTGRES_DB", self.database)

    def get_connection_url(self) -> str:
        if inside_container():
            return self.get_external_connection_url()

        host = self.get_container_host_ip(self.port_to_expose)
        port = self.get_exposed_port(self.port_to_expose)
        return f'postgresql://{self.user}:{self.password}@{host}:{port}/{self.database}?sslmode=disable'

    def get_external_connection_url(self) -> str:
        host = self.get_host_ip()
        port = self.port_to_expose
        return f'postgresql://{self.user}:{self.password}@{host}:{port}/{self.database}?sslmode=disable'

    def get_jdbc_connection_url(self) -> str:
        host = self.get_host_ip()
        port = self.port_to_expose
        return f'jdbc:postgresql://{host}:{port}/{self.database}?sslmode=disable'
