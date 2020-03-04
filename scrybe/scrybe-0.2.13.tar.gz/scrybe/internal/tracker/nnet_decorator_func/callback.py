import logging

from scrybe.internal.const import KERAS_APPROACH, TRAIN_METRICS_PREFIX, VAL_METRICS_PREFIX
from scrybe.internal.tracker.metrics import get_train_metric_node, get_validation_metric_node, \
    get_eval_metric_node
from scrybe.internal.tracker.model import get_or_create_model_node
from scrybe.internal.tracker.tracker_util import handle_cv_grid_and_custom_param, upload_model_and_dataset_info
from scrybe.internal.uploader import DataReceiver
from .nnet_util import get_keras_hyperparameters, get_architecture

LOGGER = logging.getLogger("scrybe_logger")
CONTEXT_TRAIN = 'train'
CONTEXT_EVALUATE = 'test'
CONTEXT_PREDICT = 'predict'


def build_keras_callback(base, x_sample, y_sample, validation_set, metadata_dict, class_weights, local_name_dict):
    class KerasCallback(base):

        def __init__(self, x_sample=None, y_sample=None, validation_set=None, metadata_dict=None, class_weights=None,
                     local_name_dict=None):
            super(KerasCallback, self).__init__()
            self.scrybe_context = None
            self.scrybe_train_metrics = dict()
            self.scrybe_val_metrics = dict()
            self.scrybe_x_sample = x_sample
            self.scrybe_y_sample = y_sample
            self.scrybe_x_val = None
            self.scrybe_y_val = None
            self.scrybe_train_support = None
            self.scrybe_val_support = None
            self.scrybe_eval_support = None
            self.scrybe_predict_support = None
            self.scrybe_support_count_enabled = False
            if validation_set is not None and len(validation_set) >= 2:
                self.scrybe_x_val = validation_set[0]
                self.scrybe_y_val = validation_set[1]
            self.metadata_dict = metadata_dict
            self.local_name_dict = local_name_dict
            self.class_weights = class_weights

        def on_batch_begin(self, batch, logs=None):
            return

        def on_batch_end(self, batch, logs=None):
            if self.scrybe_support_count_enabled and isinstance(logs, dict):
                if 'size' in logs:
                    self.scrybe_train_support += logs['size']
            return

        def on_epoch_begin(self, epoch, logs=None):
            return

        def on_epoch_end(self, epoch, logs=None):
            try:
                self.scrybe_support_count_enabled = False
                if isinstance(logs, dict):
                    for key, value in logs.items():
                        if key.startswith(VAL_METRICS_PREFIX):
                            if key not in self.scrybe_val_metrics.keys():
                                self.scrybe_val_metrics[key] = list([0])
                            self.scrybe_val_metrics[key][0] = value
                        else:
                            key = TRAIN_METRICS_PREFIX + key
                            if key not in self.scrybe_train_metrics.keys():
                                self.scrybe_train_metrics[key] = list([0])
                            self.scrybe_train_metrics[key][0] = value
                    if self.scrybe_train_support is not None:
                        self.scrybe_train_metrics[TRAIN_METRICS_PREFIX + 'samples'] = self.scrybe_train_support
                    if self.scrybe_val_support is not None:
                        self.scrybe_val_metrics[VAL_METRICS_PREFIX + 'support'] = self.scrybe_val_support
                    if len(self.scrybe_train_metrics) > 0:
                        train_metric_node = get_train_metric_node(x_sample=self.scrybe_x_sample,
                                                                  y_sample=self.scrybe_y_sample,
                                                                  model=self.model,
                                                                  ret_val=self.scrybe_train_metrics,
                                                                  local_name_dict=self.local_name_dict)
                        if train_metric_node is not None:
                            train_metric_node.add_metric(self.scrybe_train_metrics)
                            DataReceiver.receive_batch(data_dict_list=train_metric_node.prepare_for_upload())
                            # log_upload_data_to_file(upload_data=train_metric_node.prepare_for_upload(),
                            #                         func_name="on_epoch_end_training")

                    if len(self.scrybe_val_metrics) > 0:
                        if self.scrybe_x_val is not None:
                            if 'validation_data' in local_name_dict:
                                local_name_dict['x_val'] = local_name_dict['validation_data']
                                local_name_dict['y_val'] = local_name_dict['validation_data']
                            val_metric_node = get_validation_metric_node(x_val=self.scrybe_x_val,
                                                                         y_val=self.scrybe_y_val,
                                                                         model=self.model,
                                                                         ret_val=self.scrybe_val_metrics,
                                                                         local_name_dict=local_name_dict)
                        else:
                            if 'x_sample' in local_name_dict:
                                local_name_dict['x_val'] = local_name_dict['x_sample']
                            if 'y_sample' in local_name_dict:
                                local_name_dict['y_val'] = local_name_dict['y_sample']
                            val_metric_node = get_validation_metric_node(x_val=self.scrybe_x_sample,
                                                                         y_val=self.scrybe_y_sample,
                                                                         model=self.model,
                                                                         ret_val=self.scrybe_val_metrics,
                                                                         local_name_dict=local_name_dict)
                        if val_metric_node is not None:
                            val_metric_node.add_metric(self.scrybe_val_metrics)
                            DataReceiver.receive_batch(data_dict_list=val_metric_node.prepare_for_upload())
                            # log_upload_data_to_file(upload_data=val_metric_node.prepare_for_upload(),
                            #                         func_name="on_epoch_end_validation")
            except Exception as e:
                LOGGER.error("Exception in on_epoch_end. Error: %s" % str(e))

        def on_train_batch_begin(self, batch, logs=None):
            self.on_batch_begin(batch, logs=logs)

        def on_train_batch_end(self, batch, logs=None):
            self.on_batch_end(batch, logs=logs)

        def on_test_batch_begin(self, batch, logs=None):
            return

        def on_test_batch_end(self, batch, logs=None):
            if self.scrybe_support_count_enabled and isinstance(logs, dict):
                if 'size' in logs:
                    if self.scrybe_context == CONTEXT_TRAIN:
                        self.scrybe_val_support += logs['size']
                    elif self.scrybe_context == CONTEXT_EVALUATE:
                        self.scrybe_eval_support += logs['size']
            return

        def on_predict_batch_begin(self, batch, logs=None):
            return

        def on_predict_batch_end(self, batch, logs=None):
            if self.scrybe_support_count_enabled and isinstance(logs, dict):
                if 'size' in logs:
                    self.scrybe_predict_support += logs['size']
            return

        def on_train_begin(self, logs=None):
            try:
                self.scrybe_context = CONTEXT_TRAIN
                self.scrybe_support_count_enabled = True
                self.scrybe_train_support = 0
                hyperparameters = get_keras_hyperparameters(params=self.params, model=self.model,
                                                            class_weights=self.class_weights)
                architecture = get_architecture(self.model)
                approach = KERAS_APPROACH
                model_node = get_or_create_model_node(model=self.model, x_sample=self.scrybe_x_sample,
                                                      y_sample=self.scrybe_y_sample, approach=approach,
                                                      name=self.model.name, create_new=True,
                                                      local_name_dict=local_name_dict)

                handle_cv_grid_and_custom_param(metadata_dict, self.model, model_node, self.scrybe_x_sample,
                                                hyperparameters)
                model_node.set_architecture(architecture)
                upload_model_and_dataset_info(x_train=self.scrybe_x_sample, y_train=self.scrybe_y_sample,
                                              model_obj=self.model, model_node=model_node, approach=approach)
            except Exception as e:
                LOGGER.error("Exception in on_train_begin. Error: %s" % str(e))

        def on_train_end(self, *args, **kwargs):
            self.scrybe_context = None

        def on_test_begin(self, *args, **kwargs):
            if self.scrybe_context is None:
                self.scrybe_context = CONTEXT_EVALUATE
                self.scrybe_eval_support = 0
                self.scrybe_support_count_enabled = True
            elif self.scrybe_context == CONTEXT_TRAIN and self.scrybe_val_support is None:
                self.scrybe_val_support = 0

        def on_test_end(self, *args, **kwargs):
            try:
                if self.scrybe_context != CONTEXT_EVALUATE:
                    return
                self.scrybe_context = None
                self.scrybe_support_count_enabled = False
                if self.scrybe_eval_support <= 0:
                    return
                if "x_sample" in local_name_dict:
                    local_name_dict["x_test"] = local_name_dict["x_sample"]
                if "y_sample" in local_name_dict:
                    local_name_dict["y_true"] = local_name_dict["y_sample"]
                metric_dict = {'support': self.scrybe_eval_support}
                eval_metric_tuple = get_eval_metric_node(y_true=self.scrybe_y_sample, x_test=self.scrybe_x_sample,
                                                         ret_val=self, model=self.model,
                                                         metric_names=list(metric_dict.keys()),
                                                         local_name_dict=local_name_dict)
                if eval_metric_tuple is None:
                    return
                eval_metric_node, metric_seq_dict = eval_metric_tuple
                metric_dict.update(metric_seq_dict)
                eval_metric_node.add_metric(metric_dict)
                DataReceiver.receive_batch(data_dict_list=eval_metric_node.prepare_for_upload())
                # log_upload_data_to_file(upload_data=eval_metric_node.prepare_for_upload(),
                #                         func_name="on_test_end")
            except Exception as e:
                LOGGER.error("Exception in on_test_end. Error: %s" % str(e))

        def on_predict_begin(self, *args, **kwargs):
            self.scrybe_context = CONTEXT_PREDICT
            self.scrybe_support_count_enabled = True
            self.scrybe_predict_support = 0

        def on_predict_end(self, *args, **kwargs):
            # TODO(chandra): Automatically calculate prediction latency
            self.scrybe_context = None
            self.scrybe_support_count_enabled = False

    return KerasCallback(x_sample=x_sample, y_sample=y_sample, validation_set=validation_set,
                         metadata_dict=metadata_dict, class_weights=class_weights, local_name_dict=local_name_dict)
