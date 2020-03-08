from celery import Task
from socketio import RedisManager


class StirfriedTask(Task):
    _sio = None

    @property
    def sio(self):
        """Property that ensures each Task instance (1 per worker process) uses
        a single Redis connection for Socket.IO communication for all of its
        task invocations.

        Note that the user must configure `app.conf.socketio_redis` via standard
        Celery config mechanisms.
        """
        if self._sio is None:
            self._sio = RedisManager(self.app.conf.socketio_redis, write_only=True)
        return self._sio
        # NOTE: unclear when to close connection
        # no "close()" or "free()" method available

    def emit_progress(self, current, total):
        """Emits task invocation progress.

        Note that this callback must be called by the user in the task body.
        """
        self.sio.emit(
            "on_progress",
            room=self.request.kwargs["room"],
            data=dict(
                # callback arguments
                current=current,
                total=total,
                # additional info
                task_id=self.request.id,
                task_name=self.name,
            ),
        )

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        """Emits when task invocation returns (success/failure).

        Note that this callback is called automatically by Celery.
        """
        self.sio.emit(
            "on_return",
            room=kwargs["room"],
            data=dict(
                # TODO: can we return error info? is it serializable?
                status=status,
                retval=retval,
                task_id=task_id,
                task_name=self.name,
            ),
        )

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        """Emits when task invocation failed and is retried.

        Note that this callback is called automatically by Celery.
        """
        self.sio.emit(
            "on_retry",
            room=kwargs["room"],
            data=dict(
                # TODO: can we return error info? is it serializable?
                task_id=task_id,
                task_name=self.name,
            ),
        )
