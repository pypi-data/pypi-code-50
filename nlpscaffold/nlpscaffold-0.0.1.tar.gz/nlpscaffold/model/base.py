import os
import tqdm
import json
import math
import torch
import pprint
from torch import nn, optim
from ..utils.writer import Writer
from ..utils.tracker import Tracker
from ..utils.prep import get_parser


class Model(nn.Module):

    def __init__(self, args, ext=None):
        super().__init__()
        self.args = args
        self.ext = ext
        self.state = {}

    @property
    def device(self):
        return torch.device('cuda') if torch.cuda.is_available() and torch.cuda.device_count() else torch.device('cpu')

    @property
    def dout(self):
        return os.path.join(self.args.dexp, self.args.model, self.args.name)

    def to_default_device(self):
        return self.to(self.device)

    def save_config(self):
        with open(os.path.join(self.dout, 'config.json'), 'wt') as f:
            json.dump(vars(self.args), f, indent=2)

    def compute_loss(self, out, feat, batch):
        raise NotImplementedError()

    def get_optimizer_and_scheduler(self, train):
        opt = optim.Adam(self.parameters(), lr=self.args.lr)
        max_step = math.ceil(len(train) / self.args.batch) * self.args.epoch
        sch = optim.lr_scheduler.LambdaLR(opt, lr_lambda=lambda step: (max_step - step) / max_step)
        return opt, sch

    def extract_preds(self, out, feat, batch):
        raise NotImplementedError()

    def compute_metrics(self, data, preds):
        raise NotImplementedError()

    def get_debug(self, ex, pred):
        return dict(pred=pred)

    def get_file(self, *args):
        return os.path.join(self.dout, *args)

    def write_preds(self, dev, dev_preds, fout):
        debug = [self.get_debug(ex, dev_preds[ex['id']]) for ex in dev]
        with open(fout, 'wt') as f:
            json.dump(debug, f, indent=2)

    def better(self, metrics, best):
        raise NotImplementedError()

    def featurize(self, batch):
        raise NotImplementedError()

    def forward(self, **kwargs):
        raise NotImplementedError()

    def run_train(self, train, dev, args=None, verbose=True):
        args = args or self.args
        if not os.path.isdir(self.dout):
            os.makedirs(self.dout)

        Writer(self.get_file('config.json')).write_dict(vars(self.args))

        loop_writer = Writer(self.get_file('train.log'))
        metric_writer = Writer(self.get_file('train.metrics.jsonl'))
        early_stop_metric_writer = Writer(self.get_file('train.best.json'))
        fsave = self.get_file('best.tar')
        tracker = Tracker()

        optimizer, scheduler = self.get_optimizer_and_scheduler(train)
        iteration = start_epoch = 0
        eval_step = args.eval_step if args.eval_step != -1 else math.ceil(len(train) / args.batch)

        total_train_steps = math.ceil(len(train) / args.batch) * args.epoch
        train_bar = tqdm.tqdm(total=total_train_steps, desc='train steps')

        loop_writer.write('Running:\n{}'.format(vars(args)), newline=True, stdout=True, close_on_finish=False)

        if args.resume:
            metrics = self.load_save(fname=args.resume, optimizer=optimizer, scheduler=scheduler)
            start_epoch = metrics['epoch']
            iteration = metrics['iteration']
            loop_writer.write('Resuming from {}\n{}'.format(args.resume, pprint.pformat(metrics)), newline=True, stdout=True, close_on_finish=False)

        best = {}
        orig_train = train[:]

        for epoch in range(start_epoch, args.epoch):
            loop_writer.write('Starting train epoch {}'.format(epoch), newline=True, stdout=True, close_on_finish=False)

            for batch in train.batch(args.batch, shuffle=True, verbose=False):
                self.train()
                self.state.update({'iteration': iteration, 'epoch': epoch})
                feat = self.featurize(batch)
                out = self.forward(**feat)
                loss_ = self.compute_loss(out, feat, batch)
                loss_backprop = sum(loss_.values()) if isinstance(loss_, dict) else loss_
                tracker.add(examples=batch, preds=self.extract_preds(out, feat, batch), metrics={'loss_{}'.format(k): v.item() for k, v in loss_.items()} if isinstance(loss_, dict) else dict(loss=loss_.item()))

                iteration += 1
                loss_backprop.backward()
                torch.nn.utils.clip_grad_norm_(self.parameters(), self.args.max_grad_norm)
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad()
                train_bar.update(1)

                if iteration % eval_step == 0:
                    metrics = {'epoch': epoch, 'iteration': iteration}
                    metrics.update(tracker.average_metrics())
                    metrics.update({'train_{}'.format(k): v for k, v in self.compute_metrics(tracker.examples, tracker.preds).items()})
                    dev_preds = self.run_pred(dev, args, verbose=verbose)
                    metrics.update({'dev_{}'.format(k): v for k, v in self.compute_metrics(dev, dev_preds).items()})
                    metric_writer.write_dict(metrics, newline=True, indent=0)
                    loop_writer.write(pprint.pformat(metrics), newline=True, stdout=True, close_on_finish=False)

                    if self.better(metrics, best):
                        best.update(metrics)
                        loop_writer.write('Found new best! Saving checkpoint to {}!'.format(fsave), newline=True, stdout=True, close_on_finish=False)
                        self.save(metrics, optimizer, scheduler, fsave)
                        self.write_preds(dev, dev_preds, self.get_file('dev.preds.json'))
                        early_stop_metric_writer.write_dict(metrics)

                    tracker.clear()

        loop_writer.write('Loading best checkpoint from {}'.format(fsave), newline=True, stdout=True, close_on_finish=False)
        metrics = self.load_save(fname=fsave)
        loop_writer.write(pprint.pformat(metrics), newline=True, stdout=True, close_on_finish=True)
        loop_writer.close()

    def save(self, metrics, optimizer, scheduler, fname='best.pt'):
        torch.save({
            'model': self.state_dict(),
            'optimizer': optimizer.state_dict(),
            'scheduler': scheduler.state_dict(),
            'metrics': metrics,
        }, fname)

    def load_save(self, optimizer=None, scheduler=None, fname='best.pt'):
        save = torch.load(fname, map_location='cpu')
        self.load_state_dict(save['model'])
        if optimizer is not None:
            optimizer.load_state_dict(save['optimizer'])
        if scheduler is not None:
            scheduler.load_state_dict(save['scheduler'])
        return save['metrics']

    def run_pred(self, dev, args=None, verbose=True):
        args = args or self.args
        self.eval()
        preds = None
        with torch.no_grad():
            for batch in dev.batch(args.batch, shuffle=False, verbose=verbose):
                feat = self.featurize(batch)
                out = self.forward(**feat)
                preds = dev.accumulate_preds(preds, self.extract_preds(out, feat, batch))
        return preds

    @classmethod
    def get_default_parser(cls, lr, batch, epoch, model='mymodel', max_grad_norm=20, eval_step=-1, seed=0):
        parser = get_parser()
        parser.add_argument('--model', default=model, help='model to use')
        parser.add_argument('--lr', default=lr, help='learning rate', type=float)
        parser.add_argument('--max_grad_norm', default=max_grad_norm, help='grad norm clipping', type=float)
        parser.add_argument('--eval_step', default=eval_step, help='how many steps to run before evaluation. -1 means eval after an epoch', type=int)
        parser.add_argument('--batch', default=batch, help='batch size', type=int)
        parser.add_argument('--epoch', default=epoch, help='epoch', type=int)
        parser.add_argument('--name', '-n', help='name for the experiment', default='default')
        parser.add_argument('--dexp', help='where to store the experiment', default='exp')
        parser.add_argument('--resume', help='checkpoint to resume from')
        parser.add_argument('--seed', help='random seed', default=seed, type=int)
        return parser
