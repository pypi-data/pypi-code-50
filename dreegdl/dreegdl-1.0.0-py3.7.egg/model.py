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

from config import Config

class Model:
  defaults = {
    'epochs': [50,100,500,1000], # Default epochs
    'batch_size': lambda x: len(x), # Default batch size function
    'methods': ['normal', 'oversample'],
    'transforms':['scale','norm'],
    'channels': Config.chs,
    'events': Config.valid_events,
    }
  show_summary = False

  def __init__(self,name='',model=None,version=1,usegen=False,
               batch_size=defaults['batch_size'],epochs=defaults['epochs'],
               methods=defaults['methods'],transforms=defaults['transforms'],
               channels=defaults['channels'],events=defaults['events'],
               x_conv=None,y_conv=None):
    self.name = name
    self.model = model
    self.version = version
    self.usegen = usegen
    self.channels = channels
    self.events = events
    self.batch_size = batch_size
    self.epochs = epochs
    self.methods = methods
    self.transforms = transforms
    self.x_conv = x_conv
    self.y_conv = y_conv