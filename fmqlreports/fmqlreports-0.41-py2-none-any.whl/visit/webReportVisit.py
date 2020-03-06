#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os
import re
import json
from collections import defaultdict, Counter
from datetime import datetime
import numpy

from fmqlutils.reporter.reportUtils import MarkdownTable, reportPercent, reportAbsAndPercent
from fmqlutils.typer.reduceTypeUtils import splitTypeDatas, checkDataPresent, singleValue, muBVC, muBVCOfSTProp
from fmqlreports.webReportUtils import filteredResultIterator, reduce200, TOP_MD_TEMPL, SITE_DIR_TEMPL, keyStats, roundFloat

"""
Overall: Encounter (Workload Focus)

Note: one of the "DSS-based" (https://github.com/vistadataproject/workload/issues/27) reports as Location is key. Part of a flow from Appointment through Visit. Reporting on both should go in tandem - the visit report <=> visit workload report.
"""
