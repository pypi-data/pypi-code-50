import io

from chardet.universaldetector import UniversalDetector


def file_encoding(filepath):
    detector = UniversalDetector()
    with io.open(filepath, 'rb') as file:
        while True:
            data = file.read(io.DEFAULT_BUFFER_SIZE)
            if data:
                detector.feed(data)
                if detector.done:
                    break
            else:
                break
    detector.close()
    return detector.result.get('encoding', 'ascii').lower()
