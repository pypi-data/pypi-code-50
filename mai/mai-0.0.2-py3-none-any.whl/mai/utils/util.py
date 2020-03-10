'''
训练与验证时的各种工具
'''
from tensorboardX import SummaryWriter
import torch
import os
import torch.nn as nn
from flyai.utils import remote_helper
import sys
import re
import shutil
if sys.version_info[0] == 2:
    from urlparse import urlparse
    from urllib2 import urlopen  # noqa f811
else:
    from urllib.request import urlopen
    from urllib.parse import urlparse  # noqa: F401

class AverageMeter(object):
    """计算并存储平均值和当前值
       Imported from https://github.com/pytorch/examples/blob/master/imagenet/main.py#L247-L262
    """
    def __init__(self):
        self.val = float(0)
        self.avg = float(0)
        self.sum = float(0)
        self.count = int(0)

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val*n
        self.count += n
        self.avg = self.sum / self.count
        
# 计算top值
def get_accuracy(output, target, topk=(1,)):
        """Computes the accuracy over the k top predictions for the specified values of k"""
        with torch.no_grad():
            maxk = max(topk)
            batch_size = target.size(0)

            _, pred = output.topk(maxk, 1, True, True)
            pred = pred.t()
            correct = pred.eq(target.view(1, -1).expand_as(pred))

            res = []
            for k in topk:
                    correct_k = correct[:k].view(-1).float().sum(0, keepdim=True)
                    res.append(correct_k.mul_(100.0 / batch_size))
            return res
        
# 保存模型
def save_checkpoint(state, is_best, model_name='model', path='checkpoints'):
    os.makedirs(path, exist_ok=True)
    torch.save(state, os.path.join(path, str(state['epoch'])+'_'+model_name+'_'+str(round(state['acc1'],2))+str(round(state['loss'],2))+'.pth'))
    if is_best:
        torch.save(state, os.path.join(path, 'model_best.pth'))
        
# 手动更改学习率
def adjust_learning_rate(optimizer, epoch, lr, setlr):
    """Sets """
    if epoch in setlr:
        for param_group in optimizer.param_groups:
            lr_data = lr[setlr.index(epoch) + 1]
            print("epoch ", epoch,"set lr is ", lr_data)
            param_group['lr'] = lr[setlr.index(epoch) + 1]
            
# 使用ReduceLROnPlateau学习调度器，如果三个epoch准确率没有提升，则减少学习率
def set_scheduler(optimizer):
    exp_lr_scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer,mode='max',patience=3,verbose=True)
    return exp_lr_scheduler

# 日志输出
class logger(object):
    '''
    进行日志的输出
    '''
    def __init__(self, logdir="logs"):
        self.writer = SummaryWriter(log_dir=logdir)
        
    def add_model(self, model, input_data):
        self.writer.add_graph(model, (input_data,))
        
    def add_data(self, name, data, epoch):
        self.writer.add_scalar(name, data, epoch)
        
    def add_train_data(self, data, epoch):
        self.add_data('loss/loss', data[0], epoch)
        self.add_data('acc/acc1', data[1], epoch)
        self.add_data('acc/acc5', data[2], epoch)
        
    def add_train_in_data(self, loss, epoch):
        self.add_data('loss/stop_loss', loss, epoch)
        
    def close(self):
        self.writer.close()
        
class TTAModule(nn.Module):
    def __init__(self, model: nn.Module):
        super().__init__()
        self.model = model

    def tta_out(self, out):
        _, preds = torch.max(out.data, 1)
        li = preds.tolist()
        smax = sid = -1
        for i in li:
            if li.count(i) > smax:
                smax = li.count(i)
                sid = i
        rid = li.index(sid)
        return out[rid].unsqueeze(0)
    
    def forward(self, x):
        x = x.squeeze(0)
        result = self.model(x)
        result = self.tta_out(result)

        return result

def down_model(url):
    path = remote_helper.get_remote_date(url)
    return path

ENV_TORCH_HOME = 'TORCH_HOME'
DEFAULT_CACHE_DIR = '~/.cache'
ENV_XDG_CACHE_HOME = 'XDG_CACHE_HOME'
# matches bfd8deac from resnet18-bfd8deac.pth
HASH_REGEX = re.compile(r'-([a-f0-9]*)\.')

def _get_torch_home():
    torch_home = os.path.expanduser(
        os.getenv(ENV_TORCH_HOME,
                  os.path.join(os.getenv(ENV_XDG_CACHE_HOME, DEFAULT_CACHE_DIR), 'torch')))
    return torch_home

def load_model(url, model_dir=None, map_location=None, progress=True, check_hash=False):
    if model_dir is None:
        torch_home = _get_torch_home()
        model_dir = os.path.join(torch_home, 'checkpoints')
    os.makedirs(model_dir, exist_ok=True)
    parts = urlparse(url)
    filename = os.path.basename(parts.path)
    cached_file = os.path.join(model_dir, filename)
    if not os.path.exists(cached_file):
        sys.stderr.write('Downloading: "{}" to {}\n'.format(url, cached_file))
        hash_prefix = HASH_REGEX.search(filename).group(1) if check_hash else None
        path = remote_helper.get_remote_date('https://www.flyai.com/m/resnet34-333f7ec4.pth')
        shutil.move(path, cached_file)
    return torch.load(cached_file, map_location=map_location)
