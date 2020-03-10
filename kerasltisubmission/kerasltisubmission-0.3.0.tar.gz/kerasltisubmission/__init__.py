# -*- coding: utf-8 -*-

"""Top-level package for kerasltisubmission."""

__author__ = """into-ai"""
__email__ = "introintoai@gmail.com"
__version__ = "0.3.0"

from kerasltisubmission.kerasltisubmission import Submission as _Submission
from kerasltisubmission.provider import AnyIDType as _AnyIDType
from kerasltisubmission.provider import LTIProvider as _LTIProvider
from kerasltisubmission.provider import PredictionsType as _PredictionsType

AnyIDType = _AnyIDType
LTIProvider = _LTIProvider
PredictionsType = _PredictionsType
Submission = _Submission
