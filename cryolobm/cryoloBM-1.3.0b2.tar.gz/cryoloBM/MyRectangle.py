from matplotlib.patches import Rectangle


class MyRectangle(Rectangle):
    def __init__(self, xy, width, height, angle=0.0, est_size=None, **kwargs):
        self.confidence = None
        self.est_size = est_size
        super(MyRectangle, self).__init__(xy, width, height, angle, **kwargs)

    def set_confidence(self,confidence):
        self.confidence = confidence
