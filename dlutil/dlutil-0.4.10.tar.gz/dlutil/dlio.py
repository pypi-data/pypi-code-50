import numpy as np
import h5py
import torch
import torch.utils.data as Data


def _shape_check(a, with_batch=True):
    if with_batch:
        shape_dim_limit = 1
    else:
        shape_dim_limit = 0
    if len(a.shape) < shape_dim_limit:
        raise ValueError(f'Check {a.shape}')
    elif len(a.shape) == shape_dim_limit:
        a = a[..., np.newaxis]
    else:
        a = a
    return a

# Write data to HDF5


def write_h5_from_arrays(filename, xs, ys, is_appending=False):
    '''This function is to write h5 file using np arrays.
    xs: list of np arrays, which stands for x;
    ys: list of np arrays, which stands for y. (ys can be None for unsupervised learning)
    Caution: the length of x and y should be the same.
    '''
    if is_appending:
        fh5 = h5py.File(filename, mode='r+')
        h5xs = fh5['x']
        x_len = h5xs.attrs['len']
        xs_names = list(h5xs.keys())
        cur_len_x = len(xs[0])
        for name, x in zip(xs_names, xs):
            xds = h5xs[name]
            xds.resize((x_len+cur_len_x, *xds.shape[1:]))
            x = _shape_check(x, with_batch=True)
            xds[x_len:x_len+cur_len_x, ...] = x
        h5xs.attrs['len'] = x_len + cur_len_x
        if ys is not None:
            h5ys = fh5['y']
            y_len = h5ys.attrs['len']
            ys_names = list(h5ys.keys())
            cur_len_y = len(ys[0])
            for name, y in zip(ys_names, ys):
                yds = h5ys[name]
                yds.resize((y_len+cur_len_y, *yds.shape[1:]))
                y = _shape_check(y, with_batch=True)
                yds[y_len:y_len+cur_len_y, ...] = y
            h5ys.attrs['len'] = y_len + cur_len_y
            assert h5xs.attrs['len'] == h5ys.attrs['len'], 'length of x and y is inconsistent'
    else:
        fh5 = h5py.File(filename, mode='w')
        h5xs = fh5.create_group('x')
        cur_len_x = len(xs[0])
        h5xs.attrs['len'] = cur_len_x
        for i, x in enumerate(xs, start=1):
            x = _shape_check(x, with_batch=True)
            h5xs.create_dataset(
                f'x{i}', shape=x.shape, dtype=x.dtype, data=x, maxshape=(None, *x.shape[1:]))
        if ys is not None:
            h5ys = fh5.create_group('y')
            cur_len_y = len(ys[0])
            h5ys.attrs['len'] = cur_len_y
            for i, y in enumerate(ys, start=1):
                y = _shape_check(y, with_batch=True)
                h5ys.create_dataset(
                    f'y{i}', shape=y.shape, dtype=y.dtype, data=y, maxshape=(None, *y.shape[1:]))
            assert h5xs.attrs['len'] == h5ys.attrs['len'], 'length of x and y is inconsistent'
    fh5.close()


def write_classified_h5_from_arrays(filename, dt, is_appending=False):
    '''This function is to write classified h5 file using np arrays.
    dt: dt[c] = [xs, ys]
    c: class, which can be integer, string... etc.
    xs: list of np arrays, which stands for x;
    ys: list of np arrays, which stands for y. 
    Caution: the length of x and y should be the same.
    '''
    if is_appending:
        fh5 = h5py.File(filename, mode='r+')
        cur_classes = fh5.attrs['classes'].tolist()
        all_classes = cur_classes[:]
        for c in dt:
            xs, ys = dt[c]
            if c in cur_classes:
                h5xs = fh5[f'c{c}']['x']
                x_len = h5xs.attrs['len']
                xs_names = list(h5xs.keys())
                cur_len_x = len(xs[0])
                for name, x in zip(xs_names, xs):
                    xds = h5xs[name]
                    xds.resize((x_len+cur_len_x, *xds.shape[1:]))
                    x = _shape_check(x, with_batch=True)
                    xds[x_len:x_len+cur_len_x, ...] = x
                h5xs.attrs['len'] = x_len + cur_len_x
                if ys is not None:
                    h5ys = fh5[f'c{c}']['y']
                    y_len = h5ys.attrs['len']
                    ys_names = list(h5ys.keys())
                    cur_len_y = len(ys[0])
                    for name, y in zip(ys_names, ys):
                        yds = h5ys[name]
                        yds.resize((y_len+cur_len_y, *yds.shape[1:]))
                        y = _shape_check(y, with_batch=True)
                        yds[y_len:y_len+cur_len_y, ...] = y
                    h5ys.attrs['len'] = y_len + cur_len_y
                    assert h5xs.attrs['len'] == h5ys.attrs['len'], 'length of x and y is inconsistent'
            else:
                all_classes.append(c)
                cset = fh5.create_group(f'c{c}')
                h5xs = cset.create_group('x')
                cur_len_x = len(xs[0])
                h5xs.attrs['len'] = cur_len_x
                for i, x in enumerate(xs, start=1):
                    x = _shape_check(x, with_batch=True)
                    h5xs.create_dataset(
                        f'x{i}', shape=x.shape, dtype=x.dtype, data=x, maxshape=(None, *x.shape[1:]))
                if ys is not None:
                    h5ys = cset.create_group('y')
                    cur_len_y = len(ys[0])
                    h5ys.attrs['len'] = cur_len_y
                    for i, y in enumerate(ys, start=1):
                        y = _shape_check(y, with_batch=True)
                        h5ys.create_dataset(
                            f'y{i}', shape=y.shape, dtype=y.dtype, data=y, maxshape=(None, *y.shape[1:]))
                    assert h5xs.attrs['len'] == h5ys.attrs['len'], 'length of x and y is inconsistent' + str(
                        h5xs.attrs['len']) + '\t' + str(h5ys.attrs['len'])
        fh5.attrs['classes'] = all_classes

    else:
        fh5 = h5py.File(filename, mode='w')
        fh5.attrs['classes'] = list(dt.keys())
        for c in fh5.attrs['classes']:
            xs, ys = dt[c]
            cset = fh5.create_group(f'c{c}')
            h5xs = cset.create_group('x')
            cur_len_x = len(xs[0])
            h5xs.attrs['len'] = cur_len_x
            for i, x in enumerate(xs, start=1):
                x = _shape_check(x, with_batch=True)
                h5xs.create_dataset(
                    f'x{i}', shape=x.shape, dtype=x.dtype, data=x, maxshape=(None, *x.shape[1:]))
            if ys is not None:
                h5ys = cset.create_group('y')
                cur_len_y = len(ys[0])
                h5ys.attrs['len'] = cur_len_y
                for i, y in enumerate(ys, start=1):
                    y = _shape_check(y, with_batch=True)
                    h5ys.create_dataset(
                        f'y{i}', shape=y.shape, dtype=y.dtype, data=y, maxshape=(None, *y.shape[1:]))
                assert h5xs.attrs['len'] == h5ys.attrs['len'], 'length of x and y is inconsistent' + str(
                    h5xs.attrs['len']) + '\t' + str(h5ys.attrs['len'])
    fh5.attrs['lens'] = [fh5[f'c{c}/x'].attrs['len']
                         for c in fh5.attrs['classes']]
    fh5.close()


def write_h5_from_generator(filename, xgns, ygns, is_appending=False, preallocated_slots=5000):
    '''This function is to write h5 file using generators.
    xgns: list of generators, which stands for x;
    ygns: list of generators, which stands for y. (ygns can be None for unsupervised learning)
    Caution: data from generators has no batch dim, e.g. 32x32 RGB images will be generated using (3, 32, 32), not (batch, 3, 32, 32). Batch dim will be automatically added in hdf5 file.
    '''
    if is_appending:
        fh5 = h5py.File(filename, mode='r+')
        h5xs = fh5['x']
        x_len = h5xs.attrs['len']
        xs_names = list(h5xs.keys())
        for name, xgn in zip(xs_names, xgns):
            xds = h5xs[name]
            cur_len = 0
            for x in xgn:
                x = _shape_check(x, with_batch=False)
                if x_len + cur_len >= len(xds):
                    xds.resize((len(xds) + preallocated_slots, *xds.shape[1:]))
                xds[x_len+cur_len] = x
                cur_len += 1
            h5xs.attrs['len'] = x_len + cur_len
            xds.resize((x_len + cur_len, *xds.shape[1:]))
        if ygns is not None:
            h5ys = fh5['y']
            y_len = h5ys.attrs['len']
            ys_names = list(h5ys.keys())
            for name, ygn in zip(ys_names, ygns):
                yds = h5ys[name]
                cur_len = 0
                for y in ygn:
                    y = _shape_check(y, with_batch=False)
                    if y_len + cur_len >= len(yds):
                        yds.resize(
                            (len(yds) + preallocated_slots, *yds.shape[1:]))
                    yds[y_len+cur_len] = y
                    cur_len += 1
                h5ys.attrs['len'] = y_len + cur_len
                yds.resize((y_len + cur_len, *yds.shape[1:]))
            assert h5xs.attrs['len'] == h5ys.attrs['len'], 'length of x and y is inconsistent'
    else:
        fh5 = h5py.File(filename, mode='w')
        h5xs = fh5.create_group('x')
        for i, xgn in enumerate(xgns, start=1):
            x = next(xgn)
            x = _shape_check(x, with_batch=False)
            cur_len = 0
            xds = h5xs.create_dataset(f'x{i}', shape=(
                preallocated_slots, *x.shape), dtype=x.dtype, maxshape=(None, *x.shape))
            while True:
                try:
                    if cur_len >= len(xds):
                        xds.resize(
                            (len(xds) + preallocated_slots, *xds.shape[1:]))
                    xds[cur_len] = x
                    cur_len += 1
                    x = next(xgn)
                    x = _shape_check(x, with_batch=False)
                except StopIteration:
                    break
            h5xs.attrs['len'] = cur_len
            xds.resize((cur_len, *xds.shape[1:]))
        if ygns is not None:
            h5ys = fh5.create_group('y')
            for i, ygn in enumerate(ygns, start=1):
                y = next(ygn)
                y = _shape_check(y, with_batch=False)
                cur_len = 0
                yds = h5ys.create_dataset(f'y{i}', shape=(
                    preallocated_slots, *y.shape), dtype=y.dtype, maxshape=(None, *y.shape))
                while True:
                    try:
                        if cur_len >= len(yds):
                            yds.resize(
                                (len(yds) + preallocated_slots, *yds.shape[1:]))
                        yds[cur_len] = y
                        cur_len += 1
                        y = next(ygn)
                        y = _shape_check(y, with_batch=False)
                    except StopIteration:
                        break
                h5ys.attrs['len'] = cur_len
                yds.resize((cur_len, *yds.shape[1:]))
            assert h5xs.attrs['len'] == h5ys.attrs['len'], 'length of x and y is inconsistent'
    fh5.close()


# Read data from HDF5
class H5Dataset(Data.Dataset):
    def __init__(self, filename, transform_func=None):
        self.filename = filename
        self.transform_func = transform_func
        self.h5set = h5py.File(filename, mode='r')
        assert 'x' in self.h5set, 'key x is required'
        self.x_len = self.h5set['x'].attrs['len']
        self.xs_names = list(self.h5set['x'].keys())
        if 'y' in self.h5set:
            self.has_y = True
            self.y_len = self.h5set['y'].attrs['len']
            assert self.x_len == self.y_len, 'data length inconsistent!'
            self.ys_names = list(self.h5set['y'].keys())
        else:
            self.has_y = False
        self.h5set.close()
        self.xs = None

    def __len__(self):
        return self.x_len

    def __getitem__(self, index):
        if self.xs is None:
            self.h5set = h5py.File(self.filename, mode='r')
            h5xs = self.h5set['x']
            self.xs = [h5xs[name] for name in self.xs_names]
            if self.has_y:
                h5ys = self.h5set['y']
                self.ys = [h5ys[name] for name in self.ys_names]
        batch_xs = tuple((x[index] for x in self.xs))
        if self.has_y:
            batch_ys = tuple((y[index] for y in self.ys))
            if self.transform_func is None:
                return (batch_xs, batch_ys)
            return self.transform_func(batch_xs, batch_ys)
        else:
            if self.transform_func is None:
                return batch_xs
            return self.transform_func(batch_xs)

    def close(self):
        self.h5set.close()

    def get_all_data(self):
        if self.xs is None:
            self.h5set = h5py.File(self.filename, mode='r')
            h5xs = self.h5set['x']
            self.xs = [h5xs[name] for name in self.xs_names]
            if self.has_y:
                h5ys = self.h5set['y']
                self.ys = [h5ys[name] for name in self.ys_names]
        x_lst = [x[...] for x in self.xs]
        if self.has_y:
            y_lst = [y[...] for y in self.ys]
            return (x_lst, y_lst)
        return x_lst

    @classmethod
    def get_batches(cls, indices, batch_size):
        n = len(indices)
        num_batches = n // batch_size + 1
        num_sample_last_round = n % batch_size
        idx_lst = []
        for i in range(num_batches - 1):
            idx_lst.append(indices[i*batch_size:(i+1)*batch_size])
        if num_sample_last_round != 0:
            idx_lst.append(indices[-num_sample_last_round:])
        return idx_lst

    def divide(self, ratio, batch_size=100):
        '''
        ratio: dataset will be divide into two parts(tr, te) which saved to h5 files.
        For tr, size(tr) = int(allsize * ratio); for te, size(te) = allsize - size(tr).
        batch_size: size of data saved to files, in case the memory will be overflowed.
        '''
        if self.xs is None:
            self.h5set = h5py.File(self.filename, mode='r')
            h5xs = self.h5set['x']
            self.xs = [h5xs[name] for name in self.xs_names]
            if self.has_y:
                h5ys = self.h5set['y']
                self.ys = [h5ys[name] for name in self.ys_names]
        indices = np.random.permutation(np.arange(self.x_len)).tolist()
        tr_size = int(self.x_len * ratio)
        te_size = self.x_len - tr_size
        tr_filename = f'{self.filename[:-3]}_tr.h5'
        te_filename = f'{self.filename[:-3]}_te.h5'
        tr_indices = indices[:tr_size]
        te_indices = indices[tr_size:]

        tr_idx_lst = self.get_batches(tr_indices, batch_size)
        for i, idx_raw in enumerate(tr_idx_lst):
            idx = sorted(idx_raw)
            tr_xs = [x[idx] for x in self.xs]
            if self.has_y:
                tr_ys = [y[idx] for y in self.ys]
            else:
                tr_ys = None
            print(f'Processing TrSet: {i+1} / {len(tr_idx_lst)}')
            if i == 0:
                write_h5_from_arrays(tr_filename, tr_xs,
                                     tr_ys, is_appending=False)
            else:
                write_h5_from_arrays(tr_filename, tr_xs,
                                     tr_ys, is_appending=True)
        te_idx_lst = self.get_batches(te_indices, batch_size)
        for i, idx_raw in enumerate(te_idx_lst):
            idx = sorted(idx_raw)
            te_xs = [x[idx] for x in self.xs]
            if self.has_y:
                te_ys = [y[idx] for y in self.ys]
            else:
                te_ys = None
            print(f'Processing TeSet: {i+1} / {len(te_idx_lst)}')
            if i == 0:
                write_h5_from_arrays(te_filename, te_xs,
                                     te_ys, is_appending=False)
            else:
                write_h5_from_arrays(te_filename, te_xs,
                                     te_ys, is_appending=True)


class InfiniteRandomSampler(Data.Sampler):
    r"""Infinitely Samples elements randomly. 

    Arguments:
        data_source (Dataset): dataset to sample from
    """

    def __init__(self, data_source):
        self.data_source = data_source

    @classmethod
    def get_generator(cls, n):
        iterator = iter(torch.randperm(n).tolist())
        while True:
            try:
                yield next(iterator)
            except StopIteration:
                iterator = iter(torch.randperm(n).tolist())
                yield next(iterator)

    @classmethod
    def get_generator_from_lst(cls, lst):
        np.random.shuffle(lst)
        iterator = iter(lst)
        while True:
            try:
                yield next(iterator)
            except StopIteration:
                np.random.shuffle(lst)
                iterator = iter(lst)
                yield next(iterator)

    def __iter__(self):
        n = len(self.data_source)
        return self.get_generator(n)


class ClsH5Dataset(Data.Dataset):
    def __init__(self, filename, transform_func=None):
        self.filename = filename
        self.transform_func = transform_func
        self.fh5 = h5py.File(filename, mode='r')
        self.classes = self.fh5.attrs['classes'].tolist()
        self.lens = self.fh5.attrs['lens'].tolist()
        self.dt_cls_len = {c: l for (c, l) in zip(self.classes, self.lens)}
        self.xs_names = list(self.fh5[f'c{self.classes[0]}']['x'].keys())
        if 'y' in self.fh5[f'c{self.classes[0]}']:
            self.has_y = True
            self.ys_names = list(self.fh5[f'c{self.classes[0]}']['y'].keys())
        else:
            self.has_y = False
        self.fh5.close()
        self.file_opened = False

    def __len__(self):
        return np.sum(self.lens)

    def __getitem__(self, indices):
        '''
        indices: ([c0, i0], [c1, i1]...)
        '''
        if not self.file_opened:
            self.fh5 = h5py.File(self.filename, mode='r')
            self.file_opened = True
        grouped = True
        if type(indices[0]) not in (tuple, list):
            grouped = False
        if grouped:
            batch_xs = []
            for name in self.xs_names:
                xs = [self.fh5[f'c{c}']['x'][name][i][None]
                      for (c, i) in indices]
                batch_xs.append(np.concatenate(xs, axis=0))
        else:
            batch_xs = [self.fh5[f'c{indices[0]}']['x']
                        [name][indices[1]] for name in self.xs_names]
        batch_xs = tuple(batch_xs)
        if self.has_y:
            if grouped:
                batch_ys = []
                for name in self.ys_names:
                    ys = [self.fh5[f'c{c}']['y'][name]
                          [i][None] for (c, i) in indices]
                    batch_ys.append(np.concatenate(ys, axis=0))
            else:
                batch_ys = [self.fh5[f'c{indices[0]}']['y']
                            [name][indices[1]] for name in self.ys_names]
            batch_ys = tuple(batch_ys)
            if self.transform_func is None:
                return (batch_xs, batch_ys)
            return self.transform_func(batch_xs, batch_ys)
        else:
            if self.transform_func is None:
                return batch_xs
            return self.transform_func(batch_xs)

    def close(self):
        self.fh5.close()

    def get_all_data(self, selected_classes=None, use_class_mode=True):
        if selected_classes is None:
            selected_classes = self.classes
        if not self.file_opened:
            self.fh5 = h5py.File(self.filename, mode='r')
            self.file_opened = True
        if use_class_mode:
            dt_x = dict.fromkeys(selected_classes)
            dt_y = dict.fromkeys(selected_classes)
            for c in dt_x:
                dt_x[c] = [self.fh5[f'c{c}']['x'][name][...]
                           for name in self.xs_names]
            if self.has_y:
                for c in dt_y:
                    dt_y[c] = [self.fh5[f'c{c}']['y'][name][...]
                               for name in self.ys_names]
                return dt_x, dt_y
            return dt_x
        else:
            xs = [np.concatenate([self.fh5[f'c{c}']['x'][name][...]
                                  for c in selected_classes], axis=0) for name in self.xs_names]
            if self.has_y:
                ys = [np.concatenate(
                    [self.fh5[f'c{c}']['y'][name][...] for c in selected_classes], axis=0) for name in self.ys_names]
                return xs, ys
            return xs

    def divide_by_classes(self, suffix, batch_size=100, selected_classes=None):
        filename = f'{self.filename[:-3]}_{suffix}.h5'
        if selected_classes is None:
            selected_classes = self.classes
        if not self.file_opened:
            self.fh5 = h5py.File(self.filename, mode='r')
            self.file_opened = True
        for i, c in enumerate(selected_classes):
            xs = [self.fh5[f'c{c}']['x'][name] for name in self.xs_names]
            if self.has_y:
                ys = [self.fh5[f'c{c}']['y'][name] for name in self.ys_names]
            indices = np.arange(self.dt_cls_len[c]).tolist()
            idx_lst = H5Dataset.get_batches(indices, batch_size)
            for j, idx in enumerate(idx_lst):
                out_xs = [x[idx] for x in xs]
                if self.has_y:
                    out_ys = [y[idx] for y in ys]
                else:
                    out_ys = None
                dt = {c: [out_xs, out_ys]}
                print(
                    f'Processing Class {c}: {j+1}/{len(idx_lst)} | {i+1}/{len(selected_classes)}')
                if (i == 0) and (j == 0):
                    write_classified_h5_from_arrays(
                        filename, dt, is_appending=False)
                else:
                    write_classified_h5_from_arrays(
                        filename, dt, is_appending=True)

    def divide(self, ratio, batch_size=100):
        if not self.file_opened:
            self.fh5 = h5py.File(self.filename, mode='r')
            self.file_opened = True
        tr_filename = f'{self.filename[:-3]}_tr.h5'
        te_filename = f'{self.filename[:-3]}_te.h5'
        for i, c in enumerate(self.classes):
            indices = np.random.permutation(np.arange(self.lens[i])).tolist()
            tr_size = int(self.lens[i] * ratio)
            te_size = self.lens[i] - tr_size
            tr_indices = indices[:tr_size]
            te_indices = indices[tr_size:]
            tr_idx_lst = H5Dataset.get_batches(tr_indices, batch_size)
            for j, idx_raw in enumerate(tr_idx_lst):
                idx = sorted(idx_raw)
                tr_xs = [self.fh5[f'c{c}']['x'][name][idx]
                         for name in self.xs_names]
                if self.has_y:
                    tr_ys = [self.fh5[f'c{c}']['y'][name][idx]
                             for name in self.ys_names]
                else:
                    tr_ys = None
                dt = {c: [tr_xs, tr_ys]}
                print(
                    f'Processing TrSet: {j+1}/{len(tr_idx_lst)} | {i+1}/{len(self.classes)}')
                if (i == 0) and (j == 0):
                    write_classified_h5_from_arrays(
                        tr_filename, dt, is_appending=False)
                else:
                    write_classified_h5_from_arrays(
                        tr_filename, dt, is_appending=True)
            te_idx_lst = H5Dataset.get_batches(te_indices, batch_size)
            for j, idx_raw in enumerate(te_idx_lst):
                idx = sorted(idx_raw)
                te_xs = [self.fh5[f'c{c}']['x'][name][idx]
                         for name in self.xs_names]
                if self.has_y:
                    te_ys = [self.fh5[f'c{c}']['y'][name][idx]
                             for name in self.ys_names]
                else:
                    te_ys = None
                dt = {c: [te_xs, te_ys]}
                print(
                    f'Processing TeSet: {j+1}/{len(te_idx_lst)} | {i+1}/{len(self.classes)}')
                if (i == 0) and (j == 0):
                    write_classified_h5_from_arrays(
                        te_filename, dt, is_appending=False)
                else:
                    write_classified_h5_from_arrays(
                        te_filename, dt, is_appending=True)


class ClsBalancingSampler(Data.Sampler):
    def __init__(self, data_source: ClsH5Dataset, batch_size_per_class, selected_classes=None):
        self.data_source = data_source
        self.batch_size_per_class = batch_size_per_class
        if selected_classes is None:
            self.classes = data_source.classes
        else:
            self.classes = selected_classes
        self.batch_size = self.batch_size_per_class * len(self.classes)
        self.dt_cls_len = data_source.dt_cls_len
        self.lens = [self.dt_cls_len[c] for c in self.classes]
        self.len = max(self.lens)

    def __iter__(self):
        povit_index = np.argmax(self.lens)
        iterators = [iter(torch.randperm(self.lens[i]).tolist(
        )) if i == povit_index else InfiniteRandomSampler.get_generator(self.lens[i]) for i in range(len(self.lens))]
        batch = []
        for indices in zip(*iterators):
            batch.extend([(c, idx) for (c, idx) in zip(self.classes, indices)])
            if len(batch) >= self.batch_size:
                yield batch
                batch = []
        if len(batch) > 0:
            yield batch


class ClsFewShotSampler(Data.Sampler):
    def __init__(self, data_source: ClsH5Dataset, batch_size, shots=1, ways=None):
        '''
        shots: number of data per class,
        ways: classes per dataset, (default `None` means all classes, this sampler will become balancing sampler)
        '''
        self.data_source = data_source
        self.batch_size = batch_size
        self.shots = shots
        self.ways = ways
        self.classes = data_source.classes
        self.lens = data_source.lens

    def __iter__(self):
        iterators = [
            InfiniteRandomSampler.get_generator(n) for n in self.lens]
        batch = []
        while True:
            if self.ways is None:
                cur_classes = self.classes
            else:
                cur_classes = np.random.choice(
                    self.classes, self.ways, replace=False).tolist()
            selected_indices = []
            for _ in range(self.shots):
                indices = next(zip(*iterators))
                labeled_indices = {
                    c: i for (c, i) in zip(self.classes, indices)}
                selected_indices.extend(
                    [(c, labeled_indices[c]) for c in cur_classes])
            batch.append(selected_indices)
            if len(batch) == self.batch_size:
                yield batch
                batch = []

class ClsFewShotSequencer(Data.Sampler):
    def __init__(self, data_source: ClsH5Dataset, batch_size, shots=1, selected_classes=None):
        self.data_source = data_source
        self.batch_size = batch_size
        self.shots = shots
        if selected_classes is None:
            self.classes = data_source.classes
        else:
            self.classes = selected_classes
        self.dt_cls_len = data_source.dt_cls_len
        self.lens = [self.dt_cls_len[c] for c in self.classes]
        self.max_len = min(self.lens)
        self.num_shots = self.max_len // shots
        assert self.num_shots >= 1, 'Too few samples'

    def __iter__(self):
        iterators = iter(range(self.max_len))
        batch = []
        for _ in range(self.num_shots):
            selected_indices = []
            for _ in range(self.shots):
                idx = next(iterators)
                selected_indices.extend([(c, idx) for c in self.classes])
            batch.append(selected_indices)
            if len(batch) == self.batch_size:
                yield batch
                batch = []
        if len(batch) > 0:
            yield batch


class ClsSampler(Data.Sampler):
    def __init__(self, data_source: ClsH5Dataset, batch_size, selected_classes=None, infinite=False, shuffle=True):
        self.data_source = data_source
        self.batch_size = batch_size
        if selected_classes is None:
            self.classes = data_source.classes
        else:
            self.classes = selected_classes
        self.infinite = infinite
        self.shuffle = shuffle
        self.dt_cls_len = data_source.dt_cls_len
        self.lens = [self.dt_cls_len[c] for c in self.classes]
        self.len = np.sum(self.lens)

    @classmethod
    def get_comb(cls, classes, lens, shuffle):
        lst = []
        for (c, l) in zip(classes, lens):
            lst.extend([(c, i) for i in range(l)])
        if shuffle:
            np.random.shuffle(lst)
        return lst

    def __len__(self):
        return self.len

    def __iter__(self):
        if self.infinite:
            iterator = self.infinite_iterator()
        else:
            iterator = self.finite_iterator()
        for batch in iterator:
            yield batch

    def finite_iterator(self):
        iterator = iter(self.get_comb(self.classes, self.lens, self.shuffle))
        batch = []
        for idx in iterator:
            batch.append(idx)
            if len(batch) == self.batch_size:
                yield batch
                batch = []
        if len(batch) > 0:
            yield batch

    def infinite_iterator(self):
        iterator = InfiniteRandomSampler.get_generator_from_lst(
            self.get_comb(self.classes, self.lens, self.shuffle))
        batch = []
        while True:
            idx = next(iterator)
            batch.append(idx)
            if len(batch) == self.batch_size:
                yield batch
                batch = []


class DataReader:
    def __init__(self, filename, transform_func=None, num_workers=1):
        self.filename = filename
        self.transform_func = transform_func
        self.num_workers = num_workers
        fh5 = h5py.File(filename, mode='r')
        if 'x' in fh5:
            self.data_source = H5Dataset(self.filename, self.transform_func)
        else:
            self.data_source = ClsH5Dataset(
                self.filename, transform_func=self.transform_func)
        fh5.close()

    def common_reader(self, batch_size, infinite=False, shuffle=True):
        if infinite:
            steps_per_epoch = -1
            sampler = Data.BatchSampler(InfiniteRandomSampler(
                self.data_source), batch_size, False)
            dataset_loader = Data.DataLoader(
                self.data_source, batch_sampler=sampler, num_workers=self.num_workers)
        else:
            steps_per_epoch = int(np.ceil(len(self.data_source) / batch_size))
            dataset_loader = Data.DataLoader(
                self.data_source, batch_size=batch_size, shuffle=shuffle, num_workers=self.num_workers)
        return dataset_loader, steps_per_epoch

    def common_cls_reader(self, batch_size, selected_classes=None, infinite=False, shuffle=True):
        sampler = ClsSampler(self.data_source, batch_size,
                             selected_classes, infinite, shuffle)
        if infinite:
            steps_per_epoch = -1
        else:
            steps_per_epoch = int(np.ceil(len(sampler) / batch_size))
        dataset_loader = Data.DataLoader(
            self.data_source, batch_sampler=sampler, num_workers=self.num_workers)
        return dataset_loader, steps_per_epoch

    def balancing_reader(self, batch_size_per_class, selected_classes=None):
        sampler = ClsBalancingSampler(
            self.data_source, batch_size_per_class, selected_classes)
        steps_per_epoch = int(np.ceil(sampler.len / batch_size_per_class))
        dataset_loader = Data.DataLoader(
            self.data_source, batch_sampler=sampler, num_workers=self.num_workers)
        return dataset_loader, steps_per_epoch

    def few_shot_reader(self, batch_size, shots=1, ways=None):
        steps_per_epoch = -1
        sampler = ClsFewShotSampler(self.data_source, batch_size, shots, ways)
        dataset_loader = Data.DataLoader(
            self.data_source, batch_sampler=sampler, num_workers=self.num_workers)
        return dataset_loader, steps_per_epoch

    def few_shot_seq_reader(self, batch_size, shots=1, selected_classes=None):
        sampler = ClsFewShotSequencer(
            self.data_source, batch_size, shots, selected_classes)
        steps_per_epoch = int(np.ceil(sampler.num_shots / batch_size))
        dataset_loader = Data.DataLoader(
            self.data_source, batch_sampler=sampler, num_workers=self.num_workers)
        return dataset_loader, steps_per_epoch
