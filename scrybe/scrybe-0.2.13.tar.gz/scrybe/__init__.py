from typing import Union
from .internal import init

from pkg_resources import get_distribution

__version__ = get_distribution('scrybe').version


def log_code_files(filepaths: list):
    """
    Upload the code of files. Need not call this for IPython.
    IPython code is automatically captured when .fit is called on the model object.
    Code capture for vanilla python interpreter is currently not supported.

    :param filepaths: List of paths of the files that needs to be uploaded.
                    Files with extension .ipynb notebook will be ignored
    :return: None

    >>> scrybe.log_code_files(filepaths=["models/model_architecture.py", "metrics/metric_funcs.py"])
    """
    filepaths_filtered = [filepath for filepath in filepaths if not filepath.endswith(".ipynb")]
    from scrybe.internal.code_capture.source_code import CodeCapture
    CodeCapture.capture_code_files(filepaths=filepaths_filtered)


def log_custom_hyperparameter(model, param_name: str, param_value):
    """
    Log a hyperparameter of a model. CAUTION: This must be called BEFORE model.fit

    :param model: The estimator object on which fit can be called.
    :param param_name: Name of the custom hyperparameter. Must be a string
    :param param_value: Value of the custom hyperparameter. Must be a JSON Serializable object
    :return: None

    >>> knn = KNeighborsClassifier()
    >>> scrybe.log_custom_hyperparameter(knn, param_name='custom_param', param_value=float('nan'))
    >>> grid_search = GridSearchCV(knn, param_grid=knn_params, cv=2, scoring='accuracy', n_jobs=1)
    >>> grid_search.fit(x_train, y_train)
    """
    import json
    from .internal.tracker.model import add_custom_parameter
    if not isinstance(param_name, str):
        raise ValueError("param_name must be of type: str")
    try:
        json.dumps(param_value)
    except Exception:
        raise ValueError("param_value must be JSON Serializable")
    add_custom_parameter(model=model, param_name=param_name, param_value=param_value)


def log_features(model, feature_names: list):
    """
    Log feature names of a model. Feature names should be ordered in the same way in which they were fed to the model.
    CAUTION: This must be called AFTER model.fit

    :param model: The trained model object which can be used to make predictions
    :param feature_names: A list of string containing all the feature names
    :return: None

    >>> rf = RandomForestRegressor(featuresCol="features", labelCol="item_cnt_month")
    >>> rf_model = rf.fit(transformed)
    >>> scrybe.log_features(model=rf_model, feature_names=['shop_id', 'item_id', 'item_cnt', 'transactions',
    ...                                    'year', 'item_cnt_mean', 'item_cnt_std'])
    """
    if not isinstance(feature_names, list):
        raise ValueError("feature names must be of type: list where each element is a string")
    from .internal.tracker.model import set_features
    set_features(model=model, feature_names=feature_names)


def log_feature_importances(model, feature_importances: dict):
    """
    Log variable importance of a model. CAUTION: This must be called AFTER model.fit

    :param model: The trained model object which can be used to make predictions
    :param feature_importances: A dictionary of features as keys and the corresponding importance as value
    :return: None

    >>> knn = KNeighborsClassifier()
    >>> knn.fit(x_train, y_train)
    >>> scrybe.log_feature_importances(model=knn, feature_importances={'sepal-length': 0.9, 'sepal-width': 0.6,
    ...                                                                'petal-length': 0.4, 'petal-width': 0.1})
    """
    if not isinstance(feature_importances, dict):
        raise ValueError("feature_importances must be of type: dict where each key is the feature name")
    from .internal.tracker.model import set_feature_importances
    set_feature_importances(model=model, feature_importances=feature_importances)


def log_custom_model_evaluation_metric(model, x_test, y_test, param_name: str, param_value: Union[int, float, str]):
    """
    Log custom metric of a model. CAUTION: This must be called AFTER model.fit

    :param model: The trained model object which can be used to make predictions
                or the model id displayed on scrybe dashboard
    :param x_test: The test samples dataset. Must be one of Pandas Dataframe/Series, Numpy array, Spark dataframe/rdd
    :param y_test: The test labels dataset. Must be one of Pandas Dataframe/Series, Numpy array, Spark dataframe/rdd
    :param param_name: Name of the custom metric. Must be a string
    :param param_value: Value of the custom metric. Must str, int or float
    :return: None

    >>> model = keras.model.load_model("convnet_mnist.h5")
    >>> probabilities = model.predict(x_test)
    >>> probabilities[probabilities > 0.3] = 2]
    >>> probabilities[probabilities < 0.7] = 2]
    >>> probabilities[probabilities < 0.3] = 0]
    >>> probabilities[probabilities > 0.7] = 1]
    >>> cannot_classify = get_unclassified_images(probabilities, y_test)
    >>> scrybe.log_custom_model_evaluation_metric(model=model, x_test=x_test, y_test=y_test,
    ...                                           param_name="unclassified_images", param_value=cannot_classify)
    """
    if not isinstance(param_name, str):
        raise ValueError("param_name must be of type: str")
    if not isinstance(param_value, int) and not isinstance(param_value, float) and not isinstance(param_value, str):
        raise ValueError("param_value must be of one of the following types: str, float, int")
    from scrybe.internal.tracker.metrics import add_custom_model_evaluation_metric
    add_custom_model_evaluation_metric(model=model, x_test=x_test, y_test=y_test, param_name=param_name,
                                       param_value=param_value)


def log_custom_data_statistic(data, stats_name: str, stats_value: Union[int, float, str]):
    """
    Log custom dataset statistics on a dataset. CAUTION: This must be called AFTER model.fit

    :param data: Must be one of Pandas Dataframe/Series, Numpy array, Spark dataframe/rdd
    :param stats_name: Name of the custom stats. Must be a string
    :param stats_value: Value of the custom stats. Must str, int or float
    :return: None

    >>> dataset = pandas.read_csv(url, names=names)
    >>> num_frauds = get_fraud_count(dataset)
    >>> scrybe.log_custom_data_statistic(data=dataset, stats_name="num_fraud", stats_value=num_frauds)
    """
    if not isinstance(stats_name, str):
        raise ValueError("param_name must be of type: str")
    if not isinstance(stats_value, int) and not isinstance(stats_value, float) and not isinstance(stats_value, str):
        raise ValueError("param_value must be of one of the following types: str, float, int")
    from scrybe.internal.tracker.metrics import add_custom_data_stats
    add_custom_data_stats(data=data, stats_name=stats_name, stats_value=stats_value)


def set_label(label: Union[str, list, None]):
    """
    Set labels/tags on all the models, datasets and plots which helps you in filtering data in the dashboard

    :param label: Label can be string or a list of string with which you can filter in the dashboard
    :return: None

    >>> dataset = spark.read.csv("s3a://test-datasets/")
    >>> android_dataset = dataset.filter('os == "android"')
    >>> scrybe.set_label(label="android")
    >>> rf = RandomForestRegressor(featuresCol="features", labelCol="ltv")
    >>> rf_model = rf.fit(android_dataset)  ## The model gets tagged as "android"
    >>> ios_dataset = dataset.filter('os == "ios" and region == "US"')
    >>> scrybe.set_label(label=["ios", "US"])
    >>> rf = RandomForestRegressor(featuresCol="features", labelCol="ltv")
    >>> rf_model = rf.fit(ios_dataset)  ## The model gets tagged as "ios" and "US"
    """
    if label is not None and not isinstance(label, str) and not isinstance(label, list):
        raise ValueError("label must be a of type: str or list of str")
    elif isinstance(label, list):
        for val in label:
            if not isinstance(val, str) or not val:
                raise ValueError("label must be a of type: str or list of str")
    from .internal.config import Config
    if not Config.is_initialized():
        raise Exception("scrybe.init has either not been called or failed")
    Config.set_label(label=label)


def bookmark(obj, obj_name: str, msg: str):
    """
    Bookmark an object using this API and then filter in the dashboard by clicking the "Bookmarked" button

    :param obj: The object to be bookmarked. This can be a Scrybe tracked model, 
            numpy.ndarray or pandas dataframe or series, or a matplotlib figure object
    :param obj_name: The name of the object which will be displayed in the Scrybe dashboard
    :param msg: The description of why the bookmarked object is important
    :return: None

    >>> for model_pipe in models_pipe:
    >>>     model_pipe.fit(train, y)
    >>>     preds = model_pipe.predict(test)
    >>>     if round(np.sqrt(mean_squared_error(y_test, preds)), 2) <= 0.2:
    >>>         scrybe.bookmark(obj=model_pipe, obj_name="pipeline_model", msg="Shortlisted models with RMSE <= 0.2")
    """
    if obj is None:
        raise ValueError("The bookmarked object cannot be None")
    elif not isinstance(obj_name, str) or len(obj_name) == 0:
        raise ValueError("name must be a non-empty string")
    elif not isinstance(msg, str) or len(msg) == 0:
        raise ValueError("msg must be a non-empty string")
    from .internal.tracker.tracker_util import bookmark
    bookmark(obj=obj, name=obj_name, msg=msg)


def peek(obj):
    """
    Use this API to directly visit the web page with details of a given object in the dashboard

    :param obj: Can be a model or a dataset or figure object
    :return: Prints URL to stdout. If executed from notebook then loads the URL

    >>> import pandas
    >>> import matplotlib.pyplot as plt
    >>> import seaborn as sns
    >>> url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
    >>> names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
    >>> dataset = pandas.read_csv(url, names=names)
    >>> sns.boxplot('sepal-length', 'sepal-width', data=dataset)
    >>> scrybe.peek(plt.gcf())
    """
    from .internal import api_util
    return api_util.peek(obj=obj)
