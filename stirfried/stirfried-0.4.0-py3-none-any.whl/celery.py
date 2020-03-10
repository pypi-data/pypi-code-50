from celery import Task
from socketio import RedisManager


class StirfriedTask(Task):
    _sio = None

    @property
    def sio(self):
        """Property that ensures each Task instance (1 per worker process) uses
        a single Redis connection for Socket.IO communication for all of its
        task invocations.

        Note that the user must configure `app.conf.stirfried_redis_url` via standard
        Celery config mechanisms.
        """
        if self._sio is None:
            self._sio = RedisManager(self.app.conf.stirfried_redis_url, write_only=True)
        return self._sio
        # NOTE: unclear when to close connection
        # no "close()" or "free()" method available

    @property
    def error_info(self):
        return self.app.conf.get("stirfried_error_info", False)

    def emit_progress(self, current, total, info=None):
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
                info=info,
                # additional info
                task_id=self.request.id,
                task_name=self.name,
            ),
        )

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        """Emits when task invocation fails and is retried.

        Note that this callback is called automatically by Celery.
        """
        data = dict(
            task_id=task_id,
            task_name=self.name,
        )
        if self.error_info:
            data['einfo'] = str(einfo)
        self.sio.emit(
            "on_retry",
            room=kwargs["room"],
            data=data,
        )

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        """Emits when task invocation fails.

        Note that this callback is called automatically by Celery.
        """
        data = dict(
            task_id=task_id,
            task_name=self.name,
        )
        if self.error_info:
            data['einfo'] = str(einfo)
        self.sio.emit(
            "on_failure",
            room=kwargs["room"],
            data=data,
        )

    def on_success(self, retval, task_id, args, kwargs):
        """Emits when task invocation succeeds.

        Note that this callback is called automatically by Celery.
        """
        data = dict(
            retval=retval,
            task_id=task_id,
            task_name=self.name,
        )
        self.sio.emit(
            "on_success",
            room=kwargs["room"],
            data=data,
        )

    def after_return(self, status, retval, task_id, args, kwargs, einfo):
        """Emits when task invocation returns (success/failure).

        Note that this callback is called automatically by Celery.
        """
        if isinstance(retval, Exception):
            retval = str(retval)
        data = dict(
            status=status,
            retval=retval,
            task_id=task_id,
            task_name=self.name,
        )
        self.sio.emit(
            "on_return",
            room=kwargs["room"],
            data=data,
        )
