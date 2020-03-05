#!/usr/bin/env python3
import sys
import os
import argparse
import shlex
import pandas as pd
import importlib

from flatspin.cmdline import StoreKeyValue, eval_params
from flatspin.data import Dataset, table_formats, is_archive_format
from flatspin.runner import run, run_local, run_dist
from flatspin.encoder import encoders
from flatspin.utils import get_default_params

def import_model(name):
    if '.' in name:
        # Full module path
        module, cls = name.rsplit('.', maxsplit=1)
    else:
        module = 'flatspin.model'
        cls = name

    module = importlib.import_module(module)
    return getattr(module, cls)

def main_worker(args):
    # Run!
    dataset = Dataset.read(args.basepath)

    worker_id = args.worker_id
    num_jobs = len(dataset)
    num_workers = args.num_workers

    # Calculate which jobs in the dataset to run
    # See https://stackoverflow.com/questions/27553218/algorithm-for-distributing-workload-in-a-thread-pool
    from_idx = (worker_id * num_jobs) // num_workers
    to_idx = ((worker_id + 1) * num_jobs) // num_workers

    dataset = dataset[from_idx:to_idx-1]
    run_local(dataset)

def main_list_params(args):
    model_class = import_model(args.model)
    model_name = model_class.__name__
    encoder_name = args.encoder
    encoder = encoders[encoder_name]

    print(f"Default model parameters [{model_name}]:")
    for k,v in get_default_params(model_class).items():
        print(f" {k}={v}")

    print("")

    print(f"Default run parameters:")
    for k,v in get_default_params(run).items():
        print(f" {k}={v}")

    print("")

    print(f"Default encoder parameters [{encoder_name}]:")
    for k,v in get_default_params(encoder).items():
        print(f" {k}={v}")

def main_normal(args):
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

    basepath = args.basepath
    if os.path.exists(basepath):
        # Refuse to overwrite an existing dataset
        raise FileExistsError(basepath)
    os.makedirs(basepath)

    if is_archive_format(args.format):
        outdir = f"{model_name}.{args.format}"
    else:
        outdir = f"{model_name}.out"
    outpath = os.path.join(basepath, outdir)

    # Save dataset
    index = pd.DataFrame({'outdir': [outdir]})
    dataset = Dataset(index, params, info, basepath)
    dataset.save()

    # Run!
    if args.run == 'local':
        run_local(dataset)

    elif args.run == 'dist':
        run_dist(dataset)

def main():
    parser = argparse.ArgumentParser(description='Run flatspin simulation')
    parser.add_argument('-r', '--run', choices=['local', 'dist', 'none', 'worker'], default='local',
            help='run locally or distributed on a cluster')
    parser.add_argument('-p', '--param', action=StoreKeyValue, default={},
            help='set model/run parameter key=value')
    parser.add_argument('-m', '--model', default='SquareSpinIceClosed',
            help='name of model (default: %(default)s) ')
    parser.add_argument('-e', '--encoder', choices=encoders.keys(), default='sin',
            help='input encoder (type of external field, default: %(default)s)')
    parser.add_argument('-o', '--basepath',
            help='output directory for results')
    parser.add_argument('-f', '--format', choices=table_formats.keys(), default='npz',
            help='format of output files (default: %(default)s)')

    parser.add_argument('--list-params', action='store_true')
    parser.add_argument('--worker-id', help='worker id', type=int)
    parser.add_argument('--num-workers', help='number of workers in total', type=int)

    args = parser.parse_args()

    if args.list_params:
        return main_list_params(args)

    if args.run == 'worker':
        if args.worker_id is None or args.num_workers is None or args.basepath is None:
            parser.error('The following arguments are required for worker mode: --worker-id, --num-workers, --basepath')
    else:
        if args.basepath is None:
            parser.error('The following arguments are required: -o/--basepath')

    if args.run == 'worker':
        # Taking part in distributed run
        return main_worker(args)
    elif args.list_params:
        return main_list_params(args)

    return main_normal(args)

if __name__ == '__main__':
    main()
