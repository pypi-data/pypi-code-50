from ...with_params import JavaObjectWrapper
from ...py4j_util import get_java_class
from ...converters import py_list_to_j_array


class ParamGrid(JavaObjectWrapper):
    def get_j_obj(self):
        return self.j_param_dist

    def __init__(self):
        j_param_dist_cls = get_java_class("com.alibaba.alink.pipeline.tuning.ParamGrid")
        self.j_param_dist = j_param_dist_cls()
        self.items = []
        pass

    def addGrid(self, stage, info, *args):
        if len(args) <= 0:
            raise Exception("at least 1 item should be provided in addGrid")
        if isinstance(args[0], (list, tuple, )):
            args = args[0]
        # TODO: change the way to get info
        j_args = py_list_to_j_array(get_java_class("Object"), len(args), args)
        self.get_j_obj().addGrid(stage.get_j_obj(), stage.get_j_obj().__getattr__(info), j_args)
        self.items.append((stage, info, args))
        return self

    def getItems(self):
        return self.items
