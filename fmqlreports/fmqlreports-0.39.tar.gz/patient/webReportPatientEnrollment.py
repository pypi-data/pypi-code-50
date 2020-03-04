#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os
import re
import json
from collections import defaultdict
from datetime import datetime

from fmqlutils.reporter.reportUtils import MarkdownTable, reportPercent, reportAbsAndPercent

from fmqlutils.typer.reduceTypeUtils import splitTypeDatas, checkDataPresent, singleValue

from fmqlreports.webReportUtils import SITE_DIR_TEMPL

"""
Basic Patient Enrollment

Requires:
- 27_11 ?

... needs to be fully filled in
"""
