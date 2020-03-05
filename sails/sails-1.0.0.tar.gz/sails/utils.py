#!/usr/bin/python

# vim: set expandtab ts=4 sw=4:

import math
import numpy as np
from scipy import signal, stats

__all__ = []


def fast_resample(X, ds_factor, axis=1):
    """Fast resampling of a timeseries array. This function pads the
    time-dimension to the nearest power of 2 to ensure that the resampling can
    use efficient FFT routines. The padding is removed before the downsampled
    data are returned.

    Parameters
    ----------
    X : ndarray
        Data to be resampled

    ds_factor : float
        Factor of downsampling to apply. Output sample rate will be sample_rate/ds_factor

    axis : int
        Axis along which to perform resampling.  Defaults to 1 for compatibility reasons

    Returns
    -------
    ndarray
        Resampled dataset, of size [nchannels x nsamples]

    """

    orig_size = X.shape[axis]
    target_size = int(X.shape[axis] // ds_factor)

    tmp_size = int(2**math.ceil(math.log(X.shape[axis], 2)))
    tmp_target_size = int(tmp_size // ds_factor)

    # We zero-pad the data in the time dimension up to the temporary size
    # Start by creating an array of appropriate shape
    new_shape = list(X.shape)
    new_shape[axis] = tmp_size

    tmp_X = np.zeros(new_shape, dtype=X.dtype)

    # Now we copy the data into the relevant part of the temporary array
    slic = [slice(None)] * len(X.shape)
    slic[axis] = slice(0, orig_size)
    slic = tuple(slic)

    tmp_X[slic] = X

    # Finally, we resample along the relevant axis
    resampled_X = signal.resample(tmp_X, tmp_target_size, axis=axis)

    # And extract just the parts we want
    slic = [slice(None)] * len(X.shape)
    slic[axis] = slice(0, target_size)
    slic = tuple(slic)

    return resampled_X[slic]


__all__.append('fast_resample')


def get_valid_samples(data, delay_vect, mode='valid', backwards=False):
    """
    Helper function for excluding or replacing data samples which are not
    preceded by a full delay vect of samples for prediction.

    Parameters
    ----------
    data : ndarray
        Array of data to trim or change, of size [nchannels x nsamples x ntrials]
    delay_vect : ndarray
        Vector of lags included in model
    mode : {'valid','full_nan','full'}
        Options for excluding or replacing residuals which do not have a full
        model prediction ie the third sample of an order 5 model. 'valid'
        removes samples without a full model prediction, 'full_nan' returns
        resids of the same size as the data with nans replacing excluded
        samples and 'full' returns resids keeping non-full model samples in
        place. (Default is 'valid')
    backwards : Boolean
        Flag indicating whether to edit the first or last samples

    Returns
    -------
    ndarray
        data with non-valid samples removed or replaced with nans

    """

    if mode == 'full':
        # just pass through
        return data

    # Don't work in place
    ret = data.copy()

    if mode == 'valid':
        if backwards:
            ret = ret[:, :-len(delay_vect), :]
        else:
            ret = ret[:, len(delay_vect):, :]

    elif mode == 'full_nan':
        if backwards:
            ret[:, -len(delay_vect):, :] = np.nan
        else:
            ret[:, :len(delay_vect), :] = np.nan

    else:
        raise ValueError("Residual return mode is not recognised, please use \
                          'valid', 'full_nan' or 'full'")

    return ret


__all__.append('get_valid_samples')


def gesd(x, alpha=0.05, p_out=.1, outlier_side=0):
    """Detect outliers using Generalized ESD test

     Parameters
     ----------
     x : vector
        Data set containing outliers
     alpha : scalar
        Significance level to detect at (default = 0.05)
     p_out : int
        Maximum number of outliers to detect (default = 10% of data set)
     outlier_side : {-1,0,1}
        Specify sidedness of the test
           - outlier_side = -1 -> outliers are all smaller
           - outlier_side = 0  -> outliers could be small/negative or large/positive (default)
           - outlier_side = 1  -> outliers are all larger

    Returns
    -------
    idx : boolean vector
        Boolean array with TRUE wherever a sample is an outlier
    x2 : vector
        Input array with outliers removed

    References
    ----------
    B. Rosner (1983). Percentage Points for a Generalized ESD Many-Outlier Procedure. Technometrics 25(2), pp. 165-172.
    http://www.jstor.org/stable/1268549?seq=1

    """

    if outlier_side == 0:
        alpha = alpha/2

    if not isinstance(x, np.ndarray):
        x = np.asarray(x)

    n_out = int(np.ceil(len(x)*p_out))

    if np.any(np.isnan(x)):
        # Need to find outliers only in finite x
        y = np.where(np.isnan(x))[0]
        idx1, x2 = gesd(x[np.isfinite(x)], alpha, n_out, outlier_side)

        # idx1 has the indexes of y which were marked as outliers
        # the value of y contains the corresponding indexes of x that are outliers
        idx = np.zeros_like(x).astype(bool)
        idx[y[idx1]] = True

    n = len(x)
    temp = x.copy()
    R = np.zeros((n_out,))
    rm_idx = np.zeros((n_out,), dtype=int)
    lam = np.zeros((n_out,))

    for j in range(0, int(n_out)):
        i = j+1
        if outlier_side == -1:
            rm_idx[j] = np.nanargmin(temp)
            sample = np.nanmin(temp)
            R[j] = np.nanmean(temp) - sample
        elif outlier_side == 0:
            rm_idx[j] = int(np.nanargmax(abs(temp-np.nanmean(temp))))
            R[j] = np.nanmax(abs(temp-np.nanmean(temp)))
        elif outlier_side == 1:
            rm_idx[j] = np.nanargmax(temp)
            sample = np.nanmax(temp)
            R[j] = sample - np.nanmean(temp)

        R[j] = R[j] / np.nanstd(temp)
        temp[int(rm_idx[j])] = np.nan

        p = 1-alpha/(n-i+1)
        t = stats.t.ppf(p, n-i-1)
        lam[j] = ((n-i) * t) / (np.sqrt((n-i-1+t**2)*(n-i+1)))

    # Create a boolean array of outliers
    idx = np.zeros((n,)).astype(bool)
    idx[rm_idx[np.where(R > lam)[0]]] = True

    x2 = x[~idx]

    return idx, x2


def detect_artefacts(X, reject_dim='channels', reject_metric='std',
                     segment_len=100, gesd_args=None, ret_mode='bad_inds'):
    """Detect bad channels or segments in M/EEG data

    Parameters
    ----------
    X : ndarray
        Array of size [channels x samples] or [channels x samples x trials] to
        find artefacts in.
    reject_dim : {'channels','samples','trials'}
        Flag indicating whether bad samples will be detected in the channels,
        samples or trials (Default is 'channels')
    reject_metric : {'std','var'}
        Flag indicating which summary measure will be used to detect artefacts
    segement_len : int > 0
        Integer window length of dummy epochs for bad_segment detection
    gesd_args : dict
        Dictionary of arguments to pass to gesd
    ret_mode : {'good_inds','bad_inds',clean_data','nan_data'}
        Flag indicating whether to return the indices for good observations,
        indices for bad observations (default), the input data with outliers
        removed (clean_data) or the input data with outliers replaced with nans

    Returns
    -------
    ndarray
        array of input siz with artefacts set to nan
    bad_inds : ndarray
        Optional output containing indices to outliers

    """

    # Housekeeeping
    if reject_dim not in ['channels', 'samples', 'trials']:
        raise ValueError("'reject_dim':{0} not recognised - please use \
        'channels', 'samples' or 'trials'".format(reject_dim))

    if reject_metric not in ['std', 'var']:
        raise ValueError("'reject_metric':{0} not recognised - please use \
        'std' or 'var'".format(reject_dim))

    # Add a dummy trial if none are passed
    if X.ndim == 2:
        X = X[:, :, None]

    if gesd_args is None:
        # Not sure if this is necessary - can you explode a None?
        gesd_args = {'alpha': .05}

    # Preprocessing
    if (reject_dim == 'channels') and (reject_metric == 'std'):
        X2 = X.std(axis=(1, 2))
    elif (reject_dim == 'channels') and (reject_metric == 'var'):
        X2 = X.var(axis=(1, 2))

    if (reject_dim == 'trials') and (reject_metric == 'std'):
        X2 = X.std(axis=(0, 1))
    elif (reject_dim == 'trials') and (reject_metric == 'var'):
        X2 = X.var(axis=(0, 1))

    elif reject_dim == 'samples':
        if reject_metric == 'std':
            X2 = X.std(axis=(0, 2))
        elif reject_metric == 'var':
            X2 = X.var(axis=(0, 2))

        # Apply dummy epochs
        nsegs = np.ceil(X2.shape[0] / segment_len).astype(int)
        if nsegs*segment_len > X2.shape[0]:
            X2 = np.r_[X2, np.zeros(((nsegs*segment_len)-X2.shape[0],))]

        X2 = X2.reshape(nsegs, segment_len).mean(axis=1)  # average of variances within segment
        seginds = np.repeat(np.arange(X2.shape[0]), segment_len)

    # Rejection
    rm_ind, _ = gesd(X2, **gesd_args)

    # Returns based on user options
    if ret_mode == 'bad_inds':
        # Return inds to bad observations
        bads = np.where(rm_ind)[0]
        if reject_dim == 'samples':
            return np.where(np.in1d(seginds, bads))[0]
        else:
            return bads

    elif ret_mode == 'good_inds':
        # Return inds to good observations
        tmp = np.ones_like(X2).astype(bool)
        tmp[rm_ind] = False
        goods = np.where(tmp)[0]
        if reject_dim == 'samples':
            print('hi')
            return np.where(np.in1d(seginds, goods))[0]
        else:
            return goods

    elif ret_mode == 'clean_data':
        # Remove bad dims altogether
        tmp = np.ones_like(X2).astype(bool)
        tmp[rm_ind] = False
        goods = np.where(tmp)[0]

        out = X.copy()  # Don't work in place
        if reject_dim == 'channels':
            out = out[goods, :, :]
        elif reject_dim == 'samples':
            keep_ind = np.where(np.in1d(seginds, goods))[0]
            out = out[:, keep_ind, :]
        elif reject_dim == 'trials':
            out = out[:, :, goods]
        return out

    elif ret_mode == 'nan_data':
        # Replace data in bad dims with nans
        bads = np.where(rm_ind)[0]
        out = X.copy()  # Don't work in place
        if reject_dim == 'channels':
            out[rm_ind, :, :] = np.nan
        elif reject_dim == 'samples':
            rm_ind = np.where(np.in1d(seginds, bads))[0]
            out[:, rm_ind, :] = np.nan
        elif reject_dim == 'trials':
            out[:, :, rm_ind]
        return out
