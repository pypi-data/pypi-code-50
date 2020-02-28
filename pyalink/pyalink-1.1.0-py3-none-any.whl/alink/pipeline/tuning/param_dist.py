from ...with_params import JavaObjectWrapper
from ...py4j_util import get_java_class
from ...converters import py_list_to_j_array


class ValueDist(JavaObjectWrapper):
    def get_j_obj(self):
        return self.j_value_dist

    @staticmethod
    def get_j_value_dist_cls():
        return get_java_class("com.alibaba.alink.pipeline.tuning.ValueDist")

    @staticmethod
    def randInteger(start, end):
        obj = ValueDist()
        obj.j_value_dist = ValueDist.get_j_value_dist_cls().randInteger(start, end)
        return obj

    @staticmethod
    def randLong(start, end):
        obj = ValueDist()
        obj.j_value_dist = ValueDist.get_j_value_dist_cls().randLong(start, end)
        return obj

    @staticmethod
    def randArray(*args):
        if len(args) <= 0:
            raise Exception("at least 1 item should be provided in randArray")
        if isinstance(args[0], (list, tuple, )):
            args = args[0]
        obj = ValueDist()
        j_args = py_list_to_j_array(get_java_class("Object"), len(args), args)
        obj.j_value_dist = ValueDist.get_j_value_dist_cls().randArray(j_args)
        return obj

    @staticmethod
    def exponential(l):
        obj = ValueDist()
        obj.j_value_dist = ValueDist.get_j_value_dist_cls().exponential(l)
        return obj

    @staticmethod
    def uniform(lowerbound, upperbound):
        obj = ValueDist()
        obj.j_value_dist = ValueDist.get_j_value_dist_cls().uniform(lowerbound, upperbound)
        return obj

    @staticmethod
    def normal(mu, sigma2):
        obj = ValueDist()
        obj.j_value_dist = ValueDist.get_j_value_dist_cls().normal(mu, sigma2)
        return obj

    @staticmethod
    def stdNormal():
        obj = ValueDist()
        obj.j_value_dist = ValueDist.get_j_value_dist_cls().stdNormal()
        return obj

    @staticmethod
    def chi2(df):
        obj = ValueDist()
        obj.j_value_dist = ValueDist.get_j_value_dist_cls().chi2(df)
        return obj

    def get(self, p):
        return self.get_j_obj().get(p)


class ParamDist(JavaObjectWrapper):
    def get_j_obj(self):
        return self.j_param_dist

    def __init__(self):
        j_param_dist_cls = get_java_class("com.alibaba.alink.pipeline.tuning.ParamDist")
        self.j_param_dist = j_param_dist_cls()
        self.items = []
        pass

    def addDist(self, stage, info, dist):
        # TODO: change the way to get info
        self.get_j_obj().addDist(stage.get_j_obj(), stage.get_j_obj().__getattr__(info), dist.get_j_obj())
        self.items.append((stage, info, dist))
        return self

    def getItems(self):
        return self.items
