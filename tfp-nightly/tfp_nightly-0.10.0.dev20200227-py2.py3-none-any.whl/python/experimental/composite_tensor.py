# Copyright 2019 The TensorFlow Probability Authors.
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
# ============================================================================
"""Use `tfp.distributions.Distribution`s as `tf.CompositeTensor`s."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import inspect

import tensorflow.compat.v2 as tf
from tensorflow_probability.python import distributions
from tensorflow_probability.python.internal import tensor_util
from tensorflow.python.framework.composite_tensor import CompositeTensor  # pylint: disable=g-direct-tensorflow-import
from tensorflow.python.saved_model import nested_structure_coder  # pylint: disable=g-direct-tensorflow-import


__all__ = ['as_composite']


_registry = {}  # Mapping from (python pkg, class name) -> class.


class _DistributionTypeSpec(tf.TypeSpec):
  """A tf.TypeSpec for `tfp.distributions.Distribution` objects."""

  __slots__ = ('_clsid', '_kwargs', '_param_specs')

  def __init__(self, clsid, param_specs, kwargs):
    self._clsid = clsid
    self._kwargs = kwargs
    self._param_specs = param_specs

  @property
  def value_type(self):
    return _registry[self._clsid]

  def _to_components(self, obj):
    return {k: getattr(obj, k, obj.parameters[k])
            for k in sorted(self._param_specs)}

  def _from_components(self, components):
    kwargs = dict(self._kwargs)
    kwargs.update(components)
    return self.value_type(**kwargs)  # pylint: disable=not-callable

  @property
  def _component_specs(self):
    return self._param_specs

  def _serialize(self):
    return 1, self._clsid, self._param_specs, self._kwargs

  @classmethod
  def _deserialize(cls, encoded):
    version, clsid, param_specs, kwargs = encoded
    if version != 1:
      raise ValueError('Unexpected version')
    if _find_clsid(clsid) is None:
      raise ValueError(
          'Unable to identify distribution type for {}. For non-builtin '
          'distributions, you will need to call `as_composite` before '
          '`tf.saved_model.load` to warm up a cache.'.format(clsid))
    return cls(clsid, param_specs, kwargs)


_TypeSpecCodec = nested_structure_coder._TypeSpecCodec  # pylint: disable=protected-access
_TypeSpecCodec.TYPE_SPEC_CLASS_FROM_PROTO[275837168] = _DistributionTypeSpec
_TypeSpecCodec.TYPE_SPEC_CLASS_TO_PROTO[_DistributionTypeSpec] = 275837168
del _TypeSpecCodec


def _make_convertible(cls):
  """Makes a subclass of `cls` that also subclasses `CompositeTensor`."""

  clsid = (cls.__module__, cls.__name__)

  if clsid in _registry:
    return _registry[clsid]

  class _CompositeTensorDist(cls, CompositeTensor):
    """A per-`cls` subclass of `CompositeTensor`."""

    def _parameter_control_dependencies(self, is_init):
      # We are forced by the CompositeTensor contract (no graph operations in
      # `_to_components`, `_from_components`) to defer the
      # `_initial_parameter_control_dependencies` to point-of-use.
      if is_init:
        return ()

      result = tuple(
          super(_CompositeTensorDist, self)._parameter_control_dependencies(
              is_init=True))
      result += tuple(
          super(_CompositeTensorDist, self)._parameter_control_dependencies(
              is_init=True))
      return result

    @property
    def _type_spec(self):
      kwargs = dict(self.parameters)
      param_specs = {}
      for k in self._params_event_ndims():
        if k in kwargs and kwargs[k] is not None:
          param_specs[k] = tf.TensorSpec.from_tensor(kwargs.pop(k))
      return _DistributionTypeSpec(
          clsid, param_specs=param_specs, kwargs=kwargs)

  _CompositeTensorDist.__name__ = '{}CT'.format(cls.__name__)
  _registry[clsid] = _CompositeTensorDist
  return _CompositeTensorDist


# Lazy-cache into `_registry` so that `tf.saved_model.load` will work.
def _find_clsid(clsid):
  pkg, cls = clsid
  if clsid not in _registry:
    if pkg.startswith('tensorflow_probability.') and '.distributions' in pkg:
      dist_cls = getattr(distributions, cls)
      if (inspect.isclass(dist_cls) and
          issubclass(dist_cls, distributions.Distribution)):
        _make_convertible(dist_cls)
  return _registry[clsid] if clsid in _registry else None


def as_composite(obj):
  """Returns a `CompositeTensor` equivalent to the given object.

  Note that the returned object will have any `Variable`,
  `tfp.util.DeferredTensor`, or `tfp.util.TransformedVariable` references it
  closes over converted to tensors at the time this function is called. The
  type of the returned object will be a subclass of both `CompositeTensor` and
  `type(obj)`.

  Note: This method is best-effort and based on a heuristic for what the
  tensor parameters are and what the non-tensor parameters are. Things might be
  broken, especially for meta-distributions like `TransformedDistribution` or
  `Independent`. (We try to raise NotImplementedError in such cases.) If you'd
  benefit from better coverage, please file an issue on github or send an email
  to `tfprobability@tensorflow.org`.

  Args:
    obj: A `tfp.distributions.Distribution`.

  Returns:
    obj: A `tfp.distributions.Distribution` that extends `CompositeTensor`.
  """
  if isinstance(obj, CompositeTensor):
    return obj
  cls = _make_convertible(type(obj))
  kwargs = dict(obj.parameters)
  def mk_err_msg(suffix=''):
    return (
        'Unable to make a CompositeTensor for "{}" of type `{}`. Email '
        '`tfprobability@tensorflow.org` or file an issue on github if you '
        'would benefit from this working. {}'.format(obj, type(obj), suffix))
  try:
    params_event_ndims = obj._params_event_ndims()  # pylint: disable=protected-access
  except NotImplementedError:
    raise NotImplementedError(mk_err_msg())
  for k in params_event_ndims:
    # Use dtype inference from ctor.
    if k in kwargs and kwargs[k] is not None:
      v = getattr(obj, k, kwargs[k])
      kwargs[k] = tf.convert_to_tensor(v, name=k)
  for k, v in kwargs.items():
    if tensor_util.is_ref(v):
      kwargs[k] = tf.convert_to_tensor(v, name=k)
  result = cls(**kwargs)
  struct_coder = nested_structure_coder.StructureCoder()
  if not struct_coder.can_encode(result._type_spec):  # pylint: disable=protected-access
    raise NotImplementedError(mk_err_msg('(Unable to serialize.)'))
  return result
