#!/usr/bin/python
#
# Copyright 2020 ToCodeForSoul
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Extensions:
  _exts = {}
  def __init__(self,exts):
    self._exts = exts
  def list(self,*argv):
    return [self._exts.get(arg) for arg in argv]
  def get(self,arg):
    return self._exts.get(arg)

class Config:
  name_pattern = '{}_Depression_REST'
  valid_events = ['1', '2', '3', '4', '5', '6', '11', '12', '13', '14', '15', '16']
  ref_channels = ['M1', 'M2']
  chs = ['FP1','FPZ','FP2','AF3','AF4','F7','F5','F3','F1','FZ','F2','F4','F6',
        'F8','FT7','FC5','FC3','FC1','FCZ','FC2','FC4','FC6','FT8','T7','C5',
        'C3','C1','CZ','C2','C4','C6','T8','M1','TP7','CP5','CP3','CP1','CPZ',
        'CP2','CP4','CP6','TP8','M2','P7','P5','P3','P1','PZ','P2','P4','P6','P8',
        'PO7','PO5','PO3','POZ','PO4','PO6','PO8','O1','OZ','O2']
  bad_channels = ['CB1', 'CB2', 'EKG', 'HEOG', 'VEOG']
  rm_baseline = (None, None)
  filter_range = None # (0.2, 50)
  ica_args = None # dict(random_state=97, max_iter=3000)
  butter_filter = None # dict(order=5, highcut=50.0, lowcut=1.0)
  exts = Extensions({
    'mat': '.mat',
    'set': '.set',
    'epo':'-epo.npy',
    'ept':'-epo-times.npy', 
    'ft1': '-epo-feat-v1.npy',
    'ft2': '-epo-feat-v2.npy'
    })
  version_codes={'ftv1':1,'ftv2':2}
  subjects = [dict(id=507,BDI=0),dict(id=508,BDI=4),dict(id=509,BDI=7),dict(id=510,BDI=1),
              dict(id=511,BDI=1),dict(id=512,BDI=1),dict(id=513,BDI=0),dict(id=514,BDI=5),
              dict(id=515,BDI=5),dict(id=516,BDI=0),dict(id=517,BDI=0),dict(id=518,BDI=1),
              dict(id=519,BDI=6),dict(id=520,BDI=3),dict(id=521,BDI=2),dict(id=522,BDI=0),
              dict(id=523,BDI=1),dict(id=524,BDI=3),dict(id=525,BDI=2),dict(id=526,BDI=0),
              dict(id=527,BDI=1),dict(id=528,BDI=1),dict(id=529,BDI=0),dict(id=530,BDI=1),
              dict(id=531,BDI=1),dict(id=532,BDI=1),dict(id=533,BDI=2),dict(id=534,BDI=5),
              dict(id=535,BDI=2),dict(id=536,BDI=2),dict(id=537,BDI=2),dict(id=538,BDI=0),
              dict(id=539,BDI=0),dict(id=540,BDI=1),dict(id=541,BDI=0),dict(id=542,BDI=0),
              dict(id=543,BDI=1),dict(id=545,BDI=0),dict(id=546,BDI=5),dict(id=547,BDI=2),
              dict(id=548,BDI=3),dict(id=549,BDI=2),dict(id=550,BDI=1),dict(id=551,BDI=2),
              dict(id=552,BDI=2),dict(id=553,BDI=4),dict(id=554,BDI=1),dict(id=555,BDI=1),
              dict(id=556,BDI=2),dict(id=557,BDI=3),dict(id=558,BDI=29),dict(id=559,BDI=25),
              dict(id=560,BDI=0),dict(id=561,BDI=27),dict(id=562,BDI=0),dict(id=563,BDI=0),
              dict(id=564,BDI=27),dict(id=565,BDI=24),dict(id=566,BDI=18),dict(id=567,BDI=24),
              dict(id=568,BDI=1),dict(id=569,BDI=28),dict(id=570,BDI=1),dict(id=573,BDI=2),
              dict(id=574,BDI=4),dict(id=575,BDI=5),dict(id=576,BDI=0),dict(id=577,BDI=2),
              dict(id=578,BDI=1),dict(id=579,BDI=1),dict(id=580,BDI=0),dict(id=581,BDI=4),
              dict(id=582,BDI=2),dict(id=583,BDI=3),dict(id=584,BDI=3),dict(id=585,BDI=3),
              dict(id=586,BDI=22),dict(id=587,BDI=29),dict(id=588,BDI=3),dict(id=589,BDI=0),
              dict(id=590,BDI=22),dict(id=591,BDI=30),dict(id=592,BDI=27),dict(id=593,BDI=1),
              dict(id=594,BDI=19),dict(id=595,BDI=20),dict(id=596,BDI=0),dict(id=597,BDI=13),
              dict(id=598,BDI=19),dict(id=599,BDI=1),dict(id=600,BDI=1),dict(id=601,BDI=2),
              dict(id=602,BDI=27),dict(id=603,BDI=21),dict(id=604,BDI=22),dict(id=605,BDI=20),
              dict(id=606,BDI=20),dict(id=607,BDI=28),dict(id=608,BDI=23),dict(id=609,BDI=26),
              dict(id=610,BDI=15),dict(id=611,BDI=15),dict(id=612,BDI=25),dict(id=613,BDI=28),
              dict(id=614,BDI=19),dict(id=615,BDI=30),dict(id=616,BDI=16),dict(id=617,BDI=18),
              dict(id=618,BDI=24),dict(id=619,BDI=23),dict(id=620,BDI=27),dict(id=621,BDI=17),
              dict(id=622,BDI=14),dict(id=623,BDI=19),dict(id=624,BDI=23),dict(id=625,BDI=16),
              dict(id=626,BDI=14),dict(id=627,BDI=30),dict(id=628,BDI=19)]
  excluded_subjects = [522,539,613]

  # BDI-II. Total score of 0–13 is considered minimal range, 14–19 is mild, 20–28 is moderate, and 29–63 is severe.
  severities = ['minimal', 'mild', 'moderate', 'sever']
  severities_abb = ['min', 'mil', 'mod', 'sev']
  BDIths = [0, 14, 20, 29, 64]

  train_methods=['normal', 'oversample']
  sfreq=500
  featnb = 31
  minAcceptableLoss = 20
  maxAcceptableDup = 5

  resultPath = './results/'