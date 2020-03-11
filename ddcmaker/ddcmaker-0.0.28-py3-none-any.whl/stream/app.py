import time

from flask import Flask
from flask import Response
from ddcmaker.stream.io_stream import IOStream
from flask import request

app = Flask(__name__)

io_stream = IOStream()


@app.route('/read')
def read():
    def generate():
        global io_stream
        i = 0
        while True:
            if io_stream.readable():
                # i += 1
                info = io_stream.readline()
                # time.sleep(0.001)
                yield info

    return Response(generate())


@app.route('/write')
def write():
    global io_stream

    io_stream.write(f"{time.time()},{request.get_json()['info']}\n")
    return Response()


if __name__ == '__main__':
    # app.run(debug=True)
    # so the other machine can visit the website by ip
    app.run(host='127.0.0.1', debug=True)

# thread = threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 9000})
# thread.start()
