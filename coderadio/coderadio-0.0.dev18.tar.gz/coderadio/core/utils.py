from coderadio.logger import log


class Station:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _printable(self):
        return "{:>4} | {:<30} | tags: {} \n".format(
            self.id, self.name[0:30], self.tags
        )

    def __str__(self):
        return self._printable()

    def __repr__(self):
        return "<Station(name={})>".format(self.name)

    def get_metadata(self):
        pass


class StationList:
    def __init__(self, *args):
        self.new(*args)

    def new(self, *args):
        if args:
            self._list = []
            for index, obj in enumerate(args, 1):
                o = Station(**obj)
                o.id = index
                self._list.append(o)
        else:
            self._list = []

    def __getitem__(self, index):
        return self._list[index]

    def __len__(self):
        return len(self._list)

    def _printable(self):
        return "".join(s._printable() for s in self)

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __str__(self):
        return self._printable()


stations = StationList()
