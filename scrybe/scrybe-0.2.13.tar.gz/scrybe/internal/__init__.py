from __future__ import print_function

PROJECT_INFO = None
USER_INFO = None
HOST_URL = None
DASHBOARD_SERVER_ADDR = None

import os
import sys

from .auth import authenticate
from .commons import init_internal_logging
from .patcher import ScrybePatcher
from .tracker.data import init_data_tracking
from .tracker.nnet_decorator_func.keras_tracker import patch as keras_patch
from .tracker.nnet_decorator_func.tensorboard_tracker import patch as tb_patch
from .tracker.nnet_decorator_func.tensorflow_tracker import patch as tf_patch
from .tracker.save_and_load_tracker import patch as loader_patch
from .tracker.sklearn_decorator_func.sklearn_tracker import patch as sklearn_patch
from .tracker.xgb_decorator_func.xgb_tracker import patch as xgb_patch
from .tracker.plot_decorator_func.plot_tracker import patch as plot_patch
from .tracker.stats_decorator_func.stats_tracker import patch as stats_patch
from .tracker.data.instrumentation.spark_dataset import patch as spark_dataset_patch
from .tracker.data.instrumentation.catboost_pool import patch as catboost_pool_patch
from .tracker.pyspark_decorator_func.pyspark_tracker import patch as spark_ml_patch
from .uploader import init_module as init_uploader_module
from .code_capture.source_code import CodeCapture


def setup():
    modules_to_patch = [
        ('pyspark', "pyspark models and datasets"),
        ('sklearn', "sklearn models"),
        ('keras', "keras models"),
        ('xgboost', "xgboost models"),
        ('lightgbm', "lightgbm models"),
        ('catboost', "catboost models"),
        # ('tensorflow', "tensorflow models"),
        # ('tensorboard', "tensorboard logs"),
        ('pickle', "paths of models and dataset saved or loaded using pickle"),
        ('joblib', "model path of models saved using joblib"),
        ('pandas', "pandas plots"),
        ('numpy', "numpy stats"),
        ('matplotlib', "matplotlib plots"),
        ('seaborn', "seaborn plots"),
        ('h5py', "paths for datasets loaded from h5py"),
    ]

    sys_module_keys = sys.modules.keys()

    already_imported = [module_to_patch for module_to_patch, msg in modules_to_patch if
                        module_to_patch in sys_module_keys]

    # Activate the monkey patching
    patcher_obj = ScrybePatcher()
    loader_patch(patcher_obj)
    sklearn_patch(patcher_obj)
    xgb_patch(patcher_obj)
    keras_patch(patcher_obj)
    plot_patch(patcher_obj)
    stats_patch(patcher_obj)
    spark_dataset_patch(patcher_obj)
    catboost_pool_patch(patcher_obj)
    spark_ml_patch(patcher_obj)
    # tb_patch(patcher_obj)
    # tf_patch(patcher_obj)
    # pytorch_patch(patcher_obj)
    for module_name in already_imported:
        patcher_obj.patch_already_imported_modules(module_name=module_name)
    patcher_obj.start()

    init_data_tracking()
    CodeCapture.init_zeppelin_code()


def init(project_name: str,
         user_access_key: str = None,
         host_url: str = None):
    if user_access_key is None:
        user_access_key = os.getenv('SCRYBE_USER_KEY')
    if host_url is None:
        host_url = os.getenv('SCRYBE_SERVER_HOST')
    if user_access_key is None or host_url is None:
        home_dir = os.path.expanduser('~')
        fname = '%s/.scrybeenv' % home_dir
        if os.path.exists(fname):
            with open(fname) as f:
                lines = f.readlines()
                for line in lines:
                    line = line.strip()
                    if '=' in line:
                        key, val = line.split('=')
                        if key == 'SCRYBE_USER_KEY':
                            user_access_key = val
                        elif key == 'SCRYBE_SERVER_HOST':
                            host_url = val
        if user_access_key is None:
            raise ValueError('ensure SCRYBE_USER_KEY is set as an env var or is there in '
                             '.scrybeenv in your home dir %s or you provide user_access_key in the arg of init call' % home_dir)
        if host_url is None:
            raise ValueError('ensure SCRYBE_SERVER_HOST is set as an env var or is there in '
                             '.scrybeenv in your home dir %s or you provide host_url in the arg of init call' % home_dir)

    global PROJECT_INFO
    global USER_INFO
    global HOST_URL
    global DASHBOARD_SERVER_ADDR
    HOST_URL = host_url
    auth_response = authenticate(host_url=host_url, user_access_key=user_access_key, project_name=project_name)
    if auth_response is None:
        raise ValueError("Authentication failed")

    PROJECT_INFO, USER_INFO, DASHBOARD_SERVER_ADDR = auth_response
    os.environ['SCRYBE_PROJECT_NAME'] = PROJECT_INFO['name']
    init_uploader_module(host_url=HOST_URL, project_info=PROJECT_INFO, user_info=USER_INFO)
    from .uploader import LOG_QUEUE
    init_internal_logging(logger_name='scrybe_logger', log_queue=LOG_QUEUE)
    from .config import init_config
    init_config(project_info=PROJECT_INFO, dashboard_server_url=DASHBOARD_SERVER_ADDR)


setup()
