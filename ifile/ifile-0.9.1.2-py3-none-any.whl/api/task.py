from flask import jsonify
from flask.views import MethodView

from ifile.apps.task import app


class Task(MethodView):
    def get(self, task_id):
        task = app.get_async_task(task_id)
        context = task.context
        return jsonify(context.to_json())


class Tasks(MethodView):
    def get(self):
        tasks = []
        _tasks = app.get_async_tasks()
        for task in _tasks:
            tasks.append(task.context.to_json())

        return jsonify(tasks)
