import numpy as np
import pandas as pd
import pytest
import collections
from os import path

from flatspin.data import Dataset, read_csv
from flatspin.utils import eval_dict

@pytest.fixture
def dataset(tmpdir_factory):
    basedir = tmpdir_factory.mktemp('test')
    index = pd.DataFrame({'A': np.arange(0,1,0.1), 'B': np.arange(0,10)//2})
    params = {'foo': 1, 'bar': [1,2,3]}
    info = {'array': np.array([3,2,1])}
    ds = Dataset(index, params, info, basedir)
    return ds

def test_len(dataset):
    assert len(dataset) == len(dataset.index)

def test_getitem(dataset):
    """ dataset[i] -> subset """
    ds = dataset[0]
    assert isinstance(ds, Dataset)
    assert len(ds) == 1

    ds = dataset[0:3]
    assert isinstance(ds, Dataset)
    assert len(ds) == 4

def test_iter(dataset):
    """ iter(dataset) -> iterator over subsets """
    ds = list(iter(dataset))
    assert len(ds) == len(dataset)
    assert all([isinstance(d, Dataset) for d in dataset])
    assert all([len(d) == 1 for d in dataset])

def test_keys(dataset):
    """ dataset.keys() -> list of indices """
    keys = dataset.keys()
    assert len(keys) == len(dataset)
    assert keys == list(range(len(dataset)))

def test_items(dataset):
    """ dataset.items() -> iterator over i, subsets """
    items = list(dataset.items())
    keys = [k for k,v in items]
    values = [v for k,v in items]

    assert keys == dataset.keys()
    assert values == list(dataset)

def test_filter(dataset):
    """ dataset.filter(A=0.5) -> subset """
    ds = dataset.filter(A=0.5)
    assert isinstance(ds, Dataset)
    assert len(ds) == 1

    ds = dataset.filter(A=1.0)
    assert isinstance(ds, Dataset)
    assert len(ds) == 0

    ds = dataset.filter(A=(None, 0.3))
    assert isinstance(ds, Dataset)
    assert len(ds) == 4

    ds = dataset.filter(A=(-100, 0.3))
    assert isinstance(ds, Dataset)
    assert len(ds) == 4

    ds = dataset.filter(A=(0.1, 0.3))
    assert isinstance(ds, Dataset)
    assert len(ds) == 3

    ds = dataset.filter(A=(0.4, None))
    assert isinstance(ds, Dataset)
    assert len(ds) == 6

    ds = dataset.filter(A=(0.4, 100))
    assert isinstance(ds, Dataset)
    assert len(ds) == 6

def test_groupby(dataset):
    """ dataset.groupby(column) -> iterator """
    groups = list(dataset.groupby('B'))
    B = np.unique(dataset.index['B'])
    for i, ds in groups:
        assert np.all(ds.index['B'] == B[i])

def test_save(dataset):
    dataset.save()
    assert path.exists(path.join(dataset.basepath, 'index.csv'))
    assert path.exists(path.join(dataset.basepath, 'params.csv'))
    assert path.exists(path.join(dataset.basepath, 'info.csv'))

    index = read_csv(path.join(dataset.basepath, 'index.csv'))
    assert np.all(index == dataset.index)

    params = read_csv(path.join(dataset.basepath, 'params.csv'))
    params = dict(np.array(params))
    params = eval_dict(params)
    assert params == dataset.params

    info = read_csv(path.join(dataset.basepath, 'info.csv'))
    info = dict(np.array(info))
    info = eval_dict(info)
    assert np.all(info['array'] == dataset.info['array'])

def test_read(dataset):
    dataset.save()
    dataset2 = Dataset.read(dataset.basepath)

    assert dataset == dataset2
