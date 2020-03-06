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

# SMOTE Class is a modified version of https://github.com/yzhu01/Class-Imbalance
from sklearn.neighbors import NearestNeighbors
import random as rd

class Smote:
  """
  Implement SMOTE, synthetic minority oversampling technique.
  Parameters
  -----------
  sample      2D (numpy)array
              minority class samples
  N           Integer
              amount of SMOTE N%
  k           Integer
              number of nearest neighbors k
              k <= number of minority class samples
  Attributes
  ----------
  newIndex    Integer
              keep a count of number of synthetic samples
              initialize as 0
  synthetic   2D array
              array for synthetic samples
  neighbors   K-Nearest Neighbors model
  """
  def __init__(self, sample, N, k):
    self.sample = sample
    self.k = k
    self.T = len(self.sample)
    self.N = N
    self.newIndex = 0
    self.synthetic = []
    self.neighbors = NearestNeighbors(n_neighbors=self.k).fit(self.sample)

  def over_sampling(self):
    if self.N < 100:
      self.T = (self.N / 100) * self.T
      self.N = 100
    self.N = int(self.N / 100)
    for i in range(0, self.T):
      nn_array = self.compute_k_nearest(i)
      self.populate(self.N, i, nn_array)

  def compute_k_nearest(self, i):
    nn_array = self.neighbors.kneighbors([self.sample[i]], self.k, return_distance=False)
    if len(nn_array) is 1:
      return nn_array[0]
    else:
      return []

  def populate(self, N, i, nn_array):
    while N is not 0:
      nn = rd.randint(1, self.k - 1)
      self.synthetic.append([])
      for attr in range(0, len(self.sample[i])):
        dif = self.sample[nn_array[nn]][attr] - self.sample[i][attr]
        gap = rd.random()
        while (gap == 0):
          gap = rd.random()
        self.synthetic[self.newIndex].append(self.sample[i][attr] + gap * dif)
      self.newIndex += 1
      N -= 1