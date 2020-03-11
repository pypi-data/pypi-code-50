""" Provides Crawler and DateRange classes as well as locate_mat function

The Crawler class provides functionality for locating and evaluating large
ranges of lf data in a single class.
The DateRange class allows iterating through dates at various time intervals.
locate_mat determines the file paths for the .mat files correesponding to a
single path on a single day.
"""

import os
import lf.txrx
import lf.data
from datetime import datetime, timedelta


class Crawler(object):

    """ Data crawler to sift through all the LF data"""

    def __init__(
        self,
        data_path,
        start,
        stop=datetime.today(),
        txs=["NAA", "NML", "NLK"],
        rxs=["AR", "BD", "BX", "BW", "LP", "DA", "OX"],
        config=None,
    ):
        """ Initialize the date range and paths to check

        Parameters
        ----------
        data_path : str
            Path to receiver data
        start : datetime
            Start date of interest range
        stop : datetime, optional
            Stop date of interest range
        txs : list of str, optional
            List containing the transmitters of interest
        rxs : list of str, optional
            List containing the receivers of interest

        """
        self._data_path = data_path
        if not os.path.isdir(os.path.expanduser(data_path)):
            raise OSError("Directory does not exist!")
        self._start = start
        self._stop = stop
        self._txs = txs
        self._rxs = rxs
        self._config = config

    def crawl(self, step=timedelta(days=1), resolution="low", plot=False):
        """ Sift through LF Data

        Parameters
        ----------
        step : timedelta, optional
            How much time to increment between checks
        resolution : {"low", "high"}, optional
            Data resolution of interest
        plot : bool
            Flag to plot data for each path, useful for debugging

        Returns
        -------
        None

        """
        self.paths = {}
        for day in DateRange(self._start, self._stop, step):
            self.paths[day] = {}
            for tx in self._txs:
                self.paths[day][tx] = []
                for rx in self._rxs:
                    mats = locate_mat(self._data_path, day, tx, rx, resolution)
                    if mats is not None:
                        data = lf.data.rx.LFData(mat_files=mats)
                        qual = lf.data.rxquality.EvalLF(data, self._config)
                        print()
                        print(
                            f"Evaluating {tx}-{rx} on {day.strftime('%b %d, %Y')}"
                        )
                        qual.eval_amp()
                        qual.eval_phase()
                        qual.eval_receiver()
                        if qual.quality.get_quality():
                            print(f"Data is Good!")
                            self.paths[day][tx].append(rx)
                        else:
                            print(f"Data is Bad!")
                        if plot:
                            data.plot()


class DateRange:

    """ Iterator that increments dates"""

    def __init__(self, start, stop=datetime.today(), step=timedelta(days=1)):
        """ Iterate from start date to stop date with time step delta

        Parameters
        ----------
        start : datetime
            Oldest time of interest
        stop : datetime, optional
            Newest time of interest (inclusive)
        step : timedelta, optional
            How much to increment in each loop

        """

        self._date = start
        self._stop = stop
        self._step = step

    def __iter__(self):
        """ Iterator
        Returns
        -------
        DateRange
            returns itself

        """
        return self

    def __next__(self):
        """ Calculate next date

        Returns
        -------
        datetime
            Current time plus step

        """
        date = self._date
        self._date += self._step
        if date > self._stop:
            raise StopIteration
        else:
            return date


def locate_mat(data_path, date, tx, rx, resolution):
    """ Determine the two mat_files associated with the provided Tx-Rx Path

    Parameters
    ----------
    data_path : str
        Path to the data directory containing folders for each receiver
    date : datetime
        Date of interest
    tx : {"NAA", "NLK", "NML"}
        Transmitter of interest
    rx : str
        Receiver of interest
    resolution : {"high", "low"}
        high resolution = 60 Hz, low resolution = 1 Hz

    Returns
    -------
    list of str
        list containig the amplitude and phase .mat files of interest

    """
    if resolution.lower() == "low":
        amp, phase = "A", "B"
    elif resolution.lower() == "high":
        amp, phase = "C", "D"
    else:
        raise ValueError("Resolution must be high or low!")
    receiver = lf.txrx.site_mapping[rx.upper()]
    date_str = date.strftime("%Y_%m_%d")
    filenames = [
        os.path.join(
            os.path.expanduser(data_path),
            receiver,
            date_str,
            "".join(
                [
                    rx.upper(),
                    date.strftime("%y%m%d%H%M%S"),
                    tx.upper(),
                    "_10",
                    str(ch),
                    amp_phase,
                    ".mat",
                ]
            ),
        )
        for ch in [0, 1]
        for amp_phase in [amp, phase]
    ]
    for filename in filenames:
        if not os.path.exists(filename):
            print(
                f"Data missing from {tx}-{rx} on {date.strftime('%b %d, %Y')}"
            )
            return None
    return filenames
