import warnings
import math
import numpy as np
import os
import sys
from  ..callbacks import CallbackBase
from ..backend.common import *
from ..backend.load_backend import get_backend
from ..backend.pillow_backend import image2array
from ..misc.ipython_utils import is_in_ipython,is_in_colab

if is_in_ipython():
    from IPython import display

from ..misc.visualization_utils import *
_session=get_session()
_backend=get_backend()

if get_backend()=='pytorch':
    from ..backend.pytorch_backend import to_numpy,to_tensor
    from ..backend.pytorch_ops import *
elif get_backend()=='tensorflow':
    from ..backend.tensorflow_backend import  to_numpy,to_tensor
elif get_backend()=='cntk':
    from ..backend.cntk_backend import  to_numpy,to_tensor


__all__ = ['VisualizationCallbackBase','TileImageCallback','PrintGradientsCallback','SegTileImageCallback','PlotLossMetricsCallback']

class VisualizationCallbackBase(CallbackBase):
    def __init__(self,epoch_inteval,batch_inteval,save_path: str = None, imshow=False):
        super(VisualizationCallbackBase, self).__init__()
        self.is_in_ipython=is_in_ipython()
        self.is_in_colab=is_in_colab()
        self.epoch_inteval=epoch_inteval
        self.batch_inteval=batch_inteval
        if save_path is None:
            save_path='results'
        self.save_path=make_dir_if_need(save_path)
        self.imshow = imshow
    pass


class TileImageCallback(VisualizationCallbackBase):
    def __init__(self,epoch_inteval=-1,batch_inteval=-1,save_path: str = 'results',
                                      name_prefix: str = 'tile_image_{0}.png', include_input=True, include_output=True,
                                      include_target=True, include_mask=None, imshow=False):
        super(TileImageCallback,self).__init__(epoch_inteval,batch_inteval,save_path,imshow)
        self.is_in_ipython=is_in_ipython()
        self.is_in_colab=is_in_colab()
        self.tile_image_name_prefix = name_prefix

        self.include_input = include_input
        self.include_output = include_output
        self.include_target = include_target
        self.include_mask = include_mask

    def plot_tile_image(self,training_context):
        tile_images_list=[]
        input=training_context['current_input']
        target=training_context['current_target']
        output = training_context['current_output']

        if self.include_input:
            input_arr = to_numpy(input).transpose([0, 2, 3, 1]) if get_backend() != 'tensorflow' else to_numpy(input)
            tile_images_list.append(input_arr * 127.5 + 127.5)
        if self.include_target:
            target_arr = to_numpy(target).transpose([0, 2, 3, 1]) if get_backend() != 'tensorflow' else to_numpy(target)
            tile_images_list.append(target_arr * 127.5 + 127.5)
        if self.include_output:
            output_arr = to_numpy(output).transpose([0, 2, 3, 1]) if get_backend() != 'tensorflow' else to_numpy(output)
            tile_images_list.append(output_arr * 127.5 + 127.5)

        # if self.tile_image_include_mask:
        #     tile_images_list.append(input*127.5+127.5)
        tile_rgb_images(*tile_images_list,save_path=os.path.join(self.save_path, self.tile_image_name_prefix ), imshow=True)

    def on_batch_end(self, training_context):
        if self.batch_inteval > 0 and (training_context['current_batch'] + 1) % self.batch_inteval == 0:
            self.plot_tile_image(training_context)

    def on_epoch_end(self, training_context):
        if self.epoch_inteval>0 and (training_context['current_epoch']+1)%self.epoch_inteval==0:
            self.plot_tile_image(training_context)

class SegTileImageCallback(VisualizationCallbackBase):
    def __init__(self,epoch_inteval=-1,batch_inteval=-1,save_path: str = 'results',reverse_image_transform=None,background=(120,120,120),
                                      name_prefix: str = 'segtile_image_{0}.png', imshow=False):
        super(SegTileImageCallback,self).__init__(epoch_inteval,batch_inteval,save_path,imshow)
        self.is_in_ipython=is_in_ipython()
        self.is_in_colab=is_in_colab()
        self.tile_image_name_prefix = name_prefix
        self.reverse_image_transform=reverse_image_transform
        self.background=np.expand_dims(np.expand_dims(to_numpy(background),0),0)



    def plot_tile_image(self,training_context):
        tile_images_list=[]
        input=training_context['current_input']
        target=training_context['current_target']
        output = argmax(training_context['current_output'].clone(),1)


        input_arr =[]
        inp=to_numpy(input)
        for i in range(len(inp)):
            input_arr.append(self.reverse_image_transform(inp[i]))
        #input_arr=np.asarray(input_arr)
        tile_images_list.append(input_arr)

        target_arr = np.expand_dims(to_numpy(target),-1)
        target_arr[target_arr>0]=1

        background=np.ones_like(target_arr)*self.background

        tile_images_list.append(target_arr*input_arr+(1-target_arr)*background)

        output_arr = np.expand_dims(to_numpy(output),-1)
        output_arr[output_arr > 0] = 1
        tile_images_list.append(output_arr*input_arr+(1-output_arr)*background)

        # if self.tile_image_include_mask:
        #     tile_images_list.append(input*127.5+127.5)
        tile_rgb_images(*tile_images_list,save_path=os.path.join(self.save_path, self.tile_image_name_prefix ), imshow=True)

    def on_batch_end(self, training_context):
        if self.batch_inteval > 0 and (training_context['current_batch'] + 1) % self.batch_inteval == 0:
            self.plot_tile_image(training_context)

    def on_epoch_end(self, training_context):
        if self.epoch_inteval>0 and (training_context['current_epoch']+1)%self.epoch_inteval==0:
            self.plot_tile_image(training_context)

class PlotLossMetricsCallback(VisualizationCallbackBase):
    def __init__(self,epoch_inteval=-1,batch_inteval=-1,save_path: str = 'results',clean_ipython_output_frequency=5,
                                      name_prefix: str = 'loss_metric_curve_{0}.png', imshow=False):
        super(PlotLossMetricsCallback,self).__init__(epoch_inteval,batch_inteval,save_path,imshow)
        self.training_items=None
        self.name_prefix=name_prefix

        self.is_shared=True
        self.loss_history_list=[]
        self.metric_history_list = []
        self.counter=0
        self.clean_ipython_output_frequency=clean_ipython_output_frequency



    def on_training_start(self, training_context):
        self.training_items = training_context['training_items']


    def on_overall_batch_end(self, training_context):
        if self.batch_inteval > 0 and (self.training_items.value_list[0].training_context['current_batch'] + 1) % self.batch_inteval == 0:
            if is_in_ipython() and self.counter==self.clean_ipython_output_frequency:
                display.clear_output(wait=True)
                self.counter=0
            self.loss_history_list = []
            self.metric_history_list = []
            for trainitem in self.training_items.value_list:
                self.loss_history_list.append(trainitem.batch_loss_history)
                self.metric_history_list.append(trainitem.batch_metric_history)
            self.counter+=1
            loss_metric_curve(self.loss_history_list, self.metric_history_list,
                              sample_collected=self.training_items.value_list[0].sample_collect_history,
                              legend=training_context['training_names'].value_list, calculate_base='batch', max_iteration=None,
                              save_path=os.path.join(self.save_path, self.name_prefix),
                              imshow=self.imshow)

            # if self.tile_image_unit == 'epoch' and (epoch + 1) % self.tile_image_frequency == 0:
            #     epoch_loss_history = [trainitem.epoch_loss_history for k, trainitem in self.training_items.items()]
            #     epoch_metric_history = [trainitem.epoch_metric_history for k, trainitem in self.training_items.items()]
            #
            #     loss_metric_curve(epoch_loss_history, epoch_metric_history, legend=self.training_names.value_list,
            #                       calculate_base='epoch', max_iteration=self.num_epochs,
            #                       save_path=os.path.join(self.tile_image_save_path, 'loss_metric_curve.png'),
            #                       imshow=True)


class PrintGradientsCallback(VisualizationCallbackBase):
    def __init__(self,batch_inteval=-1):
        super(PrintGradientsCallback,self).__init__(epoch_inteval=-1,batch_inteval=batch_inteval)
        self.is_in_ipython=is_in_ipython()
        self.is_in_colab=is_in_colab()
        self.batch_inteval=batch_inteval
        self.first_layer=''
        self.last_layer=''
        self.lines=[]

    def on_optimization_step_start(self, training_context):
        if self.batch_inteval > 0 and (training_context['current_epoch'] * training_context['total_batch'] + training_context['current_batch']) % self.batch_inteval == 0:
            grad_dict = {}
            if self.first_layer != '' and self.last_layer != '':
                for i, (k, v) in enumerate(training_context['current_model'].named_parameters()):
                    if k == self.first_layer:
                        training_context['grads_state']['first_layer'].append(
                            np.abs(to_numpy(0 if v.grad is None else v.grad)).mean())
                    elif k == self.last_layer:
                        training_context['grads_state']['last_layer'].append(
                            np.abs(to_numpy(0 if v.grad is None else v.grad)).mean())
            else:
                for i, (k, v) in enumerate(training_context['current_model'].named_parameters()):
                    grad_dict[k] = np.abs(to_numpy(0 if v.grad is None else v.grad))
                    if grad_dict[k].ndim > 1:
                        if self.first_layer == '':
                            self.first_layer = k
                        else:
                            self.last_layer = k

                training_context['grads_state']['first_layer'].append(grad_dict[self.first_layer].mean())
                training_context['grads_state']['last_layer'].append(grad_dict[self.last_layer].mean())

            self.lines.append('{0:<16s}  first_layer gradients: {1:<8.3e}| last_layer gradients: {2:<8.3e}'.format(
                training_context['current_model'].name, training_context['grads_state']['first_layer'][-1],
                training_context['grads_state']['last_layer'][-1]))

    def on_overall_batch_end(self, training_context):
       if len(self.lines)>0:
           sys.stdout.writelines(self.lines)
           sys.stdout.write('\n')
           sys.stdout.flush()
           self.lines = []

