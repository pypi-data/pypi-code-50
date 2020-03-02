import os
import numpy as np
import unittest
from datetime import datetime
from pynwb import NWBHDF5IO, NWBFile
from pynwb.device import Device
from pynwb.ophys import OpticalChannel
from ndx_fret import FRET, FRETSeries


class FRETTest(unittest.TestCase):

    def setUp(self):
        self.nwbfile = NWBFile('description', 'id', datetime.now().astimezone())

    def test_add_fretseries(self):
        # Create and add device
        device = Device(name='Device')
        self.nwbfile.add_device(device)

        # Create optical channels
        opt_ch_d = OpticalChannel(
            name='optical_channel',
            description='optical_channel_description',
            emission_lambda=529.
        )
        opt_ch_a = OpticalChannel(
            name='optical_channel',
            description='optical_channel_description',
            emission_lambda=633.
        )

        # Create FRET
        fs_d = FRETSeries(
            name='donor',
            fluorophore='mCitrine',
            optical_channel=opt_ch_d,
            device=device,
            description='description of donor series',
            data=np.random.randn(100, 10, 10),
            rate=200.,
        )
        fs_a = FRETSeries(
            name='acceptor',
            fluorophore='mKate2',
            optical_channel=opt_ch_a,
            device=device,
            description='description of acceptor series',
            data=np.random.randn(100, 10, 10),
            rate=200.,
        )

        fret = FRET(
            name='FRET',
            excitation_lambda=482.,
            donor=fs_d,
            acceptor=fs_a
        )
        self.nwbfile.add_acquisition(fret)

        filename = 'test_fret.nwb'

        with NWBHDF5IO(filename, 'w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(filename, mode='r') as io:
            io.read()

        os.remove(filename)
