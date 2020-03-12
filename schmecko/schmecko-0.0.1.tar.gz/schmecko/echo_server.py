#! /usr/bin/env python
import gzip

from argparse import ArgumentParser
from pprint import pprint
import io

from werkzeug.routing import Rule
from flask import Flask, request, jsonify

app = Flask(__name__)
app.url_map.add(Rule('/<path:path>', endpoint='path'))


@app.endpoint('path')
def echo(path):
    data = request.data
    if request.content_encoding == 'gzip':
        stream = io.BytesIO(data)
        data = gzip.GzipFile(fileobj=stream, mode='rb').read()

    pprint(data)
    response = dict(method=request.method,
                    host=request.host,
                    path=request.path,
                    args=request.args,
                    headers=dict(request.headers.items()),
                    data='')
    return jsonify(response)


ap = ArgumentParser()
ap.add_argument('-p', '--port', default=9080)
ap.add_argument('--host', default='0.0.0.0')


def run():
    args = ap.parse_args()
    app.run(host=args.host, port=args.port, debug=True, use_reloader=True)


if __name__ == '__main__':
    run()
