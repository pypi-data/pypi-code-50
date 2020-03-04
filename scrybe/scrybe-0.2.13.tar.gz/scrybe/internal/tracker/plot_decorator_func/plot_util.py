from scrybe.internal.depgraph.nodes import ArtifactType
from scrybe.internal.tracker.data.utils import set_dataset_info_and_maybe_upload
from scrybe.internal.tracker.metrics import get_artifact_node, get_plot_artifact_node
from scrybe.internal.uploader import DataReceiver

MATPLOTLIB_FUNC_PLOT = [
    ('matplotlib.axes._axes', 'Axes.plot'),
    ('matplotlib.axes._axes', 'Axes.step'),
]

MATPLOTLIB_FUNC_X = [
    ('matplotlib.axes._axes', 'Axes.bar'),
    ('matplotlib.axes._axes', 'Axes.barh'),
    ('matplotlib.axes._axes', 'Axes.pie'),
    ('matplotlib.axes._axes', 'Axes.boxplot'),
    ('matplotlib.axes._axes', 'Axes.imshow'),
    ('matplotlib.axes._axes', 'Axes.hist'),
    ('matplotlib.axes._axes', 'Axes.psd'),
    ('matplotlib.axes._axes', 'Axes.magnitude_spectrum'),
    ('matplotlib.axes._axes', 'Axes.angle_spectrum'),
    ('matplotlib.axes._axes', 'Axes.phase_spectrum'),
    ('matplotlib.axes._axes', 'Axes.specgram'),
    ('matplotlib.axes._axes', 'Axes.spy'),
    ('matplotlib.axes._axes', 'Axes.matshow'),
    ('matplotlib.axes._axes', 'Axes.voilinplot'),
]

MATPLOTLIB_FUNC_X_Y = [
    ('matplotlib.axes._axes', 'Axes.errorbar'),
    ('matplotlib.axes._axes', 'Axes.scatter'),
    ('matplotlib.axes._axes', 'Axes.hexbin'),
    ('matplotlib.axes._axes', 'Axes.hist2d'),
    ('matplotlib.axes._axes', 'Axes.csd'),
    ('matplotlib.axes._axes', 'Axes.cohere'),
]

MATPLOTLIB_FUNC_ARANGE_TYPE = [
    ('matplotlib.axes._axes', 'Axes.stem'),
]

PANDAS_PLOT_ACCESSOR = [
    ('pandas.plotting._core', 'PlotAccessor.__call__'),  # data = self._parent
]

PANDAS_PLOT_TABLE = [
    ('pandas.plotting._misc', 'table'),  # Very similar to Axes.plot_x
]

PANDAS_PLOT_FUNC = [
    ('pandas.plotting._core', 'boxplot'),
    ('pandas.plotting._core', 'boxplot_frame'),
    ('pandas.plotting._core', 'boxplot_frame_groupby'),
    ('pandas.plotting._core', 'hist_frame'),
    ('pandas.plotting._core', 'hist_series'),
    ('pandas.plotting._misc', 'andrews_curves'),
    ('pandas.plotting._misc', 'autocorrelation_plot'),
    ('pandas.plotting._misc', 'bootstrap_plot'),
    ('pandas.plotting._misc', 'lag_plot'),
    ('pandas.plotting._misc', 'parallel_coordinates'),
    ('pandas.plotting._misc', 'radviz'),
    ('pandas.plotting._misc', 'scatter_matrix'),
]


SEABORN_FUNC_X_Y = [
    ('seaborn.relational', 'relplot'),
    ('seaborn.relational', 'scatterplot'),
    ('seaborn.relational', 'lineplot'),
    ('seaborn.regression', 'lmplot'),
    ('seaborn.regression', 'regplot'),
    ('seaborn.regression', 'residplot'),
    ('seaborn.categorical', 'catplot'),
    ('seaborn.categorical', 'factorplot'),
    ('seaborn.categorical', 'stripplot'),
    ('seaborn.categorical', 'swarmplot'),
    ('seaborn.categorical', 'boxplot'),
    ('seaborn.categorical', 'violinplot'),
    ('seaborn.categorical', 'boxenplot'),
    ('seaborn.categorical', 'lvplot'),
    ('seaborn.categorical', 'pointplot'),
    ('seaborn.categorical', 'barplot'),
    ('seaborn.categorical', 'countplot'),
    ('seaborn.distributions', 'kdeplot'),
    ('seaborn.axisgrid', 'jointplot')
]

SEABORN_FUNC_X = [
    ('seaborn.distributions', 'distplot'),
    ('seaborn.distributions', 'rugplot'),
    ('seaborn.timeseries', 'tsplot'),
    ('seaborn.matrix', 'heatmap'),
    ('seaborn.matrix', 'clustermap'),
    ('seaborn.axisgrid', 'pairplot'),
]

SEABORN_CLASS_FUNC = [
    ('seaborn.axisgrid', 'FacetGrid.map'),  # capture data dependency using self.data
    ('seaborn.axisgrid', 'PairGrid.map'),   # capture data dependency using self.data
    ('seaborn.axisgrid', 'JointGrid.map'),  # capture data dependency using self.data
]

DATASET_NAME_SETTER_CLASS_INIT = [
    ('pandas.plotting._core', 'PlotAccessor.__init__'),
    ('seaborn.axisgrid', 'FacetGrid.__init__'),
    ('seaborn.axisgrid', 'PairGrid.__init__'),
    ('seaborn.axisgrid', 'JointGrid.__init__'),
]

AXES_SETTERS = [
    'set_title',
    'set_xlabel',
    'set_ylabel',
    'set_facecolor',
    'set_axisbelow',
    'set_xticks',
    'set_xticklabels',
    'set_yticks',
    'set_yticklabels',
    'legend'
]


def create_model_artifact_if_req(datasets: list, dataset_names: list):
    for i in range(len(datasets)):
        dataset = datasets[i]
        dataset_name = dataset_names[i]
        metric_dict = {"dataset_artifact": "ignore"}
        artifact_node = get_artifact_node(y_true=dataset, y_pred=dataset, ret_val=metric_dict,
                                          object_type=ArtifactType.PLOT_IMAGE, artifact_identifier="dataset_artifact",
                                          local_name_dict={'y_pred': dataset_name, 'y_true': dataset_name})
        if artifact_node is None:
            return
        artifact_node.add_metric(metric_dict)
        DataReceiver.receive_batch(data_dict_list=artifact_node.prepare_for_upload())


def create_and_upload_plot(datasets, dataset_names, plot_func_name, fig=None):
    if fig is None:
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            return
        fig = plt.gcf()
    plot_node = get_plot_artifact_node(figure=fig, datasets=datasets, dataset_names=dataset_names)
    if plot_node is None:
        return
    plot_node.set_content(figure=fig, name=plot_func_name)
    for dataset in datasets:
        set_dataset_info_and_maybe_upload(dataset_obj=dataset)
    DataReceiver.receive_batch(data_dict_list=plot_node.prepare_for_upload())
    create_model_artifact_if_req(datasets=datasets, dataset_names=dataset_names)
