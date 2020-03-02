import sys


class Outer:
    def __init__(self):
        self.messages = []

    def print(self, msg):
        self.messages.append(msg)
        self.messages.append("\n")

    def flush(self):
        pass

    def write(self, msg):
        self.print(msg)
        pass

    def clear(self):
        self.messages = []

    def get(self):
        result = "".join(self.messages)
        self.clear()
        return result


def main():
    newout = Outer()
    stdout = sys.stdout
    sys.stdout = newout
    print("Hi")
    import time

    time.sleep(1)
    result = newout.get()
    sys.stdout = stdout
    print(result)


if __name__ == "__main__":
    main()
