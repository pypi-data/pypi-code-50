import types, os

class ProgressReader:
    def listen(self):
        raise NotImplementedError("This progress reader does not support listening to messages")

class ProgressFileReader(ProgressReader):
    def __init__(self, file):
        self.file = file
        self.messages = []
        self.progress = []

    def listen(self, process):
        import base64
        from time import sleep
        preamble = chr(240) + chr(80) + chr(85) + chr(248) + chr(228)
        bar = chr(191) * 3
        in_message = False
        if not os.path.exists(self.file):
            # Touch the file if it doesn't exist
            with open(self.file, "a"):
                pass
        with open(self.file, 'r') as f:
            f.seek(0, 2)
            while True:
                sleep(0.1)
                line = f.read()
                if line:
                    start = 0
                    while True:
                        n = line.find(preamble, start)
                        if n == -1:
                            break
                        if in_message:
                            payload = line[(start + len(preamble) - 1):n]
                            header, message = tuple(map(
                                lambda s: base64.b64decode(bytes(s, 'UTF-8')).decode('UTF-8'),
                                payload.split(bar)
                            ))
                            if header == '':
                                self.messages.append(message)
                            elif header == 'simulation_progress':
                                data = message.split("+")
                                progress = types.SimpleNamespace(
                                    progression = float(data[0]),
                                    duration = float(data[1]),
                                    time = float(data[2]),
                                )
                                self.progress.append(progress)
                                yield progress
                        in_message = not in_message
                        start = n + 1
                if process.poll() is not None:
                    break
