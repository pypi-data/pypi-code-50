# -*- coding: utf-8 -*-
#
# This file is part of SIDEKIT.
#
# SIDEKIT is a python package for speaker verification.
# Home page: http://www-lium.univ-lemans.fr/sidekit/
#
# SIDEKIT is a python package for speaker verification.
# Home page: http://www-lium.univ-lemans.fr/sidekit/
#
# SIDEKIT is free software: you can redistribute it and/or modify
# it under the terms of the GNU LLesser General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# SIDEKIT is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with SIDEKIT.  If not, see <http://www.gnu.org/licenses/>.

"""
Copyright 2014-2020 Anthony Larcher
"""

import logging
import numpy
import torch
import pandas
import soundfile
import random
import h5py
import torch.optim as optim
import torch.multiprocessing as mp
from torchvision import transforms
from torch.utils.data import DataLoader
from pathlib import Path
from tqdm import tqdm
from torch.utils.data import Dataset


__license__ = "LGPL"
__author__ = "Anthony Larcher"
__copyright__ = "Copyright 2015-2020 Anthony Larcher"
__maintainer__ = "Anthony Larcher"
__email__ = "anthony.larcher@univ-lemans.fr"
__status__ = "Production"
__docformat__ = 'reS'


"""
How to use:

vs = ds.Vox1Set("/lium/raid01_c/larcher/vox1_raw_wav_batches.h5", transform=transforms.Compose([PreEmphasis(),]))
vloader = DataLoader(vs, batch_size=32, shuffle=True, num_workers=5)
"""



def prepare_voxceleb1(vox1_root_dir, output_batch_file, seg_duration=4, samplerate=16000):

    # List wav files in VoxCeleb1
    vox1_wav_list = [str(f) for f in list(Path(vox1_root_dir).rglob("*.[wW][aA][vV]"))]
    vox1_df = pandas.DataFrame(columns=("database", "speaker_id", "file_id", "duration", "speaker_idx"))

    print("*** Collect information from VoxCeleb1 data ***")
    for fn in tqdm(vox1_wav_list):
        file_id = ('/').join(fn.split('/')[-2:]).split('.')[0]
        speaker_id = fn.split('/')[-3]
        _set = fn.split('/')[-5]

        # get the duration of the wav file
        data, _ = soundfile.read(fn)
        duration = data.shape[0]

        vox1_df = vox1_df.append(
            {"database": "vox1", "speaker_id": speaker_id, "file_id": file_id, "duration": duration, "speaker_idx": -1,
             "set": _set}, ignore_index=True)

    print("\n\n*** Create a single HDF5 file with all training data ***")

    # Create a HDF5 file and fill it with one 4s segment per session
    with h5py.File(output_batch_file, 'w') as fh:
        for index, row in tqdm(vox1_df.iterrows()):

            session_id = row['speaker_id'] + '/' + row['file_id']

            # Load the wav signal
            fn = '/'.join((vox1_root_dir, row['set'], 'wav', session_id)) + ".wav"
            data, samplerate = soundfile.read(fn, dtype='int16')
            _nb_samp = len(data)

            # Randomly select a segment of "duration" if it's long enough
            if _nb_samp > nb_samp:
                cut = numpy.random.randint(low = 0, high = _nb_samp - nb_samp)

                # Write the segment in the HDF5 file
                fh.create_dataset(session_id,
                                  data=data[cut:cut+nb_samp].astype('int16'),
                                  maxshape=(None,),
                                  fletcher32=True)


class PreEmphasis(object):
    """
    Perform pre-emphasis filtering on audio segment
    """
    def __init__(self, pre_emp_value=0.97):
        self.pre_emp_value = pre_emp_value

    def __call__(self, sample):
        data = numpy.asarray(sample[0][1:] - 0.97 * sample[0][:-1], dtype=numpy.float32)
        return data, sample[1]


class Vox1Set(Dataset):
    """
    Object creates a dataset for VoxCeleb
    """

    def __init__(self, voxceleb1_file, speaker_list=None, transform=None):
        """

        :param voxceleb1_file: HDF5 file containing data from Voxceleb1
        :param speaker_list:  list of speaker top use for training
        :param transform: list of transformation to apply
        """
        self.transform = transform
        self.voxceleb1_file = voxceleb1_file
        with h5py.File(voxceleb1_file, 'r') as fh:
            speaker_ids = list(fh.keys())

            # Filter speaker according to the input list
            if speaker_list is not None:
                speaker_ids = [l for l in speaker_ids if l in speaker_list]

            # Create a dictionary of speaker
            speaker_ids.sort()
            self.speaker_idx = {key: val for val, key in enumerate(speaker_ids)}

            l2 = []
            for l in speaker_ids:
                for k in list(fh[l].keys()):
                    l2.append('/'.join((l, k)))
            segment_list = []
            for l in l2:
                for k in list(fh[l].keys()):
                    segment_list.append('/'.join((l, k)))
            self.segment_list = segment_list
            self.len = len(self.segment_list)

    def __getitem__(self, index):
        with h5py.File(self.voxceleb1_file, 'r') as fh:
            speaker_idx = self.speaker_idx[self.segment_list[index].split('/')[0]]
            data_pcm16 = fh[self.segment_list[index]][()]
            data_float32 = data_pcm16.astype(numpy.float32) / 32768.
            if self.transform:
                data_float32, speaker_idx = self.transform((data_float32, speaker_idx))
            return data_float32, speaker_idx

    def __len__(self):
        return self.len