from .sender import Sender


class ConsoleSender(Sender):
    def __init__(self):
        super().__init__()

    def init(self, panel):
        super().init(panel)

    def update(self):
        print("Panel {} in frame nr.{:d}".format(self.panel.id, self.panel.frame))
