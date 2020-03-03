import weakref
from typing import Union


class CustomParamManager(object):
    class TrackedParam(object):
        def __init__(self, metric: dict):
            self.metric = metric

        def update_metric(self, metric: dict):
            self.metric.update(metric)

        def get_metric(self):
            return self.metric

    # Following is a map from [TrackedParam] -> [model] (which needs to be tracked)
    # This keeps a ref on the TrackedParam object and thereby keeps the custom metric object alive
    TRACKER_MODEL_MAP = weakref.WeakValueDictionary()

    # Following is a map from model's OID -> [TrackedParam]
    # This allows looking up the TrackedParam corresponding to a model which needs tracking
    # This has a cascading delete effect -- when the main object gets collected, it will
    # remove the entry from TRACKER_MODEL_MAP, thereby losing the ref on the TrackedParam instance,
    # which in-turn will cause the entry to be removed from the below map
    OID_MODEL_MAP = weakref.WeakValueDictionary()

    @classmethod
    def has_tracked_param(cls, model) -> bool:
        return id(model) in cls.OID_MODEL_MAP

    @classmethod
    def get_custom_metric_for_model(cls, model) -> dict:
        #  This function always returns the node corresponding to the latest (i.e. current) version
        #  of the object
        return cls.OID_MODEL_MAP[id(model)].get_metric()

    @classmethod
    def add_tracked_param(cls, model, metric: dict):
        if cls.has_tracked_param(model=model):
            tracked_param = cls.OID_MODEL_MAP[id(model)]
            tracked_param.update_metric(metric=metric)
        else:
            tracked_param = cls.TrackedParam(metric=metric)
            cls.TRACKER_MODEL_MAP[tracked_param] = model
            cls.OID_MODEL_MAP[id(model)] = tracked_param

    @classmethod
    def get_custom_metric_for_model_uid(cls, uid: str) -> Union[dict, None]:
        try:
            for k, v in cls.TRACKER_MODEL_MAP.items():
                if hasattr(v, 'uid') and v.uid == uid:
                    return k.get_metric()
        except Exception as e:
            return None
