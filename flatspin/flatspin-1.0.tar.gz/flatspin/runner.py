"""
Dipole model runner
"""
import os
import numpy as np
import pandas as pd
import time
from numbers import Number
from datetime import timedelta
import subprocess
from copy import copy
from importlib import import_module
import warnings

from .cmdline import ProgressBar
from .encoder import get_encoder
from .data import read_table, to_table, save_table, is_archive, archive_key
from .utils import pop_params, label_columns, label_columns_2d, eval_dict

#
# List of deprecated parameters
#
# If you rename a parameter, please add it here to raise an error if it's being
# used! Otherwise it will go unnoticed since we ignore unknown parameters to
# facilitate fancy sweeps such as -s 'sz=arange(10,51,10)' -s 'size=[(sz,sz)]'
#
deprecated_params = ('sw_a', 'sw_alpha', 'temp_interp')

class DeprecationError(Exception):
    pass

def run(model, encoder='sin', input=1, input_key=None, periods=100, spp=100,
        temp=0, temp_func='interp', **params):
    """
    Run a flatspin simulation

    Parameters
    ----------
    model : SpinIce
        Model instance
    encoder : string or Encoder
        Name of input encoder to use.
        See flatspin.encoder for a list of available encoders
    input : float, array or string
        Input to be encoded
        float: constant input repeated periods times
        array: array of input to encode
        string: filename of table input data
    input_key : int or str
        Index into input (table column)
    periods : int
        Number of periods of the external field to run
        Only used if input is a float
    spp : int
        Number of samples to save per input value
    temp : float, array
        Temperature to be used
        float: constant temperature for whole run
        array: array of temperatures stretched to fit run
    params : dict
        Params to pass to the encoder
    """
    # unknown params are ignored

    if isinstance(encoder, str):
        encoder = get_encoder(encoder)
    encoder_params = pop_params(encoder, params)
    encoder.set_params(**encoder_params)

    # Bail out if user tries any deprecated params
    for p in params.keys():
        if p in deprecated_params:
            raise DeprecationError("Parameter is deprecated", p)

    # Warn on unknown params
    if params:
        unknown_params = ", ".join(params.keys())
        warnings.warn("Ignoring unknown parameters: " + unknown_params)

    result = {}

    if isinstance(input, str):
        # load input from file
        input = read_table(input)
        result['input'] = input
    elif isinstance(input, Number):
        # constant
        input = input * np.ones(periods)
        result['input'] = pd.DataFrame(input, columns=['input'])
    else:
        # array/list
        input = input
        result['input'] = pd.DataFrame(input, columns=['input'])

    if input_key is not None:
        input = input[input_key]
    input = np.array(input, dtype=float)

    if isinstance(encoder, str):
        encoder = get_encoder(encoder)
    encoder.set_params(**encoder_params)

    # np.random.seed(seed)
    # random.seed(seed)

    t0 = time.time()

    # Encode input as h_ext
    h_ext = encoder(input)

    # Figure out timesteps per period
    ts = len(h_ext) / len(input)
    if ts % spp != 0:
        print(f"WARNING: spp {spp} does not evenly divide the encoded input")
        print(f"         spp should divide the number of timesteps per input {ts}, e.g. spp={ts}")
    sample_every = int(np.round(ts / spp))

    # Input has now been encoded into h_ext, resulting in spp samples per input
    # value. Repeat input values spp times so that h_ext and input DataFrames
    # can be easily joined on the same index when needed. We keep the original
    # input index as an extra column called "index".
    input_df = result['input']
    input_df = input_df.loc[input_df.index.repeat(spp)].reset_index()
    input_df.index.name = 't'
    result['input'] = input_df

    # Thermal input
    temp = np.atleast_1d(temp)
    # exp-decay decays from temp[0] to temp[1] by nth order exponential decay 
    # where n is set by temp[2]
    if temp_func == 'exp-decay':
        exp_params = 3
        if len(temp) != exp_params:
            raise ValueError(f"For temp_func=exp, temp expects {exp_params}\
                parameters: temp=[start, stop, exponent]")
        lspace = np.linspace(0, 1, len(h_ext))
        temp = temp[0]*np.exp(np.log(temp[1]/temp[0])*pow(lspace, temp[2]))
    elif temp_func == 'interp':
        lspace = np.linspace(0, len(temp)-1, len(h_ext))
        temp = np.interp(lspace, np.arange(len(temp)), temp)
    else:
        if len(h_ext) % len(temp) != 0:
            raise ValueError(f"Length of temp {len(temp)} must divide length \
                of encoded input {len(h_ext)}")
        repeats = len(h_ext) / len(temp)
        temp = temp.repeat(repeats)

    save_h_therm = not np.all(temp == 0)

    result['geometry'] = pd.DataFrame({
        'posx': model.pos[:,0].copy(),
        'posy': model.pos[:,1].copy(),
        'angle': model.angle.copy()})

    result['hc'] = pd.DataFrame({'threshold': model.threshold.copy()})

    cols = label_columns(model.labels, prefix='init')
    result['init'] = pd.DataFrame([model.spin.copy()], columns=cols)

    # TODO: dump model?
    # make a copy of model so we store the initial state in the dataset
    #    'model': copy.deepcopy(model),

    steps = 0

    sample_index = []
    result['spin'] = []
    result['mag'] = []
    result['h_ext'] = []
    if save_h_therm:
        result['h_therm'] = []
    result['temp'] = []
    result['energy'] = []
    result['steps'] = []

    msg = type(model).__name__
    progress_bar = ProgressBar(desc=msg, total=len(h_ext))

    for i, (h, temp_std) in enumerate(zip(h_ext, temp)):
        if h.ndim > 1:
            # grid
            model.set_grid('h_ext', h)
        else:
            # global field
            model.set_h_ext(h)

        model.set_temperature(temp_std)

        steps += model.relax()

        progress_bar.update()

        if i % sample_every == 0:
            sample_index.append(i)
            result['spin'].append(model.spin.copy())
            result['mag'].append(model.vectors.flatten())
            result['energy'].append(model.total_energies())
            if save_h_therm:
                result['h_therm'].append(model.h_therm.flatten())
            result['temp'].append(model.thermal_std)
            if h.ndim > 1:
                # local field
                result['h_ext'].append(model.h_ext.flatten())
            else:
                # global field
                result['h_ext'].append(h)

            result['steps'].append(steps)

    progress_bar.close()

    cols = label_columns(model.labels, prefix='spin')
    result['spin'] = pd.DataFrame(result['spin'], columns=cols, index=sample_index, dtype=result['spin'][0].dtype)
    result['spin'].index.name = 't'

    cols = label_columns_2d(model.labels, prefix='mag')
    result['mag'] = pd.DataFrame(result['mag'], columns=cols, index=sample_index, dtype=result['mag'][0].dtype)
    result['mag'].index.name = 't'

    cols = ['h_extx', 'h_exty']
    if h_ext.ndim > 2:
        # local field
        cols = label_columns_2d(model.labels, prefix='h_ext')
    result['h_ext'] = pd.DataFrame(result['h_ext'], columns=cols, index=sample_index, dtype=model.h_ext.dtype)
    result['h_ext'].index.name = 't'

    if save_h_therm:
        cols = label_columns_2d(model.labels, prefix='h_therm')
        result['h_therm'] = pd.DataFrame(result['h_therm'], columns=cols, index=sample_index, dtype=np.float64)
        result['h_therm'].index.name = 't'

    result['temp'] = pd.DataFrame(result['temp'], columns=['temp'], index=sample_index)
    result['temp'].index.name = 't'

    cols = ["E_dip", "E_ext", "E_therm", "E_tot"]
    result['energy'] = pd.DataFrame(result['energy'], columns=cols, index=sample_index, dtype=np.float64)
    result['energy'].index.name = 't'

    result['steps'] = pd.DataFrame(result['steps'], columns=['steps'], index=sample_index, dtype=int)
    result['steps'].index.name = 't'


    runtime = time.time() - t0

    result['stats'] = {
        'runtime': runtime,
        'steps': steps,
    }

    td = timedelta(seconds=runtime)
    print(f'Completed {steps} steps in {td}')

    return result

def run_and_save(model_class, params, outdir, data_format):
    params_table = to_table(params)

    model_params = pop_params(model_class, params)
    model = model_class(**model_params)

    results = run(model, **params)
    results["params"] = params_table

    if not is_archive(outdir):
        os.makedirs(outdir)

    for name, data in results.items():
        df = to_table(data)
        if not is_archive(outdir):
            name = f"{name}.{data_format}"
        save_table(df, os.path.join(outdir, name))

def run_local(dataset):
    """ Run on localhost """
    n_runs = len(dataset)

    mod, cls = dataset.info['model'].rsplit('.', 1)
    module = import_module(mod)
    model_class = getattr(module, cls)
    data_format = dataset.info['data_format']

    for i, ds in enumerate(dataset):
        params = copy(ds.params)
        params.update(eval_dict(ds.row().to_dict()))
        outdir = params.pop('outdir')
        outpath = os.path.join(dataset.basepath, outdir)

        print(f"Run {i+1}/{n_runs}: {outdir}")
        print(params)
        run_and_save(model_class, params, outpath, data_format)

def generate_script(template, outfile, **params):
    with open(template) as fp:
        tpl = fp.read()
    script = tpl.format(**params)
    with open(outfile, 'w') as fp:
        fp.write(script)

job_script_template = os.path.join(os.path.dirname(__file__), 'flatspin.slurm.sh')

def run_dist(dataset, wait=True, max_jobs=1000):
    """ Run distributed on a cluster """

    #
    # Generate job script
    #

    # Construct a sensible name for the job script
    job_script_dir = dataset.basepath
    job_script_name = os.path.basename(job_script_template)
    job_script = os.path.join(job_script_dir, job_script_name)

    # Job template params
    job_params = {
        'job_script_dir': job_script_dir,
        'job_script_name': job_script_name,
        'basepath': dataset.basepath,
    }

    generate_script(job_script_template, job_script, **job_params)

    #
    # Submit jobs
    #

    # array size will never exceed max_jobs
    array_size = min(max_jobs, len(dataset))

    cmd = ['sbatch']
    if wait:
        cmd.append('--wait')
    cmd.append(f'--array=0-{array_size-1}')
    cmd.append(job_script)
    print(cmd)
    p = subprocess.Popen(cmd)

    if wait:
        p.wait()

