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

import os
import numpy as np
import pandas as pd
import math
import sklearn.preprocessing as skp
import sklearn.model_selection as skm
import matplotlib.pyplot as plt
from datetime import datetime
from IPython.display import HTML, display, Image
from sklearn.metrics import confusion_matrix, accuracy_score
from tqdm import tqdm_notebook as tqdmn
from copy import copy
from smote import Smote

class Training:

  csv = None
  datatypes = ['train', 'test']
  fit_data = {}
  X = {}
  X_classified = {}
  loop_desc = {
    'models': 'Models',
    'methods': 'Model %s Methods',
    'epochs': 'Model %s Method %s Epochs',
    'events': 'Model %s Method %s Epoch %s Events',
    'channels': 'Model %s Method %s Epoch %s Event %s Channels',
  }
  figures = []

  def __init__(self,config={},kg={}):
    self.config = config
    self.kg = kg
    self.reset_data()
    self.reset_fit_data()
    self.get_csv()

  def reset_data(self):
    self.X = {'train': [], 'test': []}
    self.X_classified = {'train': [], 'test': []}

  def reset_fit_data(self):
    self.fit_data = {self.datatypes[0]:{'x':np.array([]),'y':np.array([])},
                      self.datatypes[1]:{'x':np.array([]),'y':np.array([])}}

  def BDI_cat(self,bdi):
    return np.array([
      (bdi>=self.config.BDIths[t] and bdi<self.config.BDIths[t+1]) and 1 or 0 
      for t in range(len(self.config.BDIths)-1)])
  def BDI_index(self,bdi):
    return np.argmax(self.BDI_cat(bdi))

  def BDI_sev(self,bdi):
    return self.config.severities[self.BDI_index(bdi)]

  def BDI_sev_abb(self,bdi):
    return self.config.severities_abb[self.BDI_index(bdi)]

  # Read the CSV file or Create it from subjects
  def get_csv(self):
    self.csv = pd.DataFrame(self.config.subjects)
    self.csv = self.csv[self.csv['BDI'].isin(range(100))]
    self.csv = self.csv[~self.csv['id'].isin(self.config.excluded_subjects)]
    print('List of Id and BDI per subject:')
    display(self.csv)

  def provide_fit_data(self,model,method,event,channel):
    self.reset_fit_data()
    for dt in self.datatypes:
      for item in self.X[dt]:
        epochs = np.load(self.kg.featdir+self.config.name_pattern.format(item)+
                         self.config.exts.get('ft'+str(model.version)),
                         allow_pickle=True)
        x = epochs[self.config.valid_events.index(event)][:,channel]
        y = np.array([self.csv[self.csv.id == item]['BDI'].iloc[0]])
        del epochs
        self.fit_data[dt]['x'] = np.array(list(self.fit_data[dt]['x'])+[x])
        self.fit_data[dt]['y'] = np.array(list(self.fit_data[dt]['y'])+[y])
    if method == 'oversampling':
      self.oversampling()
    if model.transforms.count('scale'):
      scaler = skp.StandardScaler()
    for dt in self.datatypes:
      if model.x_conv:
        self.fit_data[dt]['x'] = model.x_conv(self.fit_data[dt]['x'])
      if model.y_conv:
        self.fit_data[dt]['y'] = model.y_conv(self.fit_data[dt]['y'])
      if model.transforms.count('scale'):
        for ep in self.fit_data[dt]['x']:
          scaler.partial_fit(ep)
    if len(model.transforms):
      for dt in self.datatypes:
        for j,ep in enumerate(self.fit_data[dt]['x']):
          for trans in model.transforms:
            if trans == 'scale':
              self.fit_data[dt]['x'][j] = scaler.transform(ep)
            elif trans == 'norm':
              self.fit_data[dt]['x'][j] = skp.Normalizer().fit_transform(ep)

  def oversampling(self):
    maxlen = max([len(x) for x in self.X_classified['train']])
    for x in self.X_classified['train']:
      if len(x) == maxlen: continue
      difflen = maxlen - len(x)
      augment_rate = max(math.ceil(1.0*difflen/len(x))*100,100)
      temp_index = [self.X['train'].index(k) for k in x]
      temp_shape = self.fit_data['train']['x'][0].shape
      sm = Smote(sample=[k.flatten() for k in self.fit_data['train']['x'][temp_index]],
                  N=augment_rate, k=4)
      sm.over_sampling()
      self.fit_data['train']['x'] = np.array(list(self.fit_data['train']['x'])+\
          [k.reshape(temp_shape) for k in np.array(sm.synthetic)[0:difflen]])
      self.fit_data['train']['y'] = np.array(list(self.fit_data['train']['y'])+(
          [np.mean(self.fit_data['train']['y'][temp_index])]*difflen))

  def viz_train_test_data(self):
    fig = plt.figure(figsize=(14, 4))
    axes = fig.subplots(ncols=len(self.datatypes))
    for i,dt in enumerate(self.datatypes):
      temp=list(zip(*[(x,self.csv[self.csv.id == x]['BDI'].iloc[0]) for x in self.X[dt]]))
      axes[i].plot(list(range(len(temp[1]))), temp[1], label=dt.capitalize()+' BDI')
      axes[i].set_ylabel('BDI')
      axes[i].set_xlabel('Subject')
      axes[i].legend()
    plt.show()

  def train_test_split(self):
    self.X['train'],self.X['test'] = [],[]
    self.X_classified['train'],self.X_classified['test'] = [],[]
    for t in range(len(self.config.BDIths)-1):
      csv_tmp = self.csv[(self.csv.BDI >= self.config.BDIths[t]) & (self.csv.BDI < self.config.BDIths[t+1])]
      x_train,x_test,c,d = skm.train_test_split(
          csv_tmp['id'], csv_tmp['BDI'], test_size=0.20, random_state=42)
      self.X_classified['train'].append(list(x_train))
      self.X['train'].extend(self.X_classified['train'][-1])
      self.X['test'].extend(x_test)
    np.random.shuffle(self.X['train'])
    np.random.shuffle(self.X['test'])
    self.X_classified['test'] = self.X['test'].copy()

  def history_predict(self,predPath='',logPath='',hist=[],pred=[]):
    out = []
    if logPath == '' and len(hist) == 0:
      return HTML(''.join(out))
    y_true,y_pred,y_pred_best = pred if len(pred) else np.load(predPath)
    h=pd.DataFrame(hist) if len(hist) else pd.read_csv(logPath)
    h_best_i = 0
    if len(h[h['loss']<self.config.minAcceptableLoss]):
      h_best_i = int(h[h['val_loss'] == min(list(h[h['loss']<self.config.minAcceptableLoss
                                                    ]['val_loss']))].iloc[0].name)
    y_true_sev = np.array([self.BDI_sev_abb(x) for x in y_true])
    y_pred_sev = np.array([self.BDI_sev_abb(x) for x in y_pred])
    y_pred_best_sev = np.array([self.BDI_sev_abb(x) for x in y_pred_best])
    out.append(HTML('<div style="text-align: center;">'+
                    HTML('<table><tr><td style="padding-right:20px">'+
                    HTML(pd.DataFrame({
                        'Loss':{
                          'Last': round(list(h['loss'])[-1],3),
                          'Best': round(list(h['loss'])[h_best_i],3)},
                        'Val-Loss':{
                          'Last': round(list(h['val_loss'])[-1],3),
                          'Best': round(list(h['val_loss'])[h_best_i],3)},
                        'Acc':{
                          'Last': round(list(h['acc'])[-1],3),
                          'Best': round(list(h['acc'])[h_best_i],3)},
                        'Val-Acc':{
                          'Last': round(list(h['val_acc'])[-1],3),
                          'Best': round(list(h['val_acc'])[h_best_i],3)},
                          }).to_html()).data
                  +'</td><td>'+
                  HTML(pd.DataFrame(
                    [round(((y_true-y_pred)**2).mean(),2),
                    round(((y_true-y_pred_best)**2).mean(),2)],
                    index=['Regression‌ {} Predict Loss'.format(w) for w in ['Final','Best']]
                    ).to_html(header=None)).data
                  +'</td><td>'+
                  HTML(pd.DataFrame(
                    [round(accuracy_score(y_true_sev,y_pred_sev)*100,2),
                    round(accuracy_score(y_true_sev,y_pred_best_sev)*100,2)],
                    index=['Classification‌ {} Predict Acc'.format(w) for w in ['Final','Best']]
                    ).to_html(header=None)).data
                  +'</td></tr></table>').data
                +HTML(pd.DataFrame(
                    [y_true,y_pred,y_pred_best,y_true_sev,y_pred_sev,y_pred_best_sev],
                    index=[b+a for a in ['',' Severity'] 
                          for b in ['True', 'Predict', 'Best Predict']]
                          ).style.apply(
                              lambda x: ['color: white;background-color : '+
                                          (i%3==0 and 'gray' or 'yellowgreen')
                                          if (i%3==0 or y == x.iloc[i//3*3]) 
                                          else '' for i,y in enumerate(x)]).render()
                                          ).data+
                    '</div>').data)
    axitems = [
      {'label':{'y':'Loss','x':'Epoch'},
        'items':[{'val':h['loss'], 'label':'Train Loss'},
                {'val':h['val_loss'], 'label':'Validation Loss'}]},
      {'label':{'y':'Acc','x':'Epoch'},
        'items':[{'val':h['acc'], 'label':'Train Acc'},
                {'val':h['val_acc'], 'label':'Validation Acc'}]},
      {'label':{'y':'BDI','x':'Subject'},
        'items':[{'val':y_true, 'label':'True'},
                {'val':y_pred, 'label':'Predict'}]},
      {'label':{'y':'BDI','x':'Subject'},
        'items':[{'val':y_true, 'label':'True'},
                {'val':y_pred_best, 'label':'Best Predict'}]},
    ]
    with ipio.capture_output():
      if len(self.figures) == 0 or self.figures[0] is None:
        lines = []
        fig = plt.figure(figsize=(22, 4))
        fig.subplots(ncols=4)
        for k,axesit in enumerate(fig.axes):
          lines_tmp = []
          for axit in axitems[k]['items']:
            tmp, = axesit.plot(list(range(len(axit['val']))), 
                                list(axit['val']), label=axit['label'])
            lines_tmp.append(tmp)
          lines.append(lines_tmp)
          axesit.set_ylabel(axitems[k]['label']['y'])
          axesit.set_xlabel(axitems[k]['label']['x'])
          axesit.legend()
        self.figures.append(fig)
      else:
        for k,axesit in enumerate(self.figures[0].axes):
          for m,axit in enumerate(axitems[k]['items']):
            self.figures[0].axes[k].lines[m].set_xdata(list(range(len(axit['val']))))
            self.figures[0].axes[k].lines[m].set_ydata(list(axit['val']))
          self.figures[0].axes[k].relim()
          self.figures[0].axes[k].autoscale_view(True,True,True)
        self.figures[0].canvas.draw()
      plt.close()
    return HTML(''.join(out))

  def fit_generator(self,x_data,y_data):
    while 1:
      for i in range(len(x_data)):
        yield (x_data[i:i+1], y_data[i:i+1])

  def train_test(self,mdD, method, epnb, event, chan):
    name = '_'.join([mdD.name,'ep'+('000'+str(epnb))[-5:],'ev'+event,
                      'ch'+('0'+str(chan+1))[-2:]]
                    +(method != 'normal' and [method] or []))
    modelPath = self.config.resultPath+'/'+name+'.h5'
    bestModelPath = self.config.resultPath+'/'+name+'_best.h5'
    logPath = self.config.resultPath+'/'+name+'.log'
    predPath = self.config.resultPath+'/'+name+'.npy'
    already_trained = False
    history = []
    prediction = []
    result = None
    currModel = None
    bestModel = None
    bestValLossI = 0
    if len(self.figures):
      del self.figures[0]

    def modelCheckPoint():
      nonlocal bestValLossI
      nonlocal history
      nonlocal currModel
      nonlocal bestModel
      if (currModel and len(history)>1 and history[-1].get('loss') and 
          history[-1].get('loss')<self.config.minAcceptableLoss):
        last = history[-1].get('val_loss')
        best = min([10**10]+[h['val_loss'] for h in history[bestValLossI:-1] 
                    if h['loss']<self.config.minAcceptableLoss])
        if last and last<=best:
          y_true,y_pred = predict(best=False, ret=True)
          if len(set(y_pred)) >= len(set(y_true)) - self.config.maxAcceptableDup:
            bestModel = copy(currModel)
            bestValLossI = len(history)-1
            drawResult()

    def predict(best=True,ret=False):
      nonlocal currModel
      nonlocal bestModel
      nonlocal prediction
      nonlocal mdD
      def conv(a):
        return a.round().astype(int).flatten()
      if not mdD.usegen:
          preds = [conv(self.fit_data['test']['y']),
                   conv(currModel.predict(self.fit_data['test']['x'],verbose=0))]
          if best:
            preds.append(conv(bestModel.predict(self.fit_data['test']['x'],verbose=0)))
      else:
          preds = [conv(self.fit_data['test']['y']),
                   conv(currModel.predict_generator(
                       self.fit_generator(self.fit_data['test']['x'],
                                          self.fit_data['test']['y']),
                       steps=len(self.fit_data['test']['x']),verbose=0))]
          if best:
            preds.append(conv(bestModel.predict_generator(
                self.fit_generator(self.fit_data['test']['x'],
                                   self.fit_data['test']['y']),
                          steps=len(self.fit_data['test']['x']),verbose=0)))
      preds = np.array(preds)
      if ret:
        return preds
      else:
        prediction = preds

    def drawResult(online=True, fig=False, pred=True):
      nonlocal result
      nonlocal history
      nonlocal currModel
      nonlocal bestModel
      nonlocal predPath
      nonlocal logPath
      nonlocal prediction
      if online:
        if pred:
          predict()
        out = self.history_predict(hist=history, pred=prediction)
      else:
        out = self.history_predict(predPath, logPath)
        pass
      if result is None:
        result = [display(out, display_id=True), None]
        if fig:
          result[1] = display(Utils.fig_to_html(self.figures[0]), display_id=True)
      else:
        result[0].update(out)
        if fig:
          display(Utils.fig_to_html(self.figures[0]), display_id=True)

    tf.keras.backend.clear_session()
    if os.path.isfile(modelPath):
      currModel = load_model(bestModelPath)
      bestModel = load_model(bestModelPath)
      history = pd.read_csv(logPath)
      history = history.filter(history.columns[1:]).to_dict('records')
      already_trained = True
    else:
      currModel = mdD.model(self.fit_data['train']['x'][0].shape, len(self.fit_data['train']['y']))
      bestModel = copy(currModel)
    if mdD.show_summary:
      Utils.summary_print(currModel)
    outDesc='Model: %s'%(name)
    out = tqdmn(total=epnb,ncols=800,desc=outDesc,dynamic_ncols=True)
    if not already_trained: 
      drawResult()
      out_last_update = datetime.now().timestamp()
      def out_update():
        nonlocal out
        nonlocal out_last_update
        nonlocal history
        out.update(1)
        if datetime.now().timestamp() - out_last_update > 1.:
          out_last_update = datetime.now().timestamp()
          out.set_postfix({k:round(v,2) for k,v in history[-1].items()})
      callbacks = [LambdaCallback(
          on_epoch_end=lambda e,l: [history.append(l),out_update(),modelCheckPoint()])]
      if not mdD.usegen:
          batch_size = mdD.batch_size if type(mdD.batch_size) == int else mdD.batch_size(self.fit_data['train']['y'])
          currModel.fit(self.fit_data['train']['x'], self.fit_data['train']['y'], verbose=0, epochs=epnb, callbacks=callbacks,
                        batch_size=batch_size, validation_data=(self.fit_data['test']['x'], self.fit_data['test']['y']))
      else:
          batch_size = mdD.batch_size if type(mdD.batch_size) == int else mdD.batch_size(self.fit_data['train']['y'])
          currModel.fit_generator(self.fit_generator(self.fit_data['train']['x'],self.fit_data['train']['y']),
                                  verbose=0, epochs=epnb,steps_per_epoch=batch_size,
                                  validation_data=self.fit_generator(self.fit_data['test']['x'],self.fit_data['test']['y']),
                                  validation_steps=len(self.fit_data['test']['y']),
                                  callbacks=callbacks)
      predict()
      history = pd.DataFrame(history)
      history.index.name = 'epoch'
      history.to_csv(logPath)
      currModel.save(modelPath)
      bestModel.save(bestModelPath)
      np.save(predPath, prediction)
    else:
      out.update(epnb)
    drawResult(False,True)

  def train_test_loop(self,models):
    if not os.path.isdir(self.config.resultPath):
      Utils.run_cmd(['mkdir {}'.format(self.config.resultPath)])
    if not self.X.get('train'):
      tr.train_test_split()
    tr.viz_train_test_data()
    desc = self.loop_desc['models']
    for m in tqdmn(models,ncols=1000,desc=desc):
      m.show_summary = True
      desc = self.loop_desc['methods']%(m.name)
      for method in tqdmn(m.methods,ncols=1000,desc=desc):
        desc = self.loop_desc['epochs']%(m.name,method)
        for epnb in tqdmn(m.epochs,ncols=1000,desc=desc):
          desc = self.loop_desc['events']%(m.name,method,epnb)
          for event in tqdmn(m.events,ncols=1000,desc=desc):
            desc = self.loop_desc['channels']%(m.name,method,epnb,event)
            for channel in tqdmn(range(len(m.channels)),ncols=1000,desc=desc):
              self.provide_fit_data(m, method, event, channel)
              self.train_test(m, method, epnb, event, channel)
              m.show_summary = False
