import argparse

parser = argparse.ArgumentParser(description='PyTorch ImageNet Training')
parser.add_argument('--arch', metavar='DIR', default='resnet34',help='使用的模型')
parser.add_argument('--data', metavar='DIR',
                    help='数据的路径')
parser.add_argument('--j', '--workers', default=4, type=int, metavar='N',
                    help='数据导入的线程 (默认为: 4)')
parser.add_argument('--epochs', default=90, type=int, metavar='N',
                    help='训练的次数')
parser.add_argument('--start-epoch', default=0, type=int, metavar='N',
                    help='开始的次数 (useful on restarts)')
parser.add_argument('--train-batch', default=16, type=int,
                    metavar='N',
                    help='训练批处理大小（默认为16）')
parser.add_argument('--val-batch', default=16, type=int,
                    metavar='N',
                    help='测试批处理大小（默认为16）')
parser.add_argument('--lr', '--learning-rate', default=[5e-4, 1e-4, 1e-5, 1e-6], type=float,
                    metavar='LR', help='初始化的学习率', dest='lr')
parser.add_argument('--lr-fc', default=5, type=float,
                    metavar='LR', help='线性层的学习率', dest='lr_fc')
parser.add_argument('--setlr', '--learning-change', default=[0, 5, 9], type=int,
                     help='初始化的学习率', dest='setlr')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
                    help='动量')
parser.add_argument('--wd', '--weight-decay', default=1e-4, type=float,
                    metavar='W', help='权重下降 (默认: 1e-4)',
                    dest='weight_decay')
parser.add_argument('--p', '--print-freq', default=10, type=int,
                    metavar='N', help='打印频率 (默认: 10)')
parser.add_argument('--resume', default=None, type=str, metavar='PATH',
                    help='恢复的模型 (默认: 空)')
parser.add_argument('--optimizer', default='sgd',
                         choices=['sgd', 'rmsprop', 'adam', 'AdaBound', 'radam'], metavar='N',
                         help='优化器 (默认=sgd)')
parser.add_argument('--no_nesterov', dest='nesterov',
                         action='store_false',
                         help='不要使用内斯特罗夫动量')                         
parser.add_argument('--e', '--evaluate', dest='evaluate', action='store_true',
                    help='evaluate model on validation set')
parser.add_argument('--pretrained', dest='pretrained', action='store_true',default=True,
                    help='使用训练模型')
parser.add_argument('--world-size', default=-1, type=int,
                    help='分布式训练的节点数')
parser.add_argument('--rank', default=-1, type=int,
                    help='分布式训练的节点等级')
parser.add_argument('--dist-url', default='tcp://224.66.41.62:23456', type=str,
                    help='用于设置分布式培训的url')
parser.add_argument('--dist-backend', default='nccl', type=str,
                    help='分布式后端')
parser.add_argument('--seed', default=None, type=int,
                    help='初始化培训的种子. ')
parser.add_argument('--gpu', default=0, type=int,
                    help='GPU使用的ID.')
parser.add_argument('--multiprocessing-distributed', action='store_true',
                    help='使用多处理分布式培训来启动每个节点有N个进程，'
                         '其中有N个GPU。这是对单个节点或PyTorch使用'
                         'PyTorch的最快方法多节点数据并行训练')

parser.add_argument('--num_classes', type=int, default=10, help='您的任务应该分类的类数')
parser.add_argument('--photo_size', type=int, default=224, help='图像大小')
parser.add_argument('--local_data_root', default='/cache/', type=str,
                    help='a directory used for transfer data between local path and OBS path')
parser.add_argument('--data_url', type=str, help='the training and validation data path')
parser.add_argument('--test_data_url', default='', type=str, help='the test data path')
parser.add_argument('--data_local', default='work/aifood/images', type=str, help='本地的训练和验证数据路径')
parser.add_argument('--test_data_local', default='', type=str, help='the test data path on local')
parser.add_argument('--train_url', type=str, help='the path to save training outputs')
parser.add_argument('--train_local', default='', type=str, help='the training output results on local')
parser.add_argument('--tmp', default='', type=str, help='a temporary path on local')
parser.add_argument('--deploy_script_path', default='', type=str,
                    help='a path which contain config.json and customize_service.py, '
                         'if it is set, these two scripts will be copied to {train_url}/model directory')

args = parser.parse_args(args=[]) # 实际使用要删除
