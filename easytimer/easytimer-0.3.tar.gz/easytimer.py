__all__ = ['tick', 'tock']

import time


class TickTock:
    def __init__(self):
        self.counter = 1
        self.records = []

        # records holds {name: str, time: float}

    def tick(self, name: str = None):
        # Auto generate a name for the tick if no name is provided
        if name is None:
            name = "tick " + str(self.counter)
            self.counter += 1

        self.records.append({'name': name, 'time': time.time()})

    def tock(self, clear: bool = True):
        # Call tick() one last time to end the previous tick timer
        self.tick()

        names = [d['name'] for d in self.records]
        times = [d['time'] for d in self.records]

        result = {name: 0 for name in names[:-1]}

        for i in range(len(names)):
            try:
                name = names[i]
                delta = times[i + 1] - times[i]
                result[name] += delta
            except IndexError:
                pass  # The last item was inserted by the tick() inside of tock() and is only to get the final delta

        max_len = max(len(name) for name in names)

        output = '--- Timer Results ---\n'
        for name, t in result.items():
            output += name.ljust(max_len + 1) + "- " + format_time(t) + '\n'
        output += '---------------------'

        print(output)

        if clear:
            self.records = []
            self.counter = 1


def format_time(seconds: int):
    days, remainder = divmod(seconds, 24 * 60 * 60)
    hours, remainder = divmod(remainder, 60 * 60)
    minutes, seconds = divmod(remainder, 60)

    if days:
        return f"{days:.0f}d {hours:.0f}h {minutes:.0f}m {seconds:.0f}s"
    elif hours:
        return f"{hours:.0f}h {minutes:.0f}m {seconds:.0f}s"
    elif minutes:
        return f"{minutes:.0f}m {seconds:.0f}s"
    else:
        return f"{seconds:.2f}s"


# Allow user to call tick() without creating any object after importing this module
_ticktock = TickTock()

tick = _ticktock.tick
tock = _ticktock.tock
