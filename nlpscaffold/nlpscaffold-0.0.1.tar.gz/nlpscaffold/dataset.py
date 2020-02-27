import numpy as np
from tqdm import tqdm


class Dataset(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __add__(self, rhs):
        return self.__class__(super().__add__(rhs))

    def __getitem__(self, item):
        result = super().__getitem__(item)
        if isinstance(result, list):
            return self.__class__(result)
        else:
            return result

    def compute_metrics(self, preds):
        raise NotImplementedError()

    @classmethod
    def accumulate_preds(cls, preds, batch_preds):
        if preds is None:
            preds = batch_preds.copy()
        else:
            preds.update(batch_preds)
        return preds

    def batch(self, batch_size, shuffle=False, verbose=False, desc='batch'):
        items = self[:]
        if shuffle:
            np.random.shuffle(items)
        iterator = range(0, len(items), batch_size)
        if verbose:
            iterator = tqdm(iterator, desc=desc)
        for i in iterator:
            yield items[i:i+batch_size]
