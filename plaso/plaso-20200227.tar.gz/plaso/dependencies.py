# -*- coding: utf-8 -*-
"""Functionality to check for the availability and version of dependencies.

This file is generated by l2tdevtools update-dependencies.py, any dependency
related changes should be made in dependencies.ini.
"""

from __future__ import print_function
from __future__ import unicode_literals

import re


# Dictionary that contains version tuples per module name.
#
# A version tuple consists of:
# (version_attribute_name, minimum_version, maximum_version, is_required)
#
# Where version_attribute_name is either a name of an attribute,
# property or method.
PYTHON_DEPENDENCIES = {
    'artifacts': ('__version__', '20190305', None, True),
    'bencode': ('', '', None, True),
    'biplist': ('', '1.0.3', None, True),
    'certifi': ('__version__', '2016.9.26', None, True),
    'cffi': ('__version__', '1.9.1', None, True),
    'chardet': ('__version__', '2.0.1', None, True),
    'cryptography': ('__version__', '2.0.2', None, True),
    'dateutil': ('__version__', '1.5', None, True),
    'defusedxml': ('__version__', '0.5.0', None, True),
    'dfdatetime': ('__version__', '20180704', None, True),
    'dfvfs': ('__version__', '20200117', None, True),
    'dfwinreg': ('__version__', '20180712', None, True),
    'dtfabric': ('__version__', '20181128', None, True),
    'elasticsearch': ('__versionstr__', '6.0', None, False),
    'future': ('__version__', '0.16.0', None, True),
    'idna': ('__version__', '2.5', None, True),
    'lz4': ('', '0.10.0', None, False),
    'pefile': ('__version__', '2018.8.8', None, True),
    'psutil': ('__version__', '5.4.3', None, True),
    'pybde': ('get_version()', '20140531', None, True),
    'pyesedb': ('get_version()', '20150409', None, True),
    'pyevt': ('get_version()', '20191104', None, True),
    'pyevtx': ('get_version()', '20141112', None, True),
    'pyewf': ('get_version()', '20131210', None, True),
    'pyfsapfs': ('get_version()', '20181205', None, True),
    'pyfsntfs': ('get_version()', '20191201', None, True),
    'pyfvde': ('get_version()', '20160719', None, True),
    'pyfwnt': ('get_version()', '20180117', None, True),
    'pyfwsi': ('get_version()', '20150606', None, True),
    'pylnk': ('get_version()', '20150830', None, True),
    'pyluksde': ('get_version()', '20200101', None, True),
    'pymsiecf': ('get_version()', '20150314', None, True),
    'pyolecf': ('get_version()', '20151223', None, True),
    'pyparsing': ('__version__', '2.3.0', None, True),
    'pyqcow': ('get_version()', '20131204', None, True),
    'pyregf': ('get_version()', '20150315', None, True),
    'pyscca': ('get_version()', '20190605', None, True),
    'pysigscan': ('get_version()', '20190629', None, True),
    'pysmdev': ('get_version()', '20140529', None, True),
    'pysmraw': ('get_version()', '20140612', None, True),
    'pytsk3': ('get_version()', '20160721', None, True),
    'pytz': ('__version__', '', None, True),
    'pyvhdi': ('get_version()', '20131210', None, True),
    'pyvmdk': ('get_version()', '20140421', None, True),
    'pyvshadow': ('get_version()', '20160109', None, True),
    'pyvslvm': ('get_version()', '20160109', None, True),
    'requests': ('__version__', '2.18.0', None, True),
    'six': ('__version__', '1.1.0', None, True),
    'urllib3': ('__version__', '1.21.1', None, True),
    'xlsxwriter': ('__version__', '0.9.3', None, True),
    'yaml': ('__version__', '3.10', None, True),
    'yara': ('YARA_VERSION', '3.4.0', None, True),
    'zmq': ('__version__', '2.1.11', None, True)}

_VERSION_SPLIT_REGEX = re.compile(r'\.|\-')


def _CheckPythonModule(
    module_name, version_attribute_name, minimum_version,
    is_required=True, maximum_version=None, verbose_output=True):
  """Checks the availability of a Python module.

  Args:
    module_name (str): name of the module.
    version_attribute_name (str): name of the attribute that contains
       the module version or method to retrieve the module version.
    minimum_version (str): minimum required version.
    is_required (Optional[bool]): True if the Python module is a required
        dependency.
    maximum_version (Optional[str]): maximum required version. Should only be
        used if there is a later version that is not supported.
    verbose_output (Optional[bool]): True if output should be verbose.

  Returns:
    bool: True if the Python module is available and conforms to
        the minimum required version, False otherwise.
  """
  module_object = _ImportPythonModule(module_name)
  if not module_object:
    if not is_required:
      print('[OPTIONAL]\tmissing: {0:s}.'.format(module_name))
      return True

    print('[FAILURE]\tmissing: {0:s}.'.format(module_name))
    return False

  if not version_attribute_name or not minimum_version:
    if verbose_output:
      print('[OK]\t\t{0:s}'.format(module_name))
    return True

  module_version = None
  if not version_attribute_name.endswith('()'):
    module_version = getattr(module_object, version_attribute_name, None)
  else:
    version_method = getattr(module_object, version_attribute_name[:-2], None)
    if version_method:
      module_version = version_method()

  if not module_version:
    if not is_required:
      print((
          '[OPTIONAL]\tunable to determine version information '
          'for: {0:s}').format(module_name))
      return True

    print((
        '[FAILURE]\tunable to determine version information '
        'for: {0:s}').format(module_name))
    return False

  # Make sure the module version is a string.
  module_version = '{0!s}'.format(module_version)

  # Split the version string and convert every digit into an integer.
  # A string compare of both version strings will yield an incorrect result.
  module_version_map = list(
      map(int, _VERSION_SPLIT_REGEX.split(module_version)))
  minimum_version_map = list(
      map(int, _VERSION_SPLIT_REGEX.split(minimum_version)))

  if module_version_map < minimum_version_map:
    if not is_required:
      print((
          '[OPTIONAL]\t{0:s} version: {1!s} is too old, {2!s} or later '
          'required.').format(module_name, module_version, minimum_version))
      return True

    print((
        '[FAILURE]\t{0:s} version: {1!s} is too old, {2!s} or later '
        'required.').format(module_name, module_version, minimum_version))
    return False

  if maximum_version:
    maximum_version_map = list(
        map(int, _VERSION_SPLIT_REGEX.split(maximum_version)))
    if module_version_map > maximum_version_map:
      if not is_required:
        print((
            '[OPTIONAL]\t{0:s} version: {1!s} is too recent, {2!s} or earlier '
            'required.').format(module_name, module_version, minimum_version))
        return True

      print((
          '[FAILURE]\t{0:s} version: {1!s} is too recent, {2!s} or earlier '
          'required.').format(module_name, module_version, maximum_version))
      return False

  if verbose_output:
    print('[OK]\t\t{0:s} version: {1!s}'.format(module_name, module_version))

  return True


def _ImportPythonModule(module_name):
  """Imports a Python module.

  Args:
    module_name (str): name of the module.

  Returns:
    module: Python module or None if the module cannot be imported.
  """
  try:
    module_object = list(map(__import__, [module_name]))[0]
  except ImportError:
    return None

  # If the module name contains dots get the upper most module object.
  if '.' in module_name:
    for submodule_name in module_name.split('.')[1:]:
      module_object = getattr(module_object, submodule_name, None)

  return module_object


def CheckDependencies(verbose_output=True):
  """Checks the availability of the dependencies.

  Args:
    verbose_output (Optional[bool]): True if output should be verbose.

  Returns:
    bool: True if the dependencies are available, False otherwise.
  """
  print('Checking availability and versions of dependencies.')
  check_result = True

  for module_name, version_tuple in sorted(PYTHON_DEPENDENCIES.items()):
    if not _CheckPythonModule(
        module_name, version_tuple[0], version_tuple[1],
        is_required=version_tuple[3], maximum_version=version_tuple[2],
        verbose_output=verbose_output):
      check_result = False

  if check_result and not verbose_output:
    print('[OK]')

  print('')
  return check_result
