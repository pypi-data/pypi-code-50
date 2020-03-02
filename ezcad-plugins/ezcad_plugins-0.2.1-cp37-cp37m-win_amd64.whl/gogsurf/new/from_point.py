# -*- coding: utf-8 -*-
# Copyright (c) Ezcad Development Team. All Rights Reserved.

from ezcad.config.base import _
from .from_tsurf import Dialog as BaseDialog


class Dialog(BaseDialog):
    NAME = _("Create Gsurf from Point")

    def __init__(self, parent=None):
        BaseDialog.__init__(self, parent)

    def setup_page_input(self):
        text = _("Input Point")
        geom = ['Point']
        self.grabob = self.create_grabob(text, geom=geom)
        self.layout.addWidget(self.grabob)
