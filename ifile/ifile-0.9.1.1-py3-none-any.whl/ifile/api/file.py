import logging
import mimetypes

from flask import request, jsonify, make_response, url_for
from flask.views import MethodView
from werkzeug import exceptions as exc

from ifile.exception import NotFound
from ifile.storage import api as storage_api
from ifile import client as client_api
from ifile.apps.task import app

logger = logging.getLogger(__name__)


# async task
def get_file(host, filepath):
    return client_api.get_file(host, filepath)


class Files(MethodView):
    def get(self):
        items = []
        files = storage_api.Files()
        for file_id in files:
            _file = storage_api.File(file_id)
            item = _file.to_json()
            item.update({
                "url": url_for("api.file", id=file_id, _external=True),
                "downloader_url": url_for(
                    "api.downloader_file", id=file_id, _external=True)
            })
            items.append(item)

        return jsonify(items)

    def post(self):
        f = request.files.get('file')
        files = storage_api.Files()
        _file = files.add(f.filename, f.stream)

        item = {
            'id': _file.id,
            'url': url_for("api.file", id=_file.id, _external=True),
            'downloader_url': url_for(
                "api.downloader_file", id=_file.id, _external=True)
        }
        return jsonify(item), 201


class File(MethodView):
    def get(self, id):
        try:
            _file = storage_api.File(id)
        except NotFound as e:
            raise exc.NotFound(str(e))

        item = _file.to_json()
        item.update({
            "url": url_for("api.file", id=id, _external=True),
            "downloader_url": url_for(
                "api.downloader_file", id=id, _external=True)
        })
        return jsonify(item)

    def delete(self, id):
        try:
            _file = storage_api.File(id)
        except NotFound as e:
            raise exc.NotFound(str(e))

        _file.destroy()

        response = make_response()
        response.status_code = 204
        return response


class FileDownloader(MethodView):
    def get(self, id):
        try:
            _file = storage_api.File(id)
            bdata = _file.stream
        except NotFound as e:
            raise exc.NotFound(str(e))

        response = make_response(bdata)

        mime_type = mimetypes.guess_type(_file.name)
        response.headers['Content-Type'] = mime_type
        response.headers['Content-Disposition'] = \
            'attachment; filename={}'.format(
                _file.name.encode().decode('latin-1'))
        return response


class RemoteFiles(MethodView):
    def post(self):
        payload = request.json

        host = payload["host"]
        filepath = payload["filepath"]

        task = app.apply(get_file, host, filepath)

        return jsonify({
            "task_id": task.context.id
        })
