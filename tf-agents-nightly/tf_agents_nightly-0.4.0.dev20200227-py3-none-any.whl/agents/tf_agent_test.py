# coding=utf-8
# Copyright 2018 The TF-Agents Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for agents.tf_agent."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import six
import tensorflow as tf  # pylint: disable=g-explicit-tensorflow-version-import

from tf_agents.agents import tf_agent
from tf_agents.specs import array_spec
from tf_agents.specs import tensor_spec
from tf_agents.trajectories import time_step as ts


class LossInfoTest(tf.test.TestCase):

  def testBaseLossInfo(self):
    loss_info = tf_agent.LossInfo(0.0, ())
    self.assertEqual(loss_info.loss, 0.0)
    self.assertIsInstance(loss_info, tf_agent.LossInfo)


class AgentSpecTest(tf.test.TestCase):

  def testErrorOnWrongTimeStepSpecWhenCreatingAgent(self):
    wrong_time_step_spec = ts.time_step_spec(
        array_spec.ArraySpec([2], np.float32))
    action_spec = tensor_spec.BoundedTensorSpec([1], tf.float32, -1, 1)
    with self.assertRaises(TypeError) as cm:
      tf_agent.TFAgent(wrong_time_step_spec, action_spec, None, None, None)
    self.assertStartsWith(
        six.text_type(cm.exception), 'time_step_spec has to contain TypeSpec')

  def testErrorOnWrongActionSpecWhenCreatingAgent(self):
    time_step_spec = ts.time_step_spec(tensor_spec.TensorSpec([2], tf.float32))
    wrong_action_spec = array_spec.BoundedArraySpec([1], np.float32, -1, 1)
    with self.assertRaises(TypeError) as cm:
      tf_agent.TFAgent(time_step_spec, wrong_action_spec, None, None, None)
    self.assertStartsWith(
        six.text_type(cm.exception),
        'action_spec has to contain BoundedTensorSpec')


if __name__ == '__main__':
  tf.test.main()
