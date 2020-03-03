import functools
from .import_interceptor import ModulePatcher


def wrap_parallel_init(f):
    @functools.wraps(f)
    def wrapped_func(self, *args, **kwargs):
        f(self, *args, **kwargs)
        # hasattr(self._backend, '_workers') or self.__enter__()
        origin_init = self._backend._workers._initializer

        def scrybe_init():
            import scrybe

        def new_init():
            origin_init()
            scrybe_init()

        self._backend._workers._initializer = new_init if callable(origin_init) else scrybe_init

    return wrapped_func


def wrap_parallel_initialize_backend(f):
    @functools.wraps(f)
    def wrapped_func(self, *args, **kwargs):
        ret = f(self, *args, **kwargs)

        if hasattr(self._backend, '_workers'):
            origin_init = self._backend._workers._initializer

            def scrybe_init():
                import os
                import scrybe
                scrybe.init(project_name=os.getenv('SCRYBE_PROJECT_NAME'))
                
            def new_init():
                origin_init()
                scrybe_init()

            self._backend._workers._initializer = new_init if callable(origin_init) else scrybe_init
        return ret

    return wrapped_func


MODULE_PATCHER_MAP = {
    "joblib.parallel": ModulePatcher(
        patch_func_map=dict(),
        dynamic_class_specs=[],
        class_method_patcher_spec=[
            # ('Parallel', '__init__', wrap_parallel_init)
            ('Parallel', '_initialize_backend', wrap_parallel_initialize_backend)
        ],
        post_patch_additional_modules=['joblib']
    )
}
