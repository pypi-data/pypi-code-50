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

from utils import Utils

class Kaggle:
  userid = ''
  license = ''
  metafile = 'dataset-metadata.json'

  src_dataset = 'depression-rest-eeg-source-mat'
  srcdir = src_dataset+'/'

  set_dataset = src_dataset[:-4]+'-set'
  setdir = set_dataset+'/'

  epo_dataset = 'depression-rest-eeg-epochs'
  epodir = epo_dataset+'/'

  feat_dataset = 'depression-rest-eeg-features'
  featdir = feat_dataset+'/'

  deprest = 'Depression-Rest EEG Dataset - '
  datasettitles = {
    set_dataset: deprest + '.set files',
    epo_dataset: deprest + 'epochs',
    feat_dataset: deprest + 'features',
  }

  def __init__(self,license='CC0-1.0'):
    self.license = license

  def login(self):
    if not self.userid:
      import os
      kg = 'kaggle'
      name = 'kaggle.json'
      path = '~/.kaggle/'+name
      expandedpath = os.path.expanduser(path)
      if not os.path.isfile(expandedpath):
        print('Logging into Kaggle')
        try:
          Utils.run_cmd(['which {}'.format(kg)])
        except Exception as e:
          Utils.run_cmd(['pip install {} --user'.format(kg)])
        if not os.path.isdir(os.path.expanduser('~/.'+kg)):
          Utils.run_cmd(['mkdir ~/.'+kg])
        if os.path.isfile(name):
          Utils.run_cmd(['mv {} {}'.format(kg,path)])
        else:
          raise Exception('{} file is required, get it from your {} account, '.format(name,kg)+
            'upload/put it in the current working directory')
      Utils.run_cmd(['chmod 600 '+path])
      kagglejson = None
      with open(expandedpath,'r') as kagglejson:
        kagglejson = json.load(kagglejson)
      self.userid = kagglejson['username']

  def get_dataset(self, dataset, dirpath, overwrite=False, hard=False):
    import os
    self.login()
    if overwrite or not self.got_dataset(dataset):
      dataset_status = Utils.run_cmd(['kaggle datasets status {}/{}'.format(self.userid,dataset)],ret=True)
      if dataset_status.split('\n')[-1] != 'ready':
        msg = 'The {} dataset does not exist'.format(dataset)
        if hard:
          raise Exception(msg)
        else:
          print(msg)
      else:
        print('Downloading {} dataset'.format(dataset))
        Utils.run_cmd(['kaggle datasets download -d {}/{}'.format(self.userid,dataset)])
        print('Unzipping {} dataset files'.format(dataset))
        Utils.unzip('{}.zip'.format(dataset),dirpath)
        print('Removing zip file to free disk')
        Utils.run_cmd(['rm -f {}.zip'.format(dataset)])
    else:
      print('The {} dataset is already downloaded'.format(dataset))

  def get_sources(self,**kwargs):
    self.get_dataset(self.src_dataset, self.srcdir, **kwargs)

  def get_sets(self,**kwargs):
    self.get_dataset(self.set_dataset, self.setdir, **kwargs)

  def get_epochs(self,**kwargs):
    self.get_dataset(self.epo_dataset, self.epodir, **kwargs)

  def get_features(self,**kwargs):
    self.get_dataset(self.feat_dataset, self.featdir, **kwargs)

  def got_dataset(self,dataset):
    return {'mat':self.got_source,'set':self.got_sets,
    'epochs':self.got_epochs,'features':self.got_features}[dataset.split('-')[-1]]()

  def got_sources(self):
    return os.path.isdir(self.srcdir) and len(glob(self.srcdir+'*')) >= 119

  def got_sets(self):
    return os.path.isdir(self.setdir) and len(glob(self.setdir+'*')) >= 119

  def got_epochs(self):
    return os.path.isdir(self.epodir) and len(glob(self.epodir+'*')) >= 2*116

  def got_features(self):
    return os.path.isdir(self.featdir) and len(glob(self.featdir+'*')) >= 2*116

  def put_dataset(self, dataset, dirpath):
    dirpath = './'+dirpath
    import json
    self.login()
    if not os.path.isdir('./'+dirpath):
      raise Exception('./'+dirpath+' directory does not exists')
    dataset_status = Utils.run_cmd(['kaggle datasets status {}/{}'.format(self.userid,dataset)],ret=True)
    action = 'create'
    extra  = ''
    if dataset_status.split('\n')[-1] == 'ready':
      print('Dataset {} already exists, updating to a new version'.format(dataset))
      action = 'version'
      extra  = ' -m "Updated data"'
    if not os.path.isfile(dirpath+dataset+'.zip'):
      print('Zipping {} dataset files'.format(dataset))
      Utils.zip(dirpath+'*',dirpath+dataset+'.zip','-rj')
    metafile = dirpath+self.metafile
    cmd_find = "find {} ! -name '{}.zip' ! -name '{}' -type f -maxdepth 1".format(dirpath,dataset,metafile.split('/')[-1])
    if len(list(filter(None,Utils.run_cmd([cmd_find],ret=True).strip().split('\n')))):
      print('Moving {} dataset files to a subdirectory temporarily'.format(dataset))
      Utils.run_cmd(['mkdir {}temp'.format(dirpath)])
      Utils.run_cmd([cmd_find+" -exec mv -ft {}temp/ {{}} +".format(dirpath)])
    if not os.path.isfile(metafile):
      print('Initing {} dataset'.format(dataset))
      Utils.run_cmd(['kaggle datasets init -p '+dirpath])
      print('Filling {} file'.format(metafile))
      Utils.run_cmd(['echo "'+json.dumps({
          'licenses': [{'name':self.license}],
          'id': self.userid+'/'+dataset,
          'title': self.datasettitles[dataset]
          }, indent=2).replace('"','\\"')+'" > '+metafile])
    print('Uploading {} dataset'.format(dataset))
    Utils.run_cmd([('kaggle datasets {} -p '+dirpath+'{}').format(action,extra)])
    if glob('{}temp/*'.format(dirpath)):
      print('Moving back {} dataset files to the dataset\'s directory'.format(dataset))
      Utils.run_cmd(['mv -f {}/temp/* {}'.format(dirpath, dirpath)])
      Utils.run_cmd(['rm -rf {}/temp'.format(dirpath)])
    if os.path.isfile(dirpath+dataset+'.zip'):
      Utils.run_cmd(['rm -f {}.zip'.format(dirpath+dataset)])

  def put_sets(self):
    print('Upload Process of Sets Dataset:',self.set_dataset)
    self.put_dataset(self.set_dataset,self.setdir)

  def put_epochs(self):
    print('Upload Process of Epochs Dataset:',self.epo_dataset)
    self.put_dataset(self.epo_dataset,self.epodir)

  def put_features(self):
    print('Upload Process of Features Dataset:',self.feat_dataset)
    self.put_dataset(self.feat_dataset,self.featdir)