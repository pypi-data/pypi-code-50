from celery import Celery
import socketio


celery_app = Celery()
CONFIG_MODULE = "settings"
celery_app.config_from_object(CONFIG_MODULE)

try:
    redis_url = celery_app.conf.stirfried_redis_url
except AttributeError:
    raise AttributeError("Configuration key `stirfried_redis_url` missing")

available_tasks = set(celery_app.conf.get("stirfried_available_tasks", []))

socketio_opts = {
    key[9:]: value
    for key, value in celery_app.conf.items()
    if key.startswith("socketio_")
}

mgr = socketio.AsyncRedisManager(redis_url)
sio = socketio.AsyncServer(client_manager=mgr, async_mode="asgi", **socketio_opts)
app = socketio.ASGIApp(sio)


@sio.event
def revoke_task(sid, message):
    """Call to revoke a task from the worker fleet."""
    celery_app.control.revoke(message)


@sio.event
def send_task(sid, message: dict):
    """Call to send a task to the worker fleet."""
    args = message.get("args", ())
    kwargs = {
        **message.get("kwargs", {}),
        **dict(room=sid),
    }
    task_name = message["task_name"]
    if len(available_tasks) > 0 and task_name not in available_tasks:
        return dict(status="failure", data=f"unknown task {task_name}")
    t = celery_app.send_task(task_name, args=args, kwargs=kwargs)
    return dict(status="success", data=t.id)
