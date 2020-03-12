from ..utils import utils
import numpy as np
from pyswarms.single.global_best import GlobalBestPSO
from .csip_access import ServiceClient
import json


def service(x, param, url, step_param_names, step_objfunc, calib_params, files=None):
    cost = np.ones(len(x[:, 0]))
    threads = []
    print('   ', end='', flush=True)

    for i_particle, v in enumerate(x[:, 0]):
        worker = ServiceClient(url, i_particle, cost, x, param,
                               step_param_names, step_objfunc, calib_params, files)
        threads.append(worker)
        worker.start()
        # stagger the calls a bit (250ms)
        # time.sleep(0.25)

    for x in threads:
        x.join()

    print(flush=True)
    return cost


def global_best(steps, rounds, args, n_particles, iters, options, ctol=1.0E-6, ftol=-np.inf):
    utils.check_url(args['url'])

    min_rounds = 1
    if type(rounds) == tuple:
        min_rounds = rounds[0]
        max_rounds = rounds[1]
    else:
        max_rounds = rounds

    if min_rounds < 1:
        raise Exception('min rounds >= 1 expected, was "{}"'.format(min_rounds))

    if max_rounds > 20:
        raise Exception('max rounds <= 20 expected, was "{}"'.format(max_rounds))

    best_cost = np.ones(len(steps))
    optimizer = np.empty(len(steps), dtype=object)

    for r in range(max_rounds):
        no_improvement = np.full(len(steps), True)
        for s, step in enumerate(steps):
            param_names, bounds, objfunc = utils.get_step_info(steps, s)
            # maybe clone args?
            args['step_param_names'] = param_names
            args['step_objfunc'] = objfunc
            # get calibrated parameter from all other steps
            args['calib_params'] = utils.get_calibrated_params(steps, s)

            if optimizer[s] is None:
                optimizer[s] = GlobalBestPSO(n_particles, len(param_names),
                                             options=options, bounds=bounds, ftol=ftol)

            print('\n>>>>> R{}/S{}  particle params: {}  using: {}\n'.format(r + 1, s + 1, param_names,
                                                                             args['calib_params']))

            cost, pos = optimizer[s].optimize(service, iters=iters, **args)

            # capture the best cost
            # if cost < best_cost[s]:
            if np.abs(cost - best_cost[s]) > ctol:
                best_cost[s] = cost
                no_improvement[s] = False
                utils.annotate_step(best_cost[s], pos, steps, s)

            print('\n     Step summary, best particle values: {} '.format(pos))

            # print(json.dumps(steps, sort_keys=False, indent=2))

        # if no improvement in all steps, break out of rounds prematurely
        print('\n  Round summary, bestcost: {}, improvement:{} '.format(best_cost, np.invert(no_improvement)))
        # but start checking only after min_rounds
        if (r + 1 >= min_rounds) and all(no_improvement):
            break

    print('Done after {}/{} rounds'.format(r + 1, max_rounds))
    return optimizer, cost  # return the last output
