from celery import Celery
import socketio


celery_app = Celery()
CONFIG_MODULE = "settings"
celery_app.config_from_object(CONFIG_MODULE)
try:
    SOCKETIO_REDIS = celery_app.conf.socketio_redis
except ImportError:
    raise ImportError(
        "Set configuration key `socketio_redis` by "
        f"providing an importable `{CONFIG_MODULE}` module"
    )

mgr = socketio.AsyncRedisManager(SOCKETIO_REDIS)
sio = socketio.AsyncServer(client_manager=mgr, async_mode="asgi")
app = socketio.ASGIApp(sio)


@sio.event
def revoke_task(sid, task_id):
    """Call to revoke a task from the worker fleet."""
    celery_app.control.revoke(task_id)


@sio.event
def send_task(sid, message: dict):
    """Call to send a task to the worker fleet."""
    args = message.get("args", ())
    kwargs = {
        **message.get("kwargs", {}),
        **dict(room=sid),
    }
    t = celery_app.send_task(message["task_name"], args=args, kwargs=kwargs)
    return t.id
