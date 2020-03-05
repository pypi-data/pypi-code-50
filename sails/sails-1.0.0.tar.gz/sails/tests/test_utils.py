#!/usr/bin/python

# vim: set expandtab ts=4 sw=4:

import unittest

import numpy as np

from ..support import array_assert


class ResampleTests(unittest.TestCase):
    def test_fast_resample_int_factor(self):
        """Test that we properly resample data with an integer factor"""
        from ..utils import fast_resample

        # Create a 10Hz signal sampled at 500Hz for 2s
        t = np.linspace(0, 2-(1/1000), 1000)
        s = np.sin(2*np.pi*t*10)

        # Reformat to [nchannels, nsamples]
        s = s[np.newaxis, :]

        # Re-sample by a factor of 2 (to 250Hz)
        res = fast_resample(s, 2)

        # We should still have 20 peaks
        # Find them by looking for points where the derivative reverses sign
        diff_res = np.diff(res)[0, :]
        peaks = []
        for idx in range(1, diff_res.shape[0]):
            if diff_res[idx-1] > 0 and diff_res[idx] < 0:
                peaks.append(idx)

        assert(len(peaks) == 20)

        # And each peak should be 25 samples apart starting at sample 6
        assert(peaks[0] == 6)
        diff = np.array([peaks[x] - peaks[x-1] for x in range(1, len(peaks))])
        assert(np.sum(diff == 25) == 19)

    def test_fast_resample_alt_dim(self):
        """Test that we properly resample data with an alternate dimension"""
        from ..utils import fast_resample

        # Create a 10Hz signal sampled at 500Hz for 2s
        t = np.linspace(0, 2-(1/1000), 1000)
        s = np.sin(2*np.pi*t*10)

        # Re-sample by a factor of 2 (to 250Hz)
        res = fast_resample(s, 2, axis=0)

        # We should still have 20 peaks
        # Find them by looking for points where the derivative reverses sign
        diff_res = np.diff(res)
        peaks = []
        for idx in range(1, diff_res.shape[0]):
            if diff_res[idx-1] > 0 and diff_res[idx] < 0:
                peaks.append(idx)

        assert(len(peaks) == 20)

        # And each peak should be 25 samples apart starting at sample 6
        assert(peaks[0] == 6)
        diff = np.array([peaks[x] - peaks[x-1] for x in range(1, len(peaks))])
        assert(np.sum(diff == 25) == 19)

    def test_fast_resample_float_factor(self):
        """Test that we properly resample data with an float factor"""
        from ..utils import fast_resample

        # Create a 10Hz signal sampled at 500Hz for 2s
        t = np.linspace(0, 2-(1/1000), 1000)
        s = np.sin(2*np.pi*t*10)

        # Reformat to [nchannels, nsamples]
        s = s[np.newaxis, :]

        # Re-sample by a factor of 2.5 (to 200Hz)
        res = fast_resample(s, 2.5)

        # We should still have 20 peaks
        # Find them by looking for points where the derivative reverses sign
        diff_res = np.diff(res)[0, :]
        peaks = []
        for idx in range(1, diff_res.shape[0]):
            if diff_res[idx-1] > 0 and diff_res[idx] < 0:
                peaks.append(idx)

        assert(len(peaks) == 20)

        # And each peak should be 19 or 20 samples apart starting at sample 5
        # (there is some inevitable rounding error)
        assert(peaks[0] == 5)
        diff = np.array([peaks[x] - peaks[x-1] for x in range(1, len(peaks))])
        assert(np.sum((diff == 20) | (diff == 19)) == 19)

    def test_fast_resample_multi_dim(self):
        """Test that we properly resample data in multi dimension mode"""
        from ..utils import fast_resample

        # Create a 10Hz signal sampled at 500Hz for 2s
        t = np.linspace(0, 2-(1/1000), 1000)
        s = np.sin(2*np.pi*t*10)

        # Reformat to [nchannels, nsamples]
        s = s[:, np.newaxis, np.newaxis]

        s = np.tile(s, (1, 1, 2))

        # Re-sample by a factor of 2 (to 250Hz)
        res = fast_resample(s, 2, axis=0)

        # For each of our two copies, perform our tests
        for idx in range(2):
            test_data = res[:, 0, idx]
            # We should still have 20 peaks
            # Find them by looking for points where the derivative reverses sign
            diff_res = np.diff(test_data)
            peaks = []
            for idx in range(1, diff_res.shape[0]):
                if diff_res[idx-1] > 0 and diff_res[idx] < 0:
                    peaks.append(idx)

            assert(len(peaks) == 20)

            # And each peak should be 25 samples apart starting at sample 6
            assert(peaks[0] == 6)
            diff = np.array([peaks[x] - peaks[x-1] for x in range(1, len(peaks))])
            assert(np.sum(diff == 25) == 19)


class ValidSamplesTests(unittest.TestCase):
    def test_valid_samples(self):
        """Test that we properly compute the indices for valid samples"""
        from ..utils import get_valid_samples

        # Create some test data: 2 chans, 100 samples, 10 trials
        # Set up data as (trial_num*100) + (chan_no * 2000) + (sample_num)
        num_chans = 2
        num_samples = 100
        num_trials = 10

        data = np.zeros((num_chans, num_samples, num_trials))
        for k in range(num_chans):
            for l in range(num_trials):
                data[k, :, l] = (k * 2000) + (l * 100) + np.arange(num_samples)

        # Assume that we have an order 5 model
        delay_vect = np.arange(5 + 1)

        # Check that in the 'full' case we just get back our data
        array_assert(data, get_valid_samples(data, delay_vect, mode='full', backwards=False))
        array_assert(data, get_valid_samples(data, delay_vect, mode='full', backwards=True))

        # Check that in the 'valid' forward case, we get back our data offset by 6 samples (order + 1)
        array_assert(data[:, 6:, :],
                     get_valid_samples(data, delay_vect, mode='valid', backwards=False))

        # Check that in the 'valid' backwards case, we get back our data with 6 samples taken from
        # the end
        array_assert(data[:, :-6, :],
                     get_valid_samples(data, delay_vect, mode='valid', backwards=True))

        # Check that in the 'full_nan' forward case, we get back our data where the first 6 samples
        # are NaN
        nan_data = data.copy()
        nan_data[:, 0:6, :] = np.nan

        valid = get_valid_samples(data, delay_vect, mode='full_nan', backwards=False)
        # Check NaNs
        assert(np.sum(np.isnan(valid[:, 0:6, :])) == 120)
        # Check rest of array
        array_assert(nan_data[:, 6:, :], valid[:, 6:, ])

        # Check that in the 'full_nan' backward case, we get back our data where the last 6 samples
        # are NaN
        nan_data = data.copy()
        nan_data[:, -6:, :] = np.nan

        valid = get_valid_samples(data, delay_vect, mode='full_nan', backwards=True)
        # Check NaNs
        assert(np.sum(np.isnan(valid[:, -6:, :])) == 120)
        # Check rest of array
        array_assert(nan_data[:, :-6, :], valid[:, :-6, ])

        # Check that we raise on a bad mode
        self.assertRaises(ValueError, get_valid_samples,
                          data, delay_vect, mode='notreal', backwards=True)


class ArtefactDetectionTests(unittest.TestCase):
    def test_gesd(self):
        from ..utils import gesd
        np.random.seed(43)

        # Create some random data
        X = np.random.randn(100, 1)

        # Check that we don't detect outliers in normally distributed random
        # data
        bads, cleanX = gesd(X)
        # No bad samples
        assert(np.all(bads == False))  # noqa: E712
        # Clean data is the same as data
        assert(np.all(X == cleanX))

        # and on an outlier side -1 test
        bads, cleanX = gesd(X, outlier_side=-1)
        # No bad samples
        assert(np.all(bads == False))  # noqa: E712
        # Clean data is the same as data
        assert(np.all(X == cleanX))

        # and on an outlier side 1 test
        bads, cleanX = gesd(X, outlier_side=1)
        # No bad samples
        assert(np.all(bads == False))  # noqa: E712
        # Clean data is the same as data
        assert(np.all(X == cleanX))

        # and that we deal with passing a list
        bads, cleanX = gesd(list(X))
        # No bad samples
        assert(np.all(bads == False))  # noqa: E712
        # Clean data is the same as data
        assert(np.all(X == cleanX))

        # An an obviously bad sample
        X[50] = 10
        bads, cleanX = gesd(X)
        # Check correct sample is identified
        assert(np.where(bads == True)[0][0] == 50)  # noqa: E712
        # Bad sample is identified
        assert(cleanX.shape[0] == X.shape[0]-1)

    def test_detect_artefacts(self):
        from ..utils import detect_artefacts
        np.random.seed(43)

        # Create a dataset in sails format with 32 channels, 500 samples and
        # 128 epochs.
        X = np.random.randn(32, 500, 128)

        # Check no bad samples are found - std mode
        bad_inds = detect_artefacts(X)
        assert(len(bad_inds) == 0)

        # Check no bad samples are found - var mode
        bad_inds = detect_artefacts(X, reject_metric='var')
        assert(len(bad_inds) == 0)

        # Pass as just one trial
        # Check no bad samples are found
        bad_inds = detect_artefacts(X[:, :, 0])
        assert(len(bad_inds) == 0)

        # Add a single bad channel
        X[10, ...] *= 3

        # Make sure single bad channel is rejected
        bad_inds = detect_artefacts(X, ret_mode='good_inds')
        assert(len(bad_inds) == 31)

        # Check that good_inds option works
        bad_inds = detect_artefacts(X)
        assert(len(bad_inds) == 1)
        assert(bad_inds[0] == 10)

        # Make sure no bad trials are found
        bad_inds = detect_artefacts(X, reject_dim='trials')
        assert(len(bad_inds) == 0)

        # Make a single bad trial
        X[10, :, 32] *= 3

        # Make sure bad trial is detected
        bad_inds = detect_artefacts(X, reject_dim='trials')
        assert(len(bad_inds) == 1)
        assert(bad_inds[0] == 32)

        # Check clean data return mode
        cleanX = detect_artefacts(X, reject_dim='trials', ret_mode='clean_data')
        assert(cleanX.shape[2] == 127)

        # Make a bad segment
        X[:, 200:300, :] *= 3

        # Make sure bad segment inds are correctly identified
        bad_inds = detect_artefacts(X, reject_dim='samples', ret_mode='bad_inds')
        assert(np.all(bad_inds == np.arange(200, 300)))

        # Make sure bad segment inds are correctly identified
        nanX = detect_artefacts(X, reject_dim='samples', ret_mode='nan_data')
        assert(np.isnan(nanX[0, :, 0]).sum() == 100)

    def test_bad_params(self):
        from ..utils import detect_artefacts

        np.random.seed(43)

        # Create a dataset in sails format with 32 channels, 500 samples and
        # 128 epochs.
        X = np.random.randn(32, 500, 128)

        self.assertRaises(ValueError, detect_artefacts, X, reject_dim='unknown')

        self.assertRaises(ValueError, detect_artefacts, X, reject_metric='unknown')
