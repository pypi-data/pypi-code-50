# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

import os
import sys
if os.path.realpath(os.path.dirname(__file__)) not in sys.path:
    sys.path.append(os.path.realpath(os.path.dirname(__file__)))

from ezcad.app.mainwindow import CustomObject
from golabel.label import Label as DataObject


class Label(CustomObject):
    """ Dummy object bridging host and plugin """
    NAME = "Label"

    def __init__(self):
        super().__init__()
        self.dob = DataObject
