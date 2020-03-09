"""FNLI Persian Natural Language Inference(NLI) and Auestion Answering (QA) dataset.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ..utils.data_utils import get_file
from ..preprocessing.sequence import _remove_long_seq
import numpy as np
import json
import warnings


def load_data(path='fnli.npz', num_words=None, skip_top=0,
              maxlen=None, seed=113,
              start_char=1, oov_char=2, index_from=3, **kwargs):
    """Loads the FNLI dataset.
    # Arguments
        path: where to cache the data (relative to `~/.fnli/dataset`).
        num_words: max number of words to include. Words are ranked
            by how often they occur (in the training set) and only
            the most frequent words are kept
        skip_top: skip the top N most frequently occurring words
            (which may not be informative).
        maxlen: sequences longer than this will be filtered out.
        seed: random seed for sample shuffling.
        start_char: The start of a sequence will be marked with this character.
            Set to 1 because 0 is usually the padding character.
        oov_char: words that were cut out because of the `num_words`
            or `skip_top` limit will be replaced with this character.
        index_from: index actual words with this index and higher.
    # Returns
        Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
    # Raises
        ValueError: in case `maxlen` is so low
            that no input sequence could be kept.
    Note that the 'out of vocabulary' character is only used for
    words that were present in the training set but are not included
    because they're not making the `num_words` cut here.
    Words that were not seen in the training set but are in the test set
    have simply been skipped.
    """
    # Legacy support
    if 'nb_words' in kwargs:
        warnings.warn('The `nb_words` argument in `load_data` '
                      'has been renamed `num_words`.')
        num_words = kwargs.pop('nb_words')
    if kwargs:
        raise TypeError('Unrecognized keyword arguments: ' + str(kwargs))

    path = get_file(path,
                    origin='https://raw.githubusercontent.com/m-azari/fnli/master/data/fnli.npz',
                    file_hash='077389b62dbaa56592bbc4519fe75e5e')
    with np.load(path, allow_pickle=True) as f:
        p_train , h_train , l_train = f['p_train'] , f['h_train'] , f['l_train']
        p_dev , h_dev , l_dev = f['p_dev'] , f['h_dev'] , f['l_dev']
        p_test , h_test , l_test = f['p_test'] , f['h_test'] , f['l_test']

    rng = np.random.RandomState(seed)
    indices = np.arange(len(p_train))
    rng.shuffle(indices)
    p_train = p_train[indices]
    h_train = h_train[indices]
    l_train = l_train[indices]

    indices = np.arange(len(p_dev))
    rng.shuffle(indices)
    p_dev = p_dev[indices]
    h_dev = h_dev[indices]
    l_dev = l_dev[indices]

    indices = np.arange(len(p_test))
    rng.shuffle(indices)
    p_test = p_test[indices]
    h_test = h_test[indices]
    l_test = l_test[indices]

    ps = np.concatenate([p_train, p_dev, p_test])
    hs = np.concatenate([h_train, h_dev, h_test])
    ls = np.concatenate([l_train, l_test, l_test])

    if start_char is not None:
        ps = [[start_char] + [w + index_from for w in x] for x in ps]
    elif index_from:
        ps = [[w + index_from for w in x] for x in ps]

    if start_char is not None:
        hs = [[start_char] + [w + index_from for w in x] for x in hs]
    elif index_from:
        hs = [[w + index_from for w in x] for x in hs]

    if maxlen:
        tmep1 = []
        temp2 = []
        temp3 = []
        for i,  in len(ps):
            if len(ps[i]) < maxlen and len(hs[i]) < maxlen:
                temp1.append(ps[i])
                temp2.append(hs[i])
                temp3.append(ls[i])
        xs, hs, ls = temp1, temp2, temp3
        if len(xs)==0:
            raise ValueError('After filtering for sequences shorter than maxlen=' +
                             str(maxlen) + ', no sequence was kept. '
                             'Increase maxlen.')
    if not num_words:
        num_words1 = max([max(x) for x in ps])
        num_words2 = max([max(x) for x in hs])
        num_words = max([num_words1, num_words2])

    # by convention, use 2 as OOV word
    # reserve 'index_from' (=3 by default) characters:
    # 0 (padding), 1 (start), 2 (OOV)
    if oov_char is not None:
        ps = [[w if (skip_top <= w < num_words) else oov_char for w in x]
              for x in ps]
    else:
        ps = [[w for w in x if skip_top <= w < num_words]
              for x in ps]

    if oov_char is not None:
        hs = [[w if (skip_top <= w < num_words) else oov_char for w in x]
              for x in hs]
    else:
        hs = [[w for w in x if skip_top <= w < num_words]
              for x in hs]

    idx1 = len(p_train)
    idx2 = len(p_dev)
    p_train, h_train, l_train = np.array(ps[:idx1]), np.array(hs[:idx1]), np.array(ls[:idx1])
    p_dev, h_dev, l_dev = np.array(ps[idx1:idx1+idx2]), np.array(hs[idx1:idx1+idx2]), np.array(ls[idx1:idx1+idx2])
    p_test, h_test, l_test = np.array(ps[idx1+idx2:]), np.array(hs[idx1+idx2:]), np.array(ls[idx1+idx2:])

    return (p_train, h_train, l_train), (p_dev, h_dev, l_dev), (p_test, h_test, l_test)


def get_word_index(path='fnli_word_index.json'):
    """Retrieves the dictionary mapping words to word indices.
    # Arguments
        path: where to cache the data (relative to `~/.keras/dataset`).
    # Returns
        The word index dictionary.
    """
    path = get_file(
        path,
        origin='https://raw.githubusercontent.com/m-azari/fnli/master/data/fnli_word_index.json',
        file_hash='ee7c460edad2757a2ddf94f7324b133b')
    with open(path) as f:
        return json.load(f)