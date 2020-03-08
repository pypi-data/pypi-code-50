import tpDcc as tp

import artellapipe.register
from artellapipe.core import toolbox


class MayaToolBox(toolbox.ToolBox, object):
    def __init__(self, project, parent=None):
        if parent is None:
            parent = tp.Dcc.get_main_window()
        super(MayaToolBox, self).__init__(project=project, parent=parent)


if tp.is_maya():
    artellapipe.register.register_class('ToolBox', MayaToolBox)
