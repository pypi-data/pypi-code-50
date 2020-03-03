import inspect
import json
import os

from .const import SCRYBE_METADATA_KEYS

SITE_PACKAGES = None


def get_default_func_signature(func):
    parameters = inspect.signature(func).parameters
    if parameters is None:
        return [], []
    args = list(parameters.keys())
    defaults = list()
    for arg in args:
        val = parameters[arg]
        if val.default == inspect._empty:
            continue
        defaults.append(val.default)
    return args, defaults


def get_default_func_params(func):
    default_dict = dict()
    if func is None:
        return [], default_dict
    argspec = inspect.getfullargspec(func)
    args = argspec.args
    defaults = argspec.defaults
    if args is None or len(args) == 0:
        args, defaults = get_default_func_signature(func)
    if args is None:
        args = []
    if 'self' in args:
        args.remove('self')
    if defaults is None or len(defaults) == 0:
        return args, default_dict
    num_required_args = len(args) - len(defaults)
    for i in range(len(defaults)):
        default_dict[args[num_required_args + i]] = defaults[i]
    for key in default_dict.keys():
        args.remove(key)
    return args, default_dict


def get_default_class_init_params(class_object):
    return get_default_func_params(getattr(class_object, '__init__', None))


def get_default_params(orig_object):
    if inspect.isfunction(orig_object):
        return get_default_func_params(orig_object)
    return get_default_class_init_params(orig_object)


def get_hyperparams(processed_params, default_dict, req_args, trim=False):
    hyperparameters = dict()
    for item in processed_params.items():
        arg, val = item
        if arg in default_dict.keys():
            if val == default_dict[arg]:
                continue
            else:
                default_dict.pop(arg)
        if trim:
            hyperparameters[arg] = get_parameter_vals(val)
        else:
            hyperparameters[arg] = val
    hyperparameters['algo_defaults'] = default_dict
    hyperparameters['req_args'] = req_args
    return hyperparameters


def is_patched_object(orig_object, patched_modules):
    module_name = orig_object.__class__.__module__
    class_name = orig_object.__class__.__name__
    for patched_module, patched_class in patched_modules:
        patched_class = patched_class.replace('.fit', '')
        if module_name == patched_module and class_name == patched_class:
            return True
    return False


def get_func_arg_names(orig_func):
    parameters = inspect.signature(orig_func).parameters
    arg_names = []
    if parameters is not None:
        arg_names = list(parameters.keys())
    return arg_names


def get_func_req_params(arg_names, list_of_pos, *args, **kwargs):
    params = []
    for i in range(len(list_of_pos)):
        pos_index = list_of_pos[i]
        if pos_index < 0:
            params.append(None)
            continue
        if len(args) > pos_index:
            params.append(args[pos_index])
        else:
            if len(arg_names) > pos_index and arg_names[pos_index] in kwargs:
                params.append(kwargs[arg_names[pos_index]])
            else:
                params.append(None)
    if len(params) == 1:
        return params[0]
    return tuple(params)


def update_metadata_dict_with_new_kwargs(**kwargs):
    metadata_dict = dict()
    for key, value in kwargs.items():
        if key in SCRYBE_METADATA_KEYS:
            metadata_dict[key] = value
    return metadata_dict


def get_original_args_kwargs(*args, **kwargs):
    modified_kwargs = dict()
    metadata_dict = dict()
    for key in SCRYBE_METADATA_KEYS:
        metadata_dict[key] = None
    for key, value in kwargs.items():
        if key in metadata_dict:
            metadata_dict[key] = value
        else:
            modified_kwargs[key] = value
    return metadata_dict, args, modified_kwargs


def get_module_name(frame):
    if '__name__' in frame.f_globals:
        return frame.f_globals['__name__']
    return ''


class ScrybeJSONEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """

    def default_json(self, non_serializable_obj):
        try:
            return float(non_serializable_obj)
        except Exception as e:
            return "%s.%s" % (non_serializable_obj.__class__.__module__, non_serializable_obj.__class__.__name__)

    def default(self, obj):
        try:
            import numpy
            if isinstance(obj, (numpy.int_, numpy.intc, numpy.intp, numpy.int8,
                                numpy.int16, numpy.int32, numpy.int64, numpy.uint8,
                                numpy.uint16, numpy.uint32, numpy.uint64)):
                return int(obj)
            elif isinstance(obj, (numpy.float_, numpy.float16, numpy.float32,
                                  numpy.float64)):
                return float(obj)
            elif isinstance(obj, numpy.ndarray):
                return obj.tolist()
            return self.default_json(obj)
        except ImportError:
            return self.default_json(obj)


def get_site_packages():
    global SITE_PACKAGES
    if SITE_PACKAGES is not None:
        return SITE_PACKAGES

    import sys

    def _get_path(userbase):
        version = sys.version_info

        if os.name == 'nt':
            return '%s\\Python%s%s\\site-packages' % (userbase, version[0], version[1])

        if sys.platform == 'darwin' and sys._framework:
            return '%s/lib/python/site-packages' % userbase

        return '%s/lib/python%s.%s/site-packages' % (userbase, version[0], version[1])

    def _getsitepackages(prefixes):
        sitepackages = []
        seen = set()
        for prefix in prefixes:
            if not prefix or prefix in seen:
                continue
            seen.add(prefix)
            if os.sep == '/':
                sitepackages.append(os.path.join(prefix, "lib",
                                                 "python%d.%d" % sys.version_info[:2],
                                                 "site-packages"))
            else:
                sitepackages.append(prefix)
                sitepackages.append(os.path.join(prefix, "lib", "site-packages"))
        return sitepackages
    import site
    prefixes = []
    for prefix in site.PREFIXES:
        prefixes.append(os.path.abspath(prefix))
    prefixes.append('/usr/local')
    if hasattr(site, 'getsitepackages'):
        SITE_PACKAGES = site.getsitepackages(prefixes=prefixes)
    else:
        SITE_PACKAGES = _getsitepackages(prefixes=prefixes)
    if hasattr(site, 'getusersitepackages'):
        SITE_PACKAGES.append(os.path.abspath(site.getusersitepackages()))
    else:
        import sysconfig
        # noinspection PyProtectedMember
        user_base = sysconfig._getuserbase()
        user_base_path = _get_path(user_base)
        SITE_PACKAGES.append(os.path.abspath(user_base_path))
    SITE_PACKAGES = list(set(SITE_PACKAGES))
    return SITE_PACKAGES


def is_site_package_file(filename):
    site_packages = get_site_packages()
    for package in site_packages:
        if os.path.commonpath([package, filename]) == package:
            return True
    return False


# noinspection PyBroadException
def is_site_package_caller(caller_frame):
    # from inspect import getsourcefile, getfile
    # filename = getsourcefile(caller_frame) or getfile(caller_frame)
    filename = os.path.abspath(caller_frame.f_code.co_filename)
    if filename is None:
        return True
    return is_site_package_file(filename=filename)


# noinspection PyBroadException,PyPackageRequirements
def get_info(obj):
    import io
    buf = io.StringIO()
    try:
        import numpy as np
        if isinstance(obj, np.ndarray):
            np.info(obj, output=buf)
            info_str = buf.getvalue()
            info_lines = info_str.split("\n")
            line_to_remove = None
            for line in info_lines:
                if line.startswith("data pointer"):
                    line_to_remove = line
            if line_to_remove is not None:
                info_lines.remove(line_to_remove)
            return "\n".join(info_lines)
    except Exception:
        pass
    try:
        from pandas import DataFrame, Series
        if isinstance(obj, DataFrame):
            obj.info(buf=buf)
            info_str = buf.getvalue()
            if "Data columns" not in info_str and obj.columns.size > 0:
                info_str += '\n' + "Data columns (total %d columns):" % len(obj.columns)
                max_columns = 1000
                for i in range(len(obj.columns)):
                    if i > max_columns:
                        info_str += '\n' + "+%d more columns" % (len(obj.columns) - i)
                        break
                    info_str += '\n' + str(obj.columns[i])
            info_lines = info_str.split("\n")
            if len(info_lines) > 0 and info_lines[0].startswith("<"):
                info_lines = info_lines[1:]
            return "\n".join(info_lines)
        elif isinstance(obj, Series):
            info = "name: %s\n" % obj.name
            info += "length: %d\n" % obj.shape[0]
            info += "type: %s" % str(obj.dtype)
            return info
    except Exception:
        pass
    try:
        from pyspark.sql import DataFrame as spark_dataframe
        if isinstance(obj, spark_dataframe):
            info = obj._jdf.schema().treeString()
            info += "\n\nDAG:\n"
            info += obj._jdf.queryExecution().simpleString()
            return info
    except Exception:
        pass
    return ""


def get_item_if_basic_type(item):
    if isinstance(item, (str, int, float)):
        return item
    else:
        try:
            import numpy
            if isinstance(item, (numpy.int_, numpy.intc, numpy.intp, numpy.int8,
                                 numpy.int16, numpy.int32, numpy.int64, numpy.uint8,
                                 numpy.uint16, numpy.uint32, numpy.uint64)):
                return int(item)
            elif isinstance(item, (numpy.float_, numpy.float16, numpy.float32,
                                   numpy.float64)):
                return float(item)
            else:
                return None
        except ImportError:
            return None


def get_value_for_list(value, max_len=10):
    count = 0
    concat_val = []
    for item in value:
        count += 1
        basic_item = get_item_if_basic_type(item=item)
        if basic_item is None:
            break
        concat_val.append(item)
        if count > max_len:
            break
    if len(concat_val) > 0:
        return concat_val
    else:
        return value.__class__.__name__


def get_parameter_vals(value, max_len=10):
    basic_val = get_item_if_basic_type(item=value)
    if basic_val is not None:
        return value
    else:
        if isinstance(value, (list, tuple)):
            value = get_value_for_list(value=value, max_len=max_len)
        elif isinstance(value, dict):
            count = 0
            concat_dict = dict()
            for key in value:
                count += 1
                item = value[key]
                basic_item = get_item_if_basic_type(item=item)
                if basic_item is None:
                    break
                concat_dict[key] = basic_item
                if count > max_len:
                    break
            if len(concat_dict) > 0:
                value = concat_dict
            else:
                value = value.__class__.__name__
        else:
            try:
                import numpy
                if isinstance(value, numpy.ndarray):
                    value = get_value_for_list(value=value)
                else:
                    value = value.__class__.__name__
            except Exception as e:
                try:
                    value = value.__class__.__name__
                except Exception as e:
                    value = str(type(value))
        return value
