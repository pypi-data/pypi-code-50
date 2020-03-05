#!/usr/bin/env python3
import sys
import os
import argparse
import shlex
import pandas as pd
from collections import OrderedDict
from copy import copy

from flatspin.cmdline import StoreKeyValue, eval_params
from flatspin.sweep import sweep
from flatspin.data import Dataset, table_formats, is_archive_format
from flatspin.runner import run, run_local, run_dist
from flatspin.encoder import encoders
from flatspin.utils import get_default_params
from .run import import_model, main_list_params

def main():
    parser = argparse.ArgumentParser(description='Run flatspin sweep')
    parser.add_argument('-r', '--run', choices=['local', 'dist', 'none'], default='local',
                        help='run locally or distributed on a cluster')
    parser.add_argument('-p', '--param', action=StoreKeyValue, default={},
                        help='set model parameter key=value')
    parser.add_argument('-s', '--sweep', action=StoreKeyValue, metavar='key=SPEC',
                        help='set sweep parameter key=SPEC')
    parser.add_argument('-n', '--repeat', type=int, default=1, metavar='N',
                        help='repeat each experiment N times (default: %(default)s)')
    parser.add_argument('-ns', '--repeat-spec', action=StoreKeyValue, metavar='key=SPEC',
                        help='repeat each according to key=SPEC')
    parser.add_argument('--seed', type=int, default=0, help='random seed')
    parser.add_argument('-m', '--model', default='SquareSpinIceClosed',
            help='name of model (default: %(default)s) ')
    parser.add_argument('-e', '--encoder', choices=encoders.keys(), default='sin',
            help='input encoder (type of external field, default: %(default)s)')
    parser.add_argument('-o', '--basepath', help='output directory for results')
    parser.add_argument('-f', '--format', choices=table_formats.keys(), default='npz',
            help='format of output files (default: %(default)s)')
    parser.add_argument('--list-params', action='store_true')

    args = parser.parse_args()

    if args.list_params:
        return main_list_params(args)

    if args.basepath is None or args.sweep is None:
        parser.error('The following arguments are required: -o/--basepath, -s/--sweep')

    model_class = import_model(args.model)
    model_name = model_class.__name__
    encoder_name = args.encoder
    encoder = encoders[encoder_name]

    # -e sin is really just an alias for -p encoder=sin
    params = get_default_params(run)
    params['encoder'] = encoder_name
    params.update(get_default_params(model_class))
    params.update(get_default_params(encoder))
    params.update(eval_params(args.param))

    info = {
        'model': f'{model_class.__module__}.{model_class.__name__}',
        'model_name': model_name,
        'data_format': args.format,
        'command': ' '.join(map(shlex.quote, sys.argv)),
    }

    ext = args.format if is_archive_format(args.format) else "out"
    if args.repeat > 1 or args.repeat_spec:
        outdir_tpl = model_name + ".{:06d}.{:06d}." + ext
    else:
        outdir_tpl = model_name + ".{:06d}." + ext

    basepath = args.basepath
    if os.path.exists(basepath):
        # Refuse to overwrite an existing dataset
        raise FileExistsError(basepath)
    os.makedirs(basepath)

    index = []

    # Generate index
    for i, j, sweep_params in sweep(args.sweep, args.repeat, args.repeat_spec, params, args.seed):

        outdir = outdir_tpl.format(i, j)
        outpath = os.path.join(basepath, outdir)

        row = OrderedDict(sweep_params)
        row.update({'outdir': outdir})
        index.append(row)

    # Save dataset
    index = pd.DataFrame(index)
    dataset = Dataset(index, params, info, basepath)
    dataset.save()

    # Run!
    print("Starting sweep with {} runs".format(len(dataset)))
    if args.run == 'local':
        run_local(dataset)

    elif args.run == 'dist':
        run_dist(dataset)

if __name__ == '__main__':
    main()
