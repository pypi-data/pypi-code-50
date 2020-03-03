import builtins
import inspect
import sys

from typing import Dict, List


class ModulePatcher(object):
    def __init__(self, patch_func_map: Dict, dynamic_class_specs: List, class_method_patcher_spec: List,
                 post_patch_additional_modules: List):
        """
        :param patch_func_map: Dictionary of function name which needs patching to function constructor
        :param dynamic_class_specs: List of classes which need to be created dynamically using base classes
            from this module. Each element of the list is a tuple: the first element is a function which
            constructs and returns the class object and the second element is optional. When provided, this
            should be class name from the original module which should be replaced by the new dynamic class
        :param class_method_patcher_spec: List of class methods which need to be patched. Unlike functions,
            this requires two level look-ups (module dictionary contains class and class dictionary contains
            method). This list should contain a spec of three items (in this order):
                class-name, method-name, function constructor
        :param post_patch_additional_modules: This is a special list. In some cases, the module we are patching
        might already be loaded. In such cases, the internal/sub-packages (e.g. "numpy.core._multiarray_umath") will
        be handled via patch_module as usual. However, unlike the module load scenario, any functions which have been
        propagated to higher level packages (e.g. "numpy") will still be pointing to the original implementations.
        This parameter allows additional patching of any other packages to fix this issue.

        """
        self.patch_func_map = patch_func_map
        self.dynamic_class_specs = dynamic_class_specs
        self.class_method_patcher_spec = class_method_patcher_spec
        self.post_patch_additional_modules = post_patch_additional_modules
        self.patched_module = None

    @staticmethod
    def __load_dynamic_class(mod, dynamic_class_constructor):
        dyn_cls = dynamic_class_constructor(mod)
        dyn_cls.__qualname__ = dyn_cls.__name__
        setattr(sys.modules[dyn_cls.__module__], dyn_cls.__name__, dyn_cls)
        return dyn_cls

    def patch_module(self, mod):
        if self.patched_module is not None:
            return

        # First generate dynamic classes and replace any module classes
        for dynamic_class_spec in self.dynamic_class_specs:
            dynamic_class_constructor = dynamic_class_spec[0]
            dyn_class = self.__load_dynamic_class(mod=mod, dynamic_class_constructor=dynamic_class_constructor)
            if len(dynamic_class_spec) > 1:
                try:
                    mod.__dict__[dynamic_class_spec[1]] = dyn_class
                except:
                    pass

        # Patch functions
        for func_name, patch_func_constructor in self.patch_func_map.items():
            try:
                mod.__dict__[func_name] = patch_func_constructor(mod.__dict__[func_name])
            except:
                pass

        # Patch class methods
        for class_name, method_name, patch_func_constructor in self.class_method_patcher_spec:
            try:
                cls_obj = mod.__dict__[class_name]
                setattr(cls_obj, method_name, patch_func_constructor(getattr(cls_obj, method_name)))
            except:
                pass

        self.patched_module = mod

    def handle_post_patch(self, mod):
        self.patch_module(mod=mod)
        for module_name in self.post_patch_additional_modules:
            if module_name not in sys.modules:
                continue
            addn_mod = sys.modules[module_name]
            for dynamic_class_spec in self.dynamic_class_specs:
                try:
                    if len(dynamic_class_spec) > 1 and \
                            dynamic_class_spec[1] in addn_mod.__dict__ and \
                            inspect.isclass(addn_mod.__dict__[dynamic_class_spec[1]]):
                        addn_mod.__dict__[dynamic_class_spec[1]] = mod.__dict__[dynamic_class_spec[1]]
                except:
                    pass
            for func_name, _ in self.patch_func_map.items():
                try:
                    if func_name in addn_mod.__dict__:
                        addn_mod.__dict__[func_name] = mod.__dict__[func_name]
                except:
                    pass

    def remove_patches(self):
        for func_name, _ in self.patch_func_map.items():
            try:
                self.patched_module.__dict__[func_name] = self.patched_module.__dict__[func_name].__wrapped__
            except:
                pass


class ImportInterceptor(object):
    BuiltinImport = builtins.__import__

    def __init__(self):
        self.module_name_patchers_map = dict()

    def __handle_module_load__(self, mod):
        if mod.__name__ in self.module_name_patchers_map:
            for patcher in self.module_name_patchers_map[mod.__name__]:
                patcher.patch_module(mod)

    def __import_hook__(self, *args, **kwargs):
        mod = self.BuiltinImport(*args, **kwargs)
        self.__handle_module_load__(mod)
        return mod

    def __remove_patches__(self):
        for module_name, patchers in self.module_name_patchers_map.items():
            # remove them in reverse order
            for i in range(len(patchers)-1, -1, -1):
                patcher = patchers[i]
                patcher.remove_patches()

    def install(self):
        builtins.__import__ = self.__import_hook__

    def remove(self):
        self.__remove_patches__()
        builtins.__import__ = self.BuiltinImport

    def add_patcher_for_module(self, module_name: str, patcher: ModulePatcher):
        if module_name not in self.module_name_patchers_map:
            self.module_name_patchers_map[module_name] = list()
        self.module_name_patchers_map[module_name].append(patcher)
        # If this module is already loaded, we need to post-patch it
        if module_name in sys.modules:
            patcher.handle_post_patch(mod=sys.modules[module_name])
