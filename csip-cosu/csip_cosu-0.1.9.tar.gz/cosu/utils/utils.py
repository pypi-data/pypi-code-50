import requests
import numpy as np

NORM = {'kge': lambda x: 1 - x,
        'nslog': lambda x: 1 - x,
        'ns': lambda x: 1 - x,
        'rmse': lambda x: x,
        'trmse': lambda x: x,
        }


def get_step_info(steps, index):
    """Extract all relevant info from the step dict"""

    step = steps[index]
    l = len(step['param'])
    param_min = np.ones(l)
    param_max = np.ones(l)
    param_names = []

    # extract names and bounds
    for i, p in enumerate(step['param']):
        param_names.append(p['name'])
        if len(p['bounds']) != 2:
            raise Exception('Invalid bounds tuple: (min, max): "{}"'.format(p['bounds']))
        if not p['bounds'][0] < p['bounds'][1]:
            raise Exception('Invalid bounds values: "{}"'.format(p['bounds']))
        param_min[i] = p['bounds'][0]
        param_max[i] = p['bounds'][1]

    # check if OF is supported
    for o in step['objfunc']:
        if not o['name'] in NORM.keys():
            raise Exception('OF not supported: "{}"'.format(o['name']))
        if len(o['data']) != 2:
            raise Exception('OF missing data: (sim, obs): "{}"'.format(o['name']))

    return param_names, (param_min, param_max), step['objfunc']


def get_calibrated_params(steps, index):
    """Get all previously calibrated parameter from any other step"""

    step = steps[index]
    cp = {}
    for s in steps:
        # skip the own step
        if s is step:
            continue
        for p in s['param']:
            if 'value' in p.keys():
                cp[p['name']] = p['value']
    return cp


def annotate_step(best_cost, pos, steps, index):
    """Annotate the step with the best value"""

    step = steps[index]
    step['cost'] = best_cost
    for i, p in enumerate(step['param']):
        p['value'] = pos[i]


def check_url(url):
    """Check is the Url is valid."""

    r = requests.head(url)
    if r.status_code != 200:
        raise Exception('Error code {} from Url: "{}"'.format(r.status_code, url))
