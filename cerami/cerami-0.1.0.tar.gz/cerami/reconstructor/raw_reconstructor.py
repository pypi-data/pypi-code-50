from .base_reconstructor import BaseReconstructor

class RawReconstructor(BaseReconstructor):
    def reconstruct(self, item):
        return item
