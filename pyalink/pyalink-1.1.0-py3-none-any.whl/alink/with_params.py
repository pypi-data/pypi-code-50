from .py4j_util import get_java_class
from .converters import py_list_to_j_array


class JavaObjectWrapper:
    def get_j_obj(self):
        raise Exception("Not supported.")


class WithParams(JavaObjectWrapper):

    def __init__(self, *args, **kwargs):
        self.params = dict()

    @staticmethod
    def _get_setter_name(key):
        if key == "project": return "setProjectName"
        if key == "endpoint": return "setEndPoint"
        return "set" + key[0].capitalize() + key[1:]

    def _set_array_params(self, method_name, val):
        choices = []

        int_choices = [
            get_java_class("java.lang.Integer"),
            get_java_class("java.lang.Long"),
            get_java_class("int"),
            get_java_class("long")
        ]

        float_choices = [
            get_java_class("java.lang.Float"),
            get_java_class("java.lang.Double"),
            get_java_class("float"),
            get_java_class("double"),
        ]

        str_choices = [get_java_class("java.lang.String")]

        all_choices = [*int_choices, *float_choices, *str_choices]

        if len(val) == 0:
            choices = all_choices
        elif isinstance(val[0], int):
            choices = int_choices
        elif isinstance(val[0], float):
            choices = float_choices
        elif isinstance(val[0], str):
            choices = str_choices

        choices.append(get_java_class("Object"))

        success = False
        j_obj = self.get_j_obj()
        for choice in choices:
            try:
                args = py_list_to_j_array(choice, len(val), val)
                j_obj.__getattr__(method_name)(args)
                success = True
            except:
                pass
        if not success:
            choices_str = list(
                map(lambda d: d._java_lang_class.getName(), choices))
            raise Exception("Method " + method_name +
                            " with array of any type in " + str(choices_str) + " does not exist.")

    def _set_simple_params(self, method_name, val):
        if isinstance(val, str):
            args = get_java_class("java.lang.String")(val)
        else:
            args = val

        wrapper_j_object = self.get_j_obj()
        wrapper_j_object.__getattr__(method_name)(args)

    def _set_cuts_2d_array(self, array_2d):
        lengths = []
        array_1d = []
        for arr in array_2d:
            array_1d.extend(arr)
            lengths.append(len(arr))
        j_array_1d = py_list_to_j_array(get_java_class("double"), len(array_1d), array_1d)
        j_lengths = py_list_to_j_array(get_java_class("int"), len(lengths), lengths)
        self.get_j_obj().setCutsArray(j_array_1d, j_lengths)
        return self

    def _add_param(self, key, val):
        self.params[key] = val
        method_name = self._get_setter_name(key)

        if key == "cutsArray":
            return self._set_cuts_2d_array(val)

        if isinstance(val, (list, tuple, )):
            self._set_array_params(method_name, val)
        else:
            self._set_simple_params(method_name, val)

        if key == "vizName":
            from .session import Session
            self.params["isStat"] = "true"
            Session.inst().add_batch_sink(self)

        return self
