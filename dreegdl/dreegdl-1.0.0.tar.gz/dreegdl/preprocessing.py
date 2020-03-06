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

import logging
import numpy as np
import os
import pywt
import scipy
import subprocess
from statsmodels.tsa.ar_model import AR
from glob import glob
from IPython.utils import io as ipio
from tqdm import tqdm_notebook as tqdmn
from .utils import Utils

class Preprocessing:

  def __init__(self,config={}):
    self.config = config

  def check_src_dest(self,src,dest,destname):
    if not src:
      raise Exception('No source is specified')
    if not dest:
      raise Exception('No output path is specified for {} files'.format(destname))
    if not os.path.isdir(dest):
      Utils.run_cmd(['mkdir '+dest])
      if not os.path.isdir(dest):
        raise Exception('Can not create directory :'+dest)

  def install_octave_oct2py_eeglab(self):
    print('Installing Octave, Oct2Py, and EEGLab packages')
    # Install Octave
    try:
      Utils.run_cmd(['which octave'])
    except Exception as e:
      # Update apt-get in order to install Octave
      Utils.run_cmd(['apt-get update; apt install octave -qq > /dev/null'])

    # Clone EEGLab to be used in Octave, processing raw EEG files
    if not os.path.isdir('./eeglab'):
      Utils.run_cmd(['git clone --recurse-submodules -q https://github.com/sccn/eeglab.git'])

    # Install Oct2Py
    try:
      import oct2py
    except ImportError as e:
      Utils.run_cmd(['pip install oct2py -q'])

    import oct2py
    oct2py.octave.addpath('./eeglab/functions/miscfunc')
    oct2py.octave.addpath('./eeglab/functions/guifunc')
    oct2py.octave.addpath('./eeglab/functions/popfunc')
    oct2py.octave.addpath('./eeglab/functions/adminfunc')
    oct2py.octave.addpath('./eeglab/functions/sigprocfunc')
    oct2py.octave.logger.setLevel(logging.ERROR)

  def install_mne(self):
    # Install MNE
    try:
      import mne
    except ImportError as e:
      Utils.run_cmd(['pip install mne -q'])

  def process_source(self,mat,fdest):
    import oct2py
    with ipio.capture_output():
      itemLoaded = oct2py.octave.pop_loadset(mat)
      itemChecked = oct2py.octave.eeg_checkset(itemLoaded)
      oct2py.octave.pop_saveset(
          itemChecked, filename=fdest.split('/')[-1],
          filepath='/'.join(fdest.split('/')[:-1]),
          savemode='onefile', check='on')
    del itemLoaded, itemChecked

  def process_sources(self,src='',dest=''):
    self.check_src_dest(src,dest,'Set')
    src = src.rstrip('/')
    dest = dest.rstrip('/')
    mats = sorted(glob(src+'/*.mat'))
    if not len(mats):
      raise Exception('No Mat file found')
    self.install_octave_oct2py_eeglab()
    print('Processing Source (.mat) files and converting them to .set files')
    for item in tqdmn(mats, ncols=500):
      fname = item.split('/')[-1]
      fdest = dest+'/'+fname[:-4]+'.set'
      if not os.path.isfile(fdest):
        self.process_source(item,fdest)

  # Provide Epochs
  def epoching(self,item,fepoch,ftimes):
    import mne
    with ipio.capture_output() as capt:
      ## Read SET file
      raw = mne.io.read_raw_eeglab(item)

      ## Fetch Events
      events, event_id = mne.events_from_annotations(raw)
      event_id = dict((k.replace('.0',''),v) for k,v in event_id.items())
      event_id_swapd = dict((v,k) for k,v in event_id.items())

      ## Set reference : self.config.ref_channels = ['M1', 'M2']
      if self.config.ref_channels:
        raw.set_eeg_reference(ref_channels=self.config.ref_channels)

      ## Drop Bad Channels : self.config.bad_channels = ['CB1', 'CB2', 'EKG', 'HEOG', 'VEOG']
      if self.config.bad_channels:
        raw.drop_channels([x for x in self.config.bad_channels if x in raw.ch_names])

      ## Remove Baseline : self.config.rm_baseline = (None, None)
      if self.config.rm_baseline:
        raw._data = mne.baseline.rescale(raw.get_data(), raw.times, self.config.rm_baseline)

      ## Apply Frequency Band Filter : self.config.filter_range = (0.2, 50)
      if self.config.filter_range:
        raw.filter(self.config.filter_range[0],self.config.filter_range[1], method='iir', verbose='WARNING')

      ## Apply ICA Decomposition : self.config.ica_args = dict(random_state=97, max_iter=3000)
      if self.config.ica_args:
        ica = mne.preprocessing.ICA(**self.config.ica_args)
        ica.fit(raw)
        ica.apply(raw)

      ## Apply Butter Filter : self.config.butter_filter = dict(order=5, highcut=50.0, lowcut=1.0)
      if self.config.butter_filter:
        for key,val in self.config.butter_filter.items(): exec(key+'=val')
        nyq = 0.5 * raw.info['sfreq']
        low = lowcut / nyq
        high = highcut / nyq
        b, a = scipy.signal.butter(order, [low, high], btype='band')
        raw._data = scipy.signal.lfilter(b, a, raw.get_data())

    ## Apply Epoching
    epochs = {}
    times = {}
    maxI = len(events) - 1
    prev_ev_name = None
    for i,ev in enumerate(events):
      ev_name = event_id_swapd[ev[2]]
      if ev_name not in self.config.valid_events:
        continue
      tmin = ev[0]
      if i == maxI:
        tmax = raw._data.shape[1]
      else:
        tmax = events[i+1][0]
        if len(events) > i+2 and ev[-1] not in [14,15] and events[i+1][-1] in [14,15]:
          ccc,j = 0,1
          while( events[i+j][-1] in [14,15] ): ccc+=1;j+=1;
          last = events[i+j]
          if (ev[-1] in [1,9,10,11,12,13]
              and (last[-1] == ev[-1] or last[0]-tmin <= 270)
              or (last[-1] != ev[-1] and tmax-tmin < 174 and last[0]-tmin <= 176)
              ):
            tmax = last[0]
      dd = raw._data[:,tmin:tmax].transpose()
      tt = raw._times[tmin:tmax]
      if epochs.get(ev_name) is None:
        epochs[ev_name] = [[dd]]
        times[ev_name] = [[tt]]
      else:
        if prev_ev_name == ev_name:
          epochs[ev_name][-1].append(dd)
          times[ev_name][-1].append(tt)
        else:
          epochs[ev_name].append([dd])
          times[ev_name].append([tt])
      prev_ev_name = ev_name
    if len(epochs) < len(self.config.valid_events):
      print('Subject does not have all events:',item)
      return False

    epochsNp = []
    timesNp = []
    for ev in self.config.valid_events:
      epochsNp.append(np.array([Utils.list2arr(*x) for x in epochs[ev]]))
      timesNp.append(np.array([Utils.list2arr(*x) for x in times[ev]]))
    epochsNp = Utils.list2arr(*epochsNp)
    timesNp = Utils.list2arr(*timesNp)

    np.save(fepoch, epochsNp)
    np.save(ftimes, timesNp)
    del epochs, epochsNp, timesNp
    return True

  def do_epoching(self,src='',dest=''):
    print('Epoching method has been called')
    self.check_src_dest(src,dest,'Epochs')
    src = src.rstrip('/')
    dest = dest.rstrip('/')
    ext1 = self.config.exts.get('set')
    sets = sorted(glob(src+'/*'+ext1))
    if not len(sets):
      raise Exception('No Set file found')
    self.install_mne()
    print('Epoching Set files')
    for fset in tqdmn(sets, ncols=500):
      fname = fset.split('/')[-1][:-len(ext1)]
      fepoch,ftimes = [dest+'/'+fname+ext for ext in self.config.exts.list('epo','ept')]
      if not (os.path.isfile(fepoch) and os.path.isfile(ftimes)):
        self.epoching(fset,fepoch,ftimes)

  # Provide Features
  def features_of_channel(self,data, timesdiff):
    if len(data) < 3:
      return None
    dwt='db4'
    # DWT - Discrete Wavelet Transform
    cA,cD = pywt.dwt(data, dwt)
    # DWT - FFT of Approximation
    cAf = np.fft.fft(cA)
    # DWT - FFT of Details
    cDf = np.fft.fft(cD)
    # Diff - First Order Difference
    diff1 = np.diff(data)
    # Diff - Second Order Difference
    diff2 = np.diff(data,n=2)
    # Diff - Variance of First Order Difference
    diff1Var = np.mean(diff1 ** 2)
    # Hjorth - Activity
    activity = np.var(data)
    # Hjorth - Mobility
    mobility = np.sqrt(diff1Var / activity)
    # Hjorth - Complexity
    complexity = np.sqrt(np.mean(diff2 ** 2) / diff1Var) / mobility
    # FFT - Fast Fourier Transform
    fft1 = np.fft.fft(data)
    # FFT - ABS(FFT)
    fft1abs = np.abs(fft1.real)
    # AR Model
    # m = AR(data)
    # # AR Model - fit with data
    # mArgs = {'ic':'aic','trend':'nc'}
    # mFit = m.fit(maxlag=3, **mArgs)
    # # AR Model - get best order
    # mOrder = m.select_order(maxlag=3, **mArgs)
    # # AR Model - get coefficients
    # AR3Coeffs = {
    #     'AutoRegressive Model Order 3 Coeff ' + str(i + 1) : x
    #     for i,x in enumerate([*mFit.params,0,0,0]) if i < 3
    #     }
    # Bands - Delta/Theta/Alpha/Beta
    bands = {
        'delta':{'freq':(0.5,4),'sum': 0,'max': 0},
        'theta':{'freq':(4,8)  ,'sum': 0,'max': 0},
        'alpha':{'freq':(8,13) ,'sum': 0,'max': 0},
        'beta' :{'freq':(13,30),'sum': 0,'max': 0},
    }
    shape1sfreq = float(data.shape[0])/self.config.sfreq
    for band,bandDict in bands.items():
      arange = np.arange(bandDict['freq'][0]*shape1sfreq,
                        bandDict['freq'][1]*shape1sfreq, dtype=int)
      bandDict['sum'] = np.sum(fft1abs.real[arange])
      bandDict['max'] = np.max(fft1abs.real[arange])
    # Vertex to Vertex Slope
    diff1Slope = diff1/timesdiff
    result = np.array([
      np.min(data),                                #   'Min'
      np.max(data),                                #   'Max'
      np.std(data),                                #   'STD'
      np.mean(data),                               #   'Mean'
      np.median(data),                             #   'Median'
      activity,                                    #   'Activity'
      mobility,                                    #   'Mobility'
      complexity,                                  #   'Complexity'
      scipy.stats.kurtosis(data),                  #   'Kurtosis'
      np.mean(diff2),                              #   '2nd Difference Mean'
      np.max(diff2),                               #   '2nd Difference Max'
      np.mean(diff1),                              #   '1st Difference Mean'
      np.max(diff1),                               #   '1st Difference Max'
      scipy.stats.variation(data),                 #   'Coeffiecient of Variation'
      scipy.stats.skew(data),                      #   'Skewness'
      np.mean(cA),                                 #   'Wavelet Approximate Mean'
      np.std(cA),                                  #   'Wavelet Approximate Std Deviation'
      np.mean(cD),                                 #   'Wavelet Detailed Mean'
      np.std(cD),                                  #   'Wavelet Detailed Std Deviation'
      np.sum(np.abs(cAf) ** 2) / cAf.size,         #   'Wavelet Approximate Energy'
      np.sum(np.abs(cDf) ** 2) / cDf.size,         #   'Wavelet Detailed Energy'
      -np.sum(cA * np.nan_to_num(np.log(cA))),     #   'Wavelet Approximate Entropy'
      -np.sum(cD * np.nan_to_num(np.log(cD))),     #   'Wavelet Detailed Entropy'
      np.mean(diff1Slope),                         #   'Mean of Vertex to Vertex Slope'
      np.var(diff1Slope),                          #   'Var  of Vertex to Vertex Slope'
      bands['delta']['max'],                       #   'FFT Delta Max Power'
      bands['theta']['max'],                       #   'FFT Theta Max Power'
      bands['alpha']['max'],                       #   'FFT Alpha Max Power'
      bands['beta' ]['max'],                       #   'FFT Beta Max Power'
      bands['delta']['sum']/bands['alpha']['sum'], #   'Delta/Alpha'
      bands['delta']['sum']/bands['theta']['sum'], #   'Delta/Theta'
      # *AR3Coeffs.values(),
    ])
    return result

  def file_extract(self,fepo,fept,ft1,ft2):
    epochs = np.load(fepo, allow_pickle=True)
    times  = np.load(fept, allow_pickle=True)
    ftv1 = []
    ftv2 = []
    # per event
    for ev in range(len(epochs)):
      # per epochs sequence
      ftv1.append([])
      ftv2.append([])
      for epo_gr in range(len(epochs[ev])):
        # per single epoch
        ftv1[-1].append([])
        ftv2[-1].append([])
        temp_e = np.concatenate(epochs[ev][epo_gr])
        temp_t = np.concatenate(times[ev][epo_gr])
        temp_td = np.diff(temp_t)
        for epo in range(len(epochs[ev][epo_gr])):
          # per channel
          timesdiff = np.diff(times[ev][epo_gr][epo])
          ftv1[-1][-1].append([])
          for ch in range(epochs[ev][epo_gr][epo].shape[1]):
            res = self.features_of_channel(epochs[ev][epo_gr][epo][:,ch], timesdiff)
            if res is not None:
              ftv1[-1][-1][-1].append(res)
            if epo == 0:
              res = self.features_of_channel(temp_e[:,ch], temp_td)
              if res is not None:
                ftv2[-1][-1].append(res)
            if not len(ftv1[-1][-1][-1]):
              del ftv1[-1][-1][-1]
          ftv1[-1][-1][-1] = np.array(ftv1[-1][-1][-1])
        ftv1[-1][-1] = np.array(ftv1[-1][-1])
        ftv2[-1][-1] = np.array(ftv2[-1][-1])
      ftv1[-1] = np.concatenate(ftv1[-1])
      ftv2[-1] = np.array(ftv2[-1])
    ftv1 = Utils.list2arr(*ftv1)
    ftv2 = Utils.list2arr(*ftv2)
    np.save(ft1, ftv1)
    np.save(ft2, ftv2)
    del epochs,times,ftv1,ftv2,timesdiff,temp_e,temp_t,temp_td
    return True

  def extract_features(self,src='',dest=''):
    print('Extract Features method has been called')
    self.check_src_dest(src,dest,'Features')
    src = src.rstrip('/')
    dest = dest.rstrip('/')
    ext1,ext2 = self.config.exts.list('epo','ept')
    epochs = sorted(glob(src+'/*'+ext1))
    if not len(epochs):
      raise Exception('No Epochs file found')
    print('Extracting features of epoched files')
    for fepo in tqdmn(epochs, ncols=500):
      fname = fepo.split('/')[-1][:-len(ext1)]
      fept = fepo[:-len(ext1)]+ext2
      if not os.path.isfile(fept):
        raise Exception('FileNotFound: '+fept)
      ft1,ft2 = [dest+'/'+fname+ext for ext in self.config.exts.list('ft1','ft2')]
      if not (os.path.isfile(ft1) and os.path.isfile(ft2)):
        self.file_extract(fepo,fept,ft1,ft2)
