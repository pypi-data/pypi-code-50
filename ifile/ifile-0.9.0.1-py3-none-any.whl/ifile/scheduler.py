import logging
from datetime import datetime, timedelta

from ifile.beats import beat
from ifile.manage.client import Clients

logger = logging.getLogger(__name__)


@beat(second=2)
def check_client():
    clients = Clients()
    for (hostname, ip), c in clients.clients.items():
        util_time = datetime.now() - timedelta(seconds=10)
        if c.last_alive_time is None or c.last_alive_time < util_time:
            clients.unregister(hostname, ip)
