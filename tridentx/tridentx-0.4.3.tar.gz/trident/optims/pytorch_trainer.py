import os
import sys
import matplotlib
import platform
import string
import copy
# if platform.system() not in ['Linux', 'Darwin'] and not platform.system().startswith('CYGWIN'):
#     matplotlib.use('TKAgg')
from ..misc.ipython_utils import is_in_ipython

if is_in_ipython():
    from IPython import display
import inspect
import time
import random
import string
import uuid
import torch
import torch.nn as nn

from functools import partial
import numpy as np
from ..backend.common import *
from ..backend.pytorch_backend import *
from .pytorch_optimizers import get_optimizer
from .pytorch_losses import get_loss
from .pytorch_metrics import get_metric
from .pytorch_regularizers import get_reg
from .pytorch_constraints import get_constraint
from ..misc.visualization_utils import tile_rgb_images, loss_metric_curve
from ..callbacks.lr_schedulers import get_lr_scheduler
from .trainers import ModelBase, OptimizerMixin, progress_bar
from ..data.image_common import *

__all__ = ['TrainingItem', 'Model', 'ImageClassificationModel', 'ImageDetectionModel', 'ImageGenerationModel',
           'ImageSegmentationModel']

_, term_width = get_terminal_size()
term_width = int(term_width)
TOTAL_BAR_LENGTH = 65.
last_time = time.time()
begin_time = last_time


def _to_tuple(x):
    if isinstance(x, tuple):
        return x
    elif isinstance(x, list):
        return tuple(x)
    else:
        return x,


def make_deterministic(seed: int = 19260817, cudnn_deterministic: bool = False):
    r"""Make experiment deterministic by using specific random seeds across
    all frameworks and (optionally) use deterministic algorithms.
    Args:
        seed (int): The random seed to set.
        cudnn_deterministic (bool): If `True`, set CuDNN to use
            deterministic algorithms. Setting this to `True` can negatively
            impact performance, and might not be necessary for most cases.
            Defaults to `False`.
    """

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    if cudnn_deterministic:
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


class Model(ModelBase):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(Model, self).__init__(inputs, output, input_shape)

    def _initial_graph(self, inputs=None, output=None, input_shape=None):
        if output is None:
            raise ValueError('There is at least one output')

        if inputs is None:
            if input_shape is None:
                raise ValueError('You should assign inputs or input shape')
            else:
                input_shape = to_list(input_shape)
                input_name = 'input_{0}'.format(len(self.inputs))
                self.inputs[input_name] = input_shape
        elif isinstance(inputs, Input):
            input_name = inputs.name if inputs.name != '' else 'input_{0}'.format(len(self.inputs))
            input_shape = to_numpy(inputs.input_shape).tolist()
            self.inputs[input_name] = input_shape
        elif isinstance(inputs, (tuple, list)):
            for inp in inputs:
                if isinstance(inp, Input):
                    input_name = inp.name if inp.name != '' else 'input_{0}'.format(len(self.inputs))
                    self.inputs[input_name] = to_numpy(inp.input_shape).tolist()
        elif isinstance(inputs, dict):
            for k, v in inputs.items():
                if isinstance(v, Input):
                    self.inputs[k] = to_numpy(v.input_shape).tolist()
        if isinstance(output, (Layer, nn.Module)):
            output.input_shape = input_shape
            # output.cpu()
            dummay_input = to_tensor(np.random.standard_normal((1, *input_shape)).astype(np.float32))
            out = output(dummay_input)
            self._model = output

            if isinstance(out, torch.Tensor):
                self.outputs['output'] = list(out.size())[1:]
                self.targets['target'] = list(out.size())[1:]
            else:
                for i in range(len(out)):
                    self.outputs['output_{0}'.format(i)] = list(out[i].size())[1:]
                    self.targets['target_{0}'.format(i)] = list(out[i].size())[1:]

            self.signature =get_signature(self._model.forward)
        elif isinstance(output, (list, tuple)):
            output_list = []
            for op in output:
                if isinstance(op, (Layer, nn.Module)):
                    output_list.append(op)
            dummay_input = to_tensor(np.random.standard_normal((2, *input_shape)).astype(np.float32))
            model = Combine(output_list)
            outs = model(dummay_input)
            self._model = model
            for i in range(len(outs)):
                self.outputs['output_{0}'.format(i)] = list(outs[i].size())[1:]
                self.targets['target_{0}'.format(i)] = list(outs[i].size())[1:]
            self.signature =get_signature(self._model.forward)
        else:
            raise ValueError('Invalid output')
        for name, module in self._model.named_modules():
            try:
                if hasattr(module, '_name'):
                    if name.isdigit():
                        module._name = name + '.' + module.name
                    else:
                        module._name = name
            except:
                PrintException()

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self._model.to(self.device)
        self.training_context['current_model'] = self._model

    def train(self):
        if self._model is not None and self._model.built:
            self._model.train()
        else:
            raise ValueError('There is no built model ,nothing to learn')

    def eval(self):
        if self._model is not None and self._model.built:
            self._model.eval()
        else:
            raise ValueError('There is no built model ,nothing to evaluate')

    @property
    def layers(self):
        return self._model._nodes

    def complie(self, optimizer, losses=None, metrics=None, loss_weights=None, sample_weight_mode=None,
                weighted_metrics=None, target_tensors=None):
        self.with_optimizer(optimizer)
        if losses is not None and isinstance(losses, (list, tuple)):
            for loss in losses:
                self.with_loss(loss)
        if metrics is not None and isinstance(metrics, (list, tuple)):
            for metric in metrics:
                self.with_metric(metric)

        return self

    def with_optimizer(self, optimizer, **kwargs):
        if isinstance(optimizer, str):
            optimizer_class = get_optimizer(optimizer)
            self.optimizer = optimizer_class(self._model.parameters(), **kwargs)

        else:
            self.optimizer = optimizer(self._model.parameters(), **kwargs)
        # self.lr_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(self.optimizer, verbose=True, mode='min',
        #                                                                factor=0.5, patience=5, threshold=1e-4,
        #                                                                cooldown=0, min_lr=1e-10, eps=1e-8)
        self.base_lr = kwargs.get('lr', kwargs.get('learning_rate', 1e-3))
        self.training_context['optimizer'] = self.optimizer
        self.training_context['base_lr'] = self.base_lr
        self.training_context['current_lr'] = self.base_lr
        return self

    def with_loss(self, loss, loss_weight=1, output_idx=0, name='', **kwargs):
        if isinstance(loss, str):
            loss = get_loss(loss)
        alias = name
        if inspect.isclass(loss):
            alias = loss.__name__ if len(alias) == 0 else alias
        if len(alias) == 0 and hasattr(loss, '__name__'):
            alias = loss.__name__
        self.loss_weights[alias] = loss_weight

        argnames=[]
        if hasattr(loss, 'forward'):
            self._losses[alias] = loss(**kwargs)
            if hasattr(self._losses[alias], 'reduction'):
                setattr(self._losses[alias], 'reduction', 'mean')
            if hasattr(self._losses[alias], 'size_average'):
                setattr(self._losses[alias], 'size_average', 'True')
            argnames=get_signature(self._losses[alias].forward)
        elif callable(loss):
            if inspect.isfunction(loss):
                spec = inspect.getfullargspec(loss)
                if len(spec.args) >= 2 and len(spec.args) - 0 if spec.defaults is None else len(spec.defaults) == 2 and  (spec.args[0] in ['output',  'y_pred','pred'] or  'target_'+spec.args[0]==spec.args[1]):
                    self._losses[alias] = loss
                else:
                    self._losses[alias] = partial(loss, **kwargs)
            argnames = get_signature(self._losses[alias])

        output_idx=list(output_idx) if isinstance(output_idx,(list,tuple)) else [output_idx]
        if len(output_idx) == 1:
            out = self.outputs.key_list[output_idx[0]]
            target = self.targets.key_list[output_idx[0]]

        self._losses[alias].signature = argnames
        print('{0} signature:{1}'.format(alias, self._losses[alias].signature.key_list))
        return self

    def with_metric(self, metric, output_idx=0, name='', **kwargs):
        if isinstance(metric, str):
            metric = get_metric(metric)

        alias = name
        if inspect.isfunction(metric):
            alias = metric.__name__ if len(alias) == 0 else alias
        if len(alias) == 0 and hasattr(metric, 'name'):
            alias = metric.name
        if hasattr(metric, 'forward'):
            self._metrics[alias] = metric( **kwargs)  # if hasattr(self._metrics[metric.__name__], 'reduction'):  #     setattr(self._metrics[metric.__name__], 'reduction', 'mean')
        elif callable(metric):
            self._metrics[alias] = partial(metric, **kwargs)
        argnames = get_signature(self._metrics[alias])
        output_idx = list(output_idx) if isinstance(output_idx, (list, tuple)) else [output_idx]

        if len(output_idx)==1:
            out = self.outputs.key_list[output_idx[0]]
            target = self.targets.key_list[output_idx[0]]

        self._metrics[alias].signature  = argnames
        print('{0} signature:{1}'.format(alias, self._metrics[alias].signature.key_list))


        return self

    def with_regularizer(self, reg, **kwargs):
        if reg is None:
            return self
        reg_fn = None
        if isinstance(reg, str):
            reg_fn = get_reg(reg)
        elif reg is callable:
            reg_fn = reg
        args = reg_fn.__code__.co_varnames
        if 'reg_weight' in args:
            if 'model' in args:
                self._model_regs[reg_fn.__name__] = partial(reg_fn, **kwargs)
            elif 'output' in args:
                self._output_regs[reg_fn.__name__] = partial(reg_fn, **kwargs)
        return self

    def with_constraint(self, constraint, **kwargs):
        if constraint is None:
            return self
        constraint_fn = None
        if isinstance(constraint, str):
            constraint_fn = get_constraint(constraint)

        if hasattr(constraint_fn, 'forward') and constraint_fn.__name__[-4:] == 'norm':
            self._constraints[constraint_fn.__name__] = constraint_fn(**kwargs)

        elif callable(constraint_fn) and constraint_fn.__name__[-4:] == 'norm':
            self._constraints[constraint_fn.__name__] = partial(constraint_fn, **kwargs)

        return self

    def with_model_save_path(self, save_path, **kwargs):
        self.save_path = make_dir_if_need(save_path)
        self.training_context['save_path'] = self.save_path
        return self

    def with_learning_rate_scheduler(self, lr_schedule, warmup=0, **kwargs):
        if lr_schedule is None:
            return self
        if isinstance(lr_schedule, str):
            lr_schedule = get_lr_scheduler(lr_schedule)
        if callable(lr_schedule):
            lr_scheduler = lr_schedule(**kwargs)
            self.callbacks.append(lr_scheduler)
        self.warmup = warmup
        if self.warmup > 0:
            self.optimizer.adjust_learning_rate(1e-5, False)
            self.training_context['current_lr'] = 1e-5
        return self

    def adjust_learning_rate(self, lr):
        self.optimizer.param_groups[0]['lr'] = lr
        self.training_context['current_lr'] = lr

    def rebinding_input_output(self, input_shape):
        if input_shape == self._model._input_shape:
            pass
        else:
            if len(self.inputs) == 1:
                input_shape_list = to_numpy(input_shape).tolist()
                self._model.input_shape = input_shape_list
                self.inputs[self.inputs.key_list[0]] = input_shape_list

            dummay_input = to_tensor(np.random.standard_normal((2, *input_shape_list))).to(
                torch.device("cuda" if self._model.weights[0].data.is_cuda else "cpu")).to(
                self._model.weights[0].data.dtype)
            out = self._model(dummay_input)
            if isinstance(out, torch.Tensor) == len(self.targets) == 1:
                self.targets[self.targets.key_list[0]] = list(out.size())[1:] if len(out.size()) > 1 else []
                self._model.output_shape = out.size()[1:]
            elif isinstance(out, tuple) :
                for k in range(len(out)):
                    self.targets[self.targets.key_list[k]] = list(out[k].size())[1:] if len(out[k].size()) > 1 else []


    def do_on_training_start(self):
        self._model.train()
        self._model.zero_grad()

    def do_on_training_end(self):
        self._model.eval()

    def do_on_epoch_start(self):
        # if self.training_context['current_epoch'] < self.warmup:
        #     lr = 1e-5 * (self.training_context['current_epoch'] + 1)
        #     self.optimizer.param_groups[0]['lr'] = lr
        #     self.training_context['current_lr'] = lr
        # elif self.training_context['current_epoch'] == self.warmup:
        #     self.optimizer.param_groups[0]['lr'] = self.base_lr
        #     self.training_context['current_lr'] =self.base_lr
        if self.device == 'cuda':
            torch.cuda.empty_cache()

    def do_on_epoch_end(self):
        pass  # if self.training_context['current_epoch'] > self.warmup:  #     if self.lr_scheduler is not None:  #         self.lr_scheduler.step(np.array(self.training_context['metrics'][list(self._metrics.keys())[0]]).mean())  #         self.training_context['current_lr'] = self.optimizer.lr  #     if self.optimizer.param_groups[0]['lr'] < 1e-8:  #         self.optimizer.param_groups[0]['lr'] = 0.05 * self.base_lr  #         self.training_context['current_lr'] =  0.05 * self.base_lr  # elif  self.warmup>0 and self.training_context['current_epoch'] == self.warmup:  #     self.optimizer.adjust_learning_rate(self.base_lr, True)  #     self.training_context['current_lr'] =self.base_lr  # elif   self.warmup>0 and self.training_context['current_epoch'] < self.warmup:  #     self.optimizer.adjust_learning_rate(1e-5*(self.training_context['current_epoch']+1), True)  #     self.training_context['current_lr'] = 1e-5*(self.training_context['current_epoch']+1)

    def do_on_batch_start(self):
        pass

    def do_on_batch_end(self):
        if self.training_context['current_batch'] == 0 :
            temp=OrderedDict()
            for k in self.training_context['losses'].key_list:
                temp[k]=self.training_context['losses'][k][-1]
            print(temp)

    def do_on_data_received(self, train_data, test_data):

        # fields=train_data._fields
        # for i in range(len(fields)):

        if 'data_feed' not in self.training_context or len(self.training_context['data_feed']) == 0:
            try:
                data_feed = OrderedDict()
                inshapes = self.inputs.value_list
                outshapes = self.targets.value_list
                available_fields = copy.deepcopy(train_data.key_list)
                if train_data is not None:
                    # check input

                    for arg in self.signature.key_list:
                        data_feed[arg] = ''
                    for arg in self.signature.key_list:
                        if len(train_data) == 1:
                            data_feed[arg] = train_data.key_list[0]
                            available_fields.remove(train_data.key_list[0])
                        elif arg in available_fields:
                            data_feed[arg] = arg
                            available_fields.remove(arg)
                        elif arg=='x' and 'data' in available_fields:
                            data_feed[arg] = 'data'
                            available_fields.remove( 'data' )
                        elif arg=='x' and 'input' in available_fields:
                            data_feed[arg] = 'input'
                            available_fields.remove( 'input' )
                        elif len(self.signature.key_list) == 1:
                            for item in available_fields:
                                data_shape = list(train_data[item].shape[1:]) if len(train_data[item].shape) > 1 else []
                                if 'target' not in item and 'output' != item and data_shape == inshapes[0]:
                                    data_feed[arg] = item
                                    available_fields.remove(item)
                                    break
                        else:
                            Warning(
                                'input argment {0} cannot mapping to any data, please check it and update the datafeed'.format(
                                    arg))

                    # check for target
                    for i in range(len(self.targets)):
                        arg = self.targets.key_list[i]
                        data_feed[arg] = ''
                        if len(train_data) == 1:
                            data_feed[self.targets.key_list[0]] = train_data.key_list[0]
                        elif arg in available_fields:
                            data_feed[arg] = arg
                            available_fields.remove(arg)
                        elif arg=='target' and 'label' in available_fields:
                            data_feed[arg] = 'label'
                            available_fields.remove( 'label' )
                        elif arg=='target' and len(available_fields)==1:
                            data_feed[arg] =available_fields[0]
                            available_fields.remove( available_fields[0])
                        elif len(available_fields) > 0:
                            target_shape = outshapes[i]
                            for item in available_fields:
                                data_shape = list(train_data[item].shape[1:]) if len(train_data[item].shape) > 1 else []
                                if target_shape == data_shape:
                                    data_feed[arg] = item
                                    available_fields.remove(item)
                                elif ('int64' in str(train_data[item].dtype) or 'int32' in str(
                                        train_data[item].dtype)) and target_shape[:-1] == data_shape:
                                    data_feed[arg] = item
                                    available_fields.remove(item)
                                else:
                                    Warning(
                                        'target argment {0} cannot mapping to any data, please check it and update the datafeed'.format(
                                            arg))

                    self.training_context['data_feed'] = data_feed
            except:
                PrintException()

        # convert to tensor
        try:
            data_feed=self.training_context['data_feed']
            input_list=[data_feed[arg] for arg in self.signature.key_list]
            for item in train_data.key_list:
                if item in input_list:
                    #only model 's input argments
                    train_data[item] = to_tensor(train_data[item],requires_grad=True)
                else:
                    train_data[item] = to_tensor(train_data[item])
                if test_data is not None:
                    test_data[item] = to_tensor(test_data[item])

                    # check target
        except:
            PrintException()
        return train_data, test_data

    def do_preparation_for_loss(self):
        # self._model.zero_grad()
        self.optimizer.zero_grad()

    def get_current_loss(self):
        return self.training_context['current_loss']

    def do_gradient_update(self, log_gradients=False, keep_gradients_history=False):

        self.training_context['current_loss'].backward(retain_graph=self.training_context['retain_graph'])

        for callback in self.training_context['callbacks']:
            callback.on_optimization_step_start(self.training_context)

        if keep_gradients_history:
            self.log_gradient(keep_gradients_history)

        if self.training_context['stop_update'] == 0:
            self.optimizer.step(self.get_current_loss)
        elif 0 < self.training_context['stop_update'] < 1:
            if random.random() <= self.training_context['stop_update']:
                self.optimizer.step(self.get_current_loss)
        else:
            self.training_context['stop_update'] = self.training_context['stop_update'] - 1

        for callback in self.training_context['callbacks']:
            callback.on_optimization_step_end(self.training_context)

    def do_on_progress_end(self):
        if self.training_context['current_epoch'] > self.warmup:
            if self.lr_scheduler is not None:
                self.lr_scheduler.step(np.array(self.training_context['metrics'][list(self._metrics.keys())[0]]).mean())
                self.training_context['current_lr'] = self.optimizer.lr

    def log_gradient(self, grads=None, keep_gradients_history=False):
        grad_dict = {}

        for i, (k, v) in enumerate(self._model.named_parameters()):
            grad_dict[k] = to_numpy(v.grad)

        if keep_gradients_history:
            self.gradients_history.append(grad_dict)

    def log_weight(self, weghts=None, keep_weghts_history=False):
        weight_dict = {}
        for k, v in self._model.named_parameters():
            weight_dict[k] = to_numpy(v.data)
        if keep_weghts_history:
            self.weights_history.append(weight_dict)

    def save_model(self, save_path=None):
        for callback in self.training_context['callbacks']:
            callback.on_start_save_model(self.training_context)
        self._model.eval()
        if save_path is None or len(save_path) == 0:
            save_path = self.training_context.get('save_path', self.save_path)
            if save_path is None or len(save_path) == 0:
                save_path = 'Models/model_{0}_epoch{1}.pth'.format(self._model.name,
                                                                   self.training_context['current_epoch'])
        torch.save({'state_dict': self._model.state_dict()}, save_path + '.tar')
        self._model.train()

    def save_onnx(self, file_path, dynamic_axes=None):
        import torch.onnx
        self._model.eval()
        dummy_input = torch.randn(1, *self._model.input_shape.tolist(),
                                  device="cuda" if self._model.weights[0].data.is_cuda else "cpu")
        file, ext = os.path.splitext(file_path)
        if ext is None or ext != '.onnx':
            file_path = os.path.join(file, '.onnx')

        outputs = self._model(dummy_input)
        if isinstance(outputs, torch.Tensor):
            outputs = (outputs,)
        output_names = ['output_{0}'.format(i) for i in range(len(outputs))]
        if dynamic_axes is None:
            dynamic_axes = {}
            for inp in self.inputs.key_list:
                dynamic_axes[inp] = {0: 'batch_size'}
            for out in output_names:
                dynamic_axes[out] = {0: 'batch_size'}
        torch.onnx.export(self._model,  # model being run
                          dummy_input,  # model input (or a tuple for multiple inputs)
                          file_path,  # where to save the model (can be a file or file-like object)
                          export_params=True,  # store the trained parameter weights inside the model file
                          opset_version=10,  # the ONNX version to export the model to
                          do_constant_folding=True,  # whether to execute constant folding for optimization
                          input_names=self.inputs.key_list,  # the model's input names
                          output_names=output_names,  # the model's output names
                          dynamic_axes=dynamic_axes)
        self._model.train()

    def load_model(self, file_path):
        print('Loading pretrained model from {}'.format(file_path))
        pretrained_dict = torch.load(file_path, map_location=lambda storage, loc: storage)


        if "state_dict" in pretrained_dict.keys():
            pretrained_dict = pretrained_dict['state_dict']
        # else:
        #     pretrained_dict = remove_prefix(pretrained_dict, 'module.')
        if check_keys(self._model, pretrained_dict):
            self._model.load_state_dict(pretrained_dict, strict=False)
            print('Model loaded!')

        if self.signature is None:
            self.signature = get_signature(self._model.forward)


    def summary(self):
        #self.rebinding_input_output(self._model.input_shape)
        summary(self._model, tuple(self._model.input_shape))

    def extra_repr(self):
        return ''

    def __str__(self):
        self.__repr__()

    def _get_name(self):
        return self.__class__.__name__

    def __repr__(self):
        # We treat the extra repr like the sub-module, one item per line
        extra_lines = []
        extra_repr = self.extra_repr()
        # empty string will be split into list ['']
        if extra_repr:
            extra_lines = extra_repr.split('\n')
        child_lines = []
        for key, value in self.__dict__.items():
            if isinstance(value, OrderedDict):
                for subkey, subvalue in value.items():
                    mod_str = repr(subvalue)
                    mod_str = addindent(mod_str, 2)
                    child_lines.append('(' + key + '): ' + mod_str)
            else:
                mod_str = repr(value)
                mod_str = addindent(mod_str, 2)
                child_lines.append('(' + key + '): ' + mod_str)
        lines = extra_lines + child_lines

        main_str = self._get_name() + '('
        if lines:
            # simple one-liner info, which most builtin Modules will use
            if len(extra_lines) == 1 and not child_lines:
                main_str += extra_lines[0]
            else:
                main_str += '\n  ' + '\n  '.join(lines) + '\n'

        main_str += ')'
        return main_str

    def __dir__(self):
        module_attrs = dir(self._model.__class__)
        optimizer_attrs = dir(self.optimizer.__class__)
        attrs = list(self.__dict__.keys())
        losses = list(self._losses.keys())
        metrics = list(self._metrics.keys())
        output_regs = list(self._output_regs.keys())
        model_regs = list(self._model_regs.keys())
        constraints = list(self._constraints.keys())
        keys = module_attrs + optimizer_attrs + attrs + losses + metrics + output_regs + model_regs + constraints
        # Eliminate attrs that are not legal Python variable names
        keys = [key for key in keys if not key[0].isdigit()]

        return sorted(keys)


class ImageClassificationModel(Model):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(ImageClassificationModel, self).__init__(inputs, output, input_shape)

        self._class_names = []
        self.preprocess_flow = []

        self._idx2lab = {}
        self._lab2idx = {}

    @property
    def class_names(self):
        return self._class_names

    @class_names.setter
    def class_names(self, value):
        if self._class_names != value:
            self._class_names = value
            self._lab2idx = {v: k for k, v in enumerate(self._class_names)}
            self._idx2lab = {k: v for k, v in enumerate(self._class_names)}

    @property
    def reverse_preprocess_flow(self):
        return_list = []
        return_list.append(reverse_image_backend_adaptive)
        for i in range(len(self.preprocess_flow)):
            fn = self.preprocess_flow[-1 - i]
            if fn.__qualname__ == 'normalize.<locals>.img_op':
                return_list.append(unnormalize(fn.mean, fn.std))
        return_list.append(array2image)
        return return_list

    def index2label(self, idx: int):
        if self._idx2lab is None or len(self._idx2lab.items()) == 0:
            raise ValueError('You dont have proper mapping class names')
        elif idx not in self._idx2lab:
            raise ValueError('Index :{0} is not exist in class names'.format(idx))
        else:
            return self._idx2lab[idx]

    def label2index(self, label):
        if self._lab2idx is None or len(self._lab2idx.items()) == 0:
            raise ValueError('You dont have proper mapping class names')
        elif label not in self._lab2idx:
            raise ValueError('label :{0} is not exist in class names'.format(label))
        else:
            return self._lab2idx[label]

    def infer_single_image(self, img, topk=1):
        if self._model.built:
            self._model.eval()
            img = image2array(img)
            if img.shape[-1] == 4:
                img = img[:, :, :3]

            for func in self.preprocess_flow:
                if inspect.isfunction(func) and func is not image_backend_adaptive:
                    img = func(img)
            img = image_backend_adaptive(img)
            inp = to_tensor(np.expand_dims(img, 0)).to(
                torch.device("cuda" if self._model.weights[0].data.is_cuda else "cpu")).to(
                self._model.weights[0].data.dtype)
            result = self._model(inp)
            result = to_numpy(result)[0]

            # argresult = np.argsort(result)
            # argresult1 =argresult[::-1]
            answer = OrderedDict()
            idxs = list(np.argsort(result)[::-1][:topk])
            for idx in idxs:
                prob = result[idx]
                answer[self.index2label(idx)] = (idx, prob)
            # idx=int(np.argmax(result,-1)[0])

            return answer
        else:
            raise ValueError('the model is not built yet.')


class ImageDetectionModel(Model):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(ImageDetectionModel, self).__init__(inputs, output, input_shape)
        self.preprocess_flow = []
        self.detection_threshould = 0.5

    @property
    def reverse_preprocess_flow(self):
        return_list = []
        for i in range(len(self.preprocess_flow)):
            fn = self.preprocess_flow[-1 - i]
            if fn.__qualname__ == 'normalize.<locals>.img_op':
                return_list.append(unnormalize(fn.mean, fn.std))
        return return_list

    def infer_single_image(self, img, scale=1):
        if self._model.built:
            self._model.to(self.device)
            self._model.eval()
            img = image2array(img)
            if img.shape[-1] == 4:
                img = img[:, :, :3]

            for func in self.preprocess_flow:
                if inspect.isfunction(func):
                    img = func(img)
            img = image_backend_adaptive(img)
            inp = to_tensor(np.expand_dims(img, 0)).to(torch.device("cuda" if self._model.weights[0].data.is_cuda else "cpu")).to(self._model.weights[0].data.dtype)
            result = self._model(inp)

            bboxes = self.generate_bboxes(*result, threshould=self.detection_threshould, scale=scale)
            bboxes = self.nms(bboxes)
            # idx=int(np.argmax(result,-1)[0])
            return bboxes
        else:
            raise ValueError('the model is not built yet.')

    def generate_bboxes(self, *outputs, threshould=0.5, scale=1):
        raise NotImplementedError

    def nms(self, bboxes):
        raise NotImplementedError


class ImageSegmentationModel(Model):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(ImageSegmentationModel, self).__init__(inputs, output, input_shape)
        self.preprocess_flow = []


class ImageGenerationModel(Model):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(ImageGenerationModel, self).__init__(inputs, output, input_shape)
        self.preprocess_flow = []

    @property
    def reverse_preprocess_flow(self):
        return_list = []
        for i in range(len(self.preprocess_flow)):
            fn = self.preprocess_flow[-1 - i]
            if fn.__qualname__ == 'normalize.<locals>.img_op':
                return_list.append(unnormalize(fn.mean, fn.std))
        return return_list

    def infer_single_image(self, img):
        if self._model.built:
            self._model.to(self.device)
            self._model.eval()
            if isinstance(img, np.ndarray) and img.ndim < 2:
                pass
            else:
                img = image2array(img)
                if img.shape[-1] == 4:
                    img = img[:, :, :3]

                for func in self.preprocess_flow:
                    if inspect.isfunction(func):
                        img = func(img)

            result = self._model(to_tensor(np.expand_dims(img, 0)))

            for func in self.reverse_preprocess_flow:
                if inspect.isfunction(func):
                    img = func(img)
            img = array2image(img)
            return img


class LanguageModel(Model):
    def __init__(self, inputs=None, output=None, input_shape=None):
        super(LanguageModel, self).__init__(inputs, output, input_shape)
        self.preprocess_flow = []


TrainingItem = Model






