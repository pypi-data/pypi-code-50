import sys
sys.path.append('../..')

import numpy as np
import scipy as sp

from bayesbridge.bayesbridge import BayesBridge
from simulate_data import simulate_design, simulate_outcome
# from bayesbridge.mcmc_diagnostics import estimate_ess

model = 'logit'
n_obs, n_pred = 10 ** 3, 10 ** 2

X = simulate_design(
    n_obs, n_pred, 
    corr_dense_design=False,
    binary_frac=.6, 
    binary_pred_freq=.2,
    categorical_frac=.3, 
    n_category=5,
    shuffle_columns=False,
    format_='sparse',
    seed=0
)

n_signal = 10
intercept = 2

beta_true = np.zeros(n_pred + 1)
beta_true[0] = intercept
beta_true[1:(1 + n_signal)] = 1

n_trial = np.ones(X.shape[0]) # Binary outcome.
y = simulate_outcome(X, beta_true[1:], intercept=intercept, model=model, n_trial=n_trial, seed=1)

bridge = BayesBridge(
    y, X, model=model, 
    add_intercept=(model != 'cox'),
    n_coef_without_shrinkage=0,
    center_predictor=True,
    prior_sd_for_unshrunk=1.,
    regularizing_slab_size=1.,
    shrinkage_prior_type='horseshoe'
)

sampling_method = 'direct'
mcmc_output = bridge.gibbs(
    n_burnin=0, n_post_burnin=500, 
    sampling_method=sampling_method, 
    shrinkage_exponent=1.,
    n_init_optim_step=10, 
    init={'apriori_coef_scale': .1}, #{'global_shrinkage': .001}, #  
    seed=2, n_status_update=10,
)
samples = mcmc_output['samples']