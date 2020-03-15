from gmqtt import Client as MQTTClient
from .lgws import Client as LGClient
import asyncio, logging

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except:
    logging.warning("Cannot set uvloop as asyncio event loop")

log = logging.getLogger(__name__)
stopEvent = asyncio.Event()

BASETOPIC = "lgtv"

def on_connect(client, flags, rc, properties):
    client.subscribe(BASETOPIC+'/#', qos=0)

def on_message(client, topic, payload, qos, properties):
    pass

def on_disconnect(client, packet, exc=None):
    if exc: log.exception(exc)

def on_subscribe(client, mid, qos, properties):
    log.debug('subscribtion successfull')

async def main(broker_host, token):
    client = MQTTClient(__name__)
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe
    
    if token:
        client.set_auth_credentials(token)
    log.debug(f'Connecting to {broker_host}')
    await client.connect(broker_host)

    def on_app_changed(status, payload):
        client.publish(BASETOPIC + "/app", payload)

    def on_volume_changed(status, payload):
        client.publish(BASETOPIC + "/volume", payload)

    lg = LGClient()
    lg.ac.subscribe_get_current(on_app_changed)        
    lg.mc.subscribe_get_volume(on_volume_changed)
    
    await stopEvent.wait()
    await client.disconnect()