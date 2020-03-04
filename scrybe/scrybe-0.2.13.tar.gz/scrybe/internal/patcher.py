import sys
import functools
import inspect
import imp
import logging

from scrybe.internal.threading_util import *
from scrybe.internal.tracker.stats_decorator_func.stats_util import is_stats_function
from scrybe.internal.util import get_original_args_kwargs, update_metadata_dict_with_new_kwargs

LOGGER = logging.getLogger(__name__)


def get_pep_302_importer(path):
    importer = sys.path_importer_cache.get(path)
    if not importer:
        for hook in sys.path_hooks:
            try:
                importer = hook(path)
                break

            except ImportError:
                pass
    return importer


def valid_new_args_kwargs(callback_return):
    if callback_return is None:
        return False

    try:
        args, kwargs = callback_return
    except (ValueError, TypeError):
        return False

    if not isinstance(args, (list, tuple)):
        return False

    if not isinstance(kwargs, dict):
        return False

    return True


def get_wrap_around_callbacks(before=None, after=None, exception_handler=None):
    if before is None:
        before_callbacks = []
    else:
        before_callbacks = before

    if exception_handler is None:
        exception_handler_callbacks = []
    else:
        exception_handler_callbacks = exception_handler

    if after is None:
        after_callbacks = []
    else:
        after_callbacks = after
    return before_callbacks, exception_handler_callbacks, after_callbacks


def eval_before_callbacks(metadata_dict, func_to_patch, orig_caller_frame, before_callbacks, *args,
                          **kwargs):
    should_run_after_callback = True
    for callback in before_callbacks:
        try:
            parameters = inspect.signature(callback).parameters
            if parameters is not None and 'scrybe_orig_fn_frame' in parameters.keys():
                callback_return = callback(metadata_dict, func_to_patch, orig_caller_frame, *args,
                                           **kwargs)
            else:
                callback_return = callback(metadata_dict, func_to_patch, *args, **kwargs)
            if isinstance(callback_return, bool):
                should_run_after_callback = callback_return

            if valid_new_args_kwargs(callback_return):
                args, kwargs = callback_return
        except Exception as e:
            LOGGER.error("Exception calling before callback %r. Error %s" % (callback, str(e)))
    return should_run_after_callback, args, kwargs


def eval_exception_handler_callbacks(metadata_dict, func_to_patch, exception_handler_callbacks, *args, **kwargs):
    for callback in exception_handler_callbacks:
        try:
            callback(metadata_dict, func_to_patch, *args, **kwargs)
        except Exception as e:
            LOGGER.error("Exception calling exception_handler callback %r. Error: %s" % (callback, str(e)))


def eval_after_callbacks(metadata_dict, return_value, func_to_patch, after_callbacks, exception_handler_callbacks,
                         *args, **kwargs):
    for callback in after_callbacks:
        try:
            callback_return = callback(metadata_dict, return_value, func_to_patch, *args, **kwargs)
            if callback_return is not None:
                return_value = callback_return
        except Exception as e:
            eval_exception_handler_callbacks(metadata_dict, func_to_patch, exception_handler_callbacks, *args, **kwargs)
            LOGGER.error("Exception calling after callback %r %s %s %s" % (callback, func_to_patch, type(e), e))
    return return_value


def set_parent_node_name_if_possible(obj, local_names):
    from scrybe.internal.depgraph import TrackingGraph
    if not TrackingGraph.has_tracked_obj(obj):
        return
    current_node = TrackingGraph.get_node_for_tracked_object(obj)
    # In order to be efficient and avoid looping through a cycle in the graph,
    # we will restrict the search to max 10 items
    max_nodes = 10
    parent_node_queue = [current_node]
    queue_index = 0
    while max_nodes >= len(parent_node_queue) > queue_index:
        current_node = parent_node_queue[queue_index]
        queue_index += 1
        predecessors = current_node.predecessors
        for node, ops in predecessors.items():
            parent_node_queue.append(node)
            if len(parent_node_queue) > max_nodes:
                break
    # Removing the first element
    parent_node_queue = parent_node_queue[1:]
    for node in parent_node_queue:
        for local_name, local_obj in local_names.items():
            if node.oid == id(local_obj):
                node.set_node_name_if_not_final(local_name)


def get_local_names(previous_frame, *args, **kwargs):
    local_names = previous_frame.f_locals
    arg_obj_names = []
    for arg_obj in args:
        arg_name = None
        for local_name, local_obj in local_names.items():
            if arg_obj is local_obj:
                arg_name = local_name
                break
        arg_obj_names.append(arg_name)
        set_parent_node_name_if_possible(arg_obj, local_names)
    kwargs_obj_names = dict()
    for kwarg_key in kwargs:
        kwarg_obj = kwargs[kwarg_key]
        kwarg_name = None
        if kwarg_obj is None:
            continue
        for local_name, local_obj in local_names.items():
            if kwarg_obj is local_obj:
                kwarg_name = local_name
                break
        kwargs_obj_names[kwarg_key] = kwarg_name
        set_parent_node_name_if_possible(kwarg_obj, local_names)
    return tuple(arg_obj_names), kwargs_obj_names


def get_class_fn_wrapper(cls, fn_name, before=None, after=None, exception_handler=None):
    before_callbacks, exception_handler_callbacks, after_callbacks = \
        get_wrap_around_callbacks(before=before, after=after, exception_handler=exception_handler)

    old_fn = cls.__dict__[fn_name]
    scrybe_fn_name = '__scrybe_' + fn_name + '__'
    setattr(cls, scrybe_fn_name, cls.__dict__[fn_name])

    def wrapper(self, *args, **kwargs):
        if ThreadLocalVarHandler.all_func.is_patching_disabled():
            callable = getattr(self, scrybe_fn_name)
            return callable(*args, **kwargs)
        # Call before callbacks before calling the original method
        previous_frame = sys._getframe().f_back
        arg_obj_names, kwargs_obj_names = get_local_names(previous_frame, self, *args, **kwargs)
        metadata_dict, args, kwargs = get_original_args_kwargs(*args, **kwargs)
        metadata_dict["arg_obj_names"] = arg_obj_names
        metadata_dict["kwargs_obj_names"] = kwargs_obj_names
        should_run_after_callback, args, kwargs = eval_before_callbacks(metadata_dict, old_fn,
                                                                        previous_frame, before_callbacks, self,
                                                                        *args, **kwargs)
        metadata_dict.update(update_metadata_dict_with_new_kwargs(**kwargs))
        # The above function returns (self, args) as args
        args = args[1:]
        try:
            callable = getattr(self, scrybe_fn_name)
            return_value = callable(*args, **kwargs)
            # return_value = self.__orig_fn__(*args, **kwargs)
        except Exception as e:
            eval_exception_handler_callbacks(metadata_dict, old_fn, exception_handler_callbacks, self,
                                             *args, **kwargs)
            raise e

        if should_run_after_callback:
            return_value = eval_after_callbacks(metadata_dict, return_value, old_fn, after_callbacks,
                                                exception_handler_callbacks, self, *args, **kwargs)

        return return_value

    functools.update_wrapper(wrapper, old_fn)
    return wrapper


def get_wrapper(func_to_patch, before=None, after=None, exception_handler=None):
    before_callbacks, exception_handler_callbacks, after_callbacks = \
        get_wrap_around_callbacks(before=before, after=after, exception_handler=exception_handler)

    def wrapper(*args, **kwargs):
        if ThreadLocalVarHandler.all_func.is_patching_disabled() or (
                ThreadLocalVarHandler.stats.is_patching_disabled() and is_stats_function(func_to_patch)):
            return func_to_patch(*args, **kwargs)
        # Call before callbacks before calling the original method
        previous_frame = sys._getframe().f_back
        arg_obj_names, kwargs_obj_names = get_local_names(previous_frame, *args, **kwargs)
        metadata_dict, args, kwargs = get_original_args_kwargs(*args, **kwargs)
        metadata_dict["arg_obj_names"] = arg_obj_names
        metadata_dict["kwargs_obj_names"] = kwargs_obj_names
        should_run_after_callback, args, kwargs = eval_before_callbacks(metadata_dict, func_to_patch, previous_frame,
                                                                        before_callbacks, *args, **kwargs)
        metadata_dict.update(update_metadata_dict_with_new_kwargs(**kwargs))
        try:
            return_value = func_to_patch(*args, **kwargs)
        except Exception as e:
            eval_exception_handler_callbacks(metadata_dict, func_to_patch, exception_handler_callbacks, *args, **kwargs)
            raise e

        if should_run_after_callback:
            return_value = eval_after_callbacks(metadata_dict, return_value, func_to_patch, after_callbacks,
                                                exception_handler_callbacks, *args, **kwargs)

        return return_value

    for attr in functools.WRAPPER_ASSIGNMENTS:
        if hasattr(func_to_patch, attr):
            setattr(wrapper, attr, getattr(func_to_patch, attr))
    wrapper.__wrapped__ = func_to_patch

    return wrapper


class CustomFileLoader(object):
    def __init__(self, loader, fullname, finder):
        self.loader = loader
        self.fullname = fullname
        self.finder = finder

    def exec_module(self, module):
        if hasattr(self.loader, "exec_module"):
            self.loader.exec_module(module)
        else:
            module = self.loader.load_module(self.fullname)

        return self.finder._patch(module, self.fullname)

    def create_module(self, spec):
        return None


class ScrybePatcher(object):
    def __init__(self):
        self.patcher_functions = {}
        self.post_load_functions = {}

        if sys.version_info[0] >= 3:
            from importlib.machinery import PathFinder

            self.pathfinder = PathFinder()

    def register_post_module_load(self, module_name, post_load_function):
        module_load_funcs = self.post_load_functions.setdefault(module_name, [])
        module_load_funcs.append(post_load_function)

    def register_before(self, module_name, object_name, patcher_function):
        self._register("before", module_name, object_name, patcher_function)

    def register_exception_handler(self, module_name, object_name, patcher_function):
        self._register("exception_handler", module_name, object_name, patcher_function)

    def register_after(self, module_name, object_name, patcher_function):
        self._register("after", module_name, object_name, patcher_function)

    def _register(self, lifecycle, module_name, object_name, patcher_function):
        module_patchers = self.patcher_functions.setdefault(module_name, {})
        object_patchers = module_patchers.setdefault(
            object_name, {"before": [], "after": [], "exception_handler": []}
        )
        object_patchers[lifecycle].append(patcher_function)

    def start(self):
        if self not in sys.meta_path:
            sys.meta_path.insert(0, self)

    def patch_already_imported_modules(self, module_name):
        module_name_list = []
        for key in self.patcher_functions:
            if key.startswith(module_name):
                module_name_list.append(key)
        for fullname in module_name_list:
            module = self._get_module(fullname)
            self._patch(module, fullname)

    def find_spec(self, fullname, path=None, target=None):
        if fullname not in self.patcher_functions and fullname not in self.post_load_functions:
            return

        from importlib.machinery import ModuleSpec

        spec = self.pathfinder.find_spec(fullname, path, target)

        if not spec:
            return

        if hasattr(spec, 'origin') and spec.origin:
            module_spec = ModuleSpec(fullname, CustomFileLoader(spec.loader, fullname, self), origin=spec.origin)
            module_spec.has_location = True
        else:
            module_spec = ModuleSpec(fullname, CustomFileLoader(spec.loader, fullname, self))
        return module_spec

    def _get_module(self, fullname):
        splitted_name = fullname.split(".")
        parent = ".".join(splitted_name[:-1])

        if fullname in sys.modules:
            return sys.modules[fullname]

        elif parent in sys.modules:
            parent = sys.modules[parent]
            module_path = imp.find_module(splitted_name[-1], parent.__path__)
            return imp.load_module(fullname, *module_path)

        else:
            try:
                module_path = imp.find_module(fullname)
                return imp.load_module(fullname, *module_path)

            except ImportError:
                for p in sys.path:
                    importer = get_pep_302_importer(p)

                    # Ignore invalid paths
                    if importer is None:
                        continue

                    module_path = importer.find_module(fullname)

                    if module_path:
                        return importer.load_module(fullname)

    def _patch(self, module, fullname):
        objects_to_patch = self.patcher_functions.get(fullname, {})

        for object_name, patcher_callbacks in objects_to_patch.items():
            object_path = object_name.split(".")
            # TODO(chandra): Handle this more generically
            if 'sklearn' in fullname and object_name.startswith('Pipeline.'):
                pipeline_cls = self._get_object(module, [object_path[0]])
                fn_name = object_path[1]
                if 'delegate_names' in dir(pipeline_cls.__dict__[object_path[1]]):
                    new_object = get_class_fn_wrapper(pipeline_cls, fn_name, **patcher_callbacks)
                    setattr(pipeline_cls, fn_name, new_object)
                    continue

            original = self._get_object(module, object_path)

            if original is None:
                continue

            new_object = get_wrapper(original, **patcher_callbacks)
            self._set_object(module, object_path, new_object)

        post_load_callables = self.post_load_functions.get(fullname, [])
        for func in post_load_callables:
            func(module)

        return module

    def _get_object(self, module, object_path):
        current_object = module

        for part in object_path:
            try:
                current_object = getattr(current_object, part)
            except AttributeError:
                return None

        return current_object

    def _set_object(self, module, object_path, new_object):
        object_to_patch = self._get_object(module, object_path[:-1])
        setattr(object_to_patch, object_path[-1], new_object)
