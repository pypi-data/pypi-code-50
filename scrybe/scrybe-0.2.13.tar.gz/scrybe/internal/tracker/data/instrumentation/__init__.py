from .import_interceptor import ImportInterceptor
from .numpy_datasets import MODULE_PATCHER_MAP as NUMPY_PATCHER_MAP
from .pandas_datasets import MODULE_PATCHER_MAP as PANDAS_PATCHER_MAP
from .joblib_patch import MODULE_PATCHER_MAP as JOBLIB_PATCHER_MAP


ALL_PATCHER_MAPS = (NUMPY_PATCHER_MAP, PANDAS_PATCHER_MAP, JOBLIB_PATCHER_MAP)
# ALL_PATCHER_MAPS = (pandas_datasets_patcher_map, )

IMPORT_INTERCEPTOR = ImportInterceptor()


def setup_instrumentation():
    for patcher_map in ALL_PATCHER_MAPS:
        for mod_name, patcher in patcher_map.items():
            IMPORT_INTERCEPTOR.add_patcher_for_module(module_name=mod_name, patcher=patcher)
    IMPORT_INTERCEPTOR.install()

