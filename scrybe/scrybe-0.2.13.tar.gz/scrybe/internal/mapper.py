import weakref


class DBObjectMap(object):
    def __init__(self, after_gc_callback=None):
        self.obj_dict = dict()
        self.weak_ref_map = dict()
        self.after_gc_callback = after_gc_callback

    def gc_callback(self, weak_reference):
        key = self.weak_ref_map[weak_reference]
        if key in self.obj_dict.keys():
            self.obj_dict.pop(key)
        if self.after_gc_callback is not None:
            self.after_gc_callback(key)
        if weak_reference in self.weak_ref_map.keys():
            self.weak_ref_map.pop(weak_reference)

    def add(self, orig_object, db_object):
        if orig_object is None or db_object is None:
            return
        dict_key = self._get_dict_key(orig_object)
        if isinstance(orig_object, tuple):
            weak_refs = []
            for x in orig_object:
                try:
                    self.weak_ref_map[weakref.ref(x, self.gc_callback)] = dict_key
                except Exception as e:
                    #TODO(chandra): numpy.ndarray is not hashable
                    continue
        else:
            try:
                self.weak_ref_map[weakref.ref(orig_object, self.gc_callback)] = dict_key
            except Exception as e:
                pass
        self.obj_dict[dict_key] = db_object

    def is_obj_in_map(self, orig_object):
        if orig_object is None:
            return False
        dict_key = self._get_dict_key(orig_object)
        if dict_key in self.obj_dict.keys():
            return True
        return False

    def is_obj_id_in_map(self, orig_object_id):
        if orig_object_id in self.obj_dict.keys():
            return True
        return False

    def get_id(self, obj):
        return id(obj)

    def get_db_object(self, orig_object):
        if orig_object is None:
            return None
        dict_key = self._get_dict_key(orig_object)
        if dict_key in self.obj_dict.keys():
            return self.obj_dict[dict_key]
        return None

    def get_db_object_from_id(self, orig_object_id):
        if orig_object_id is None:
            return None
        if orig_object_id in self.obj_dict.keys():
            return self.obj_dict[orig_object_id]
        return None

    def _get_dict_key(self, orig_object):
        if isinstance(orig_object, tuple):
            keys = []
            for x in orig_object:
                keys.append(self.get_id(x))
            dict_key = tuple(keys)
        else:
            dict_key = self.get_id(orig_object)
        return dict_key

