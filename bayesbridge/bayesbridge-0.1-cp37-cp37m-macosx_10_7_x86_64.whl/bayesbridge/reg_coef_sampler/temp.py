def pcg_gaussian_sampler(self, X_row_major, X_col_major, omega, D, z,
                         beta_init_1=None, beta_init_2=None,
                         precond_by='diag', precond_blocksize=0,
                         beta_scaled_sd=None, maxiter=None, atol=10e-6,
                         seed=None, iter_list=None, return_cond_num=False):
    """
    Generate a multi-variate Gaussian with the mean mu and covariance Sigma of the form
       Sigma^{-1} = X' Omega X + D^2, mu = Sigma z
    where D is assumed to be diagonal. For numerical stability, the code first sample
    from the scaled parameter beta / precond_scale.

    Param:
    ------
    D : vector
    atol : float
        The absolute tolerance on the residual norm at the termination
        of CG iterations.
    beta_scaled_sd : vector of length X.shape[1]
        Used to estimate a good preconditioning scale for the coefficient
        without shrinkage. Used only if precond_by in ('prior', 'prior+block').
    """

    X, X_T = choose_optimal_format_for_matvec(X_row_major, X_col_major)

    if seed is not None:
        np.random.seed(seed)

    # Define a preconditioned linear operator.
    start_time = time.time()
    Phi_precond_op, precond_scale, block_precond_op, Phi_blockprecond_op = \
        self.precondition_linear_system(
            D, omega, X_row_major, X_col_major, precond_by,
            precond_blocksize, beta_scaled_sd
        )
    precond_time = time.time() - start_time

    # Draw a target vector.
    v = X_T.dot(omega ** (1 / 2) * np.random.randn(X.shape[0])) \
        + D * np.random.randn(X.shape[1])
    b = precond_scale * (z + v)

    # Pick the initial vector for CG iteration
    beta_scaled_init = self.choose_best_linear_comb(
        beta_init_1, beta_init_2, Phi_precond_op, precond_scale, b
    )

    # TODO: remove after experimentation.
    beta_scaled_init[self.n_coef_wo_shrinkage:] = 0

    # Create a dictionary and a callback function to get intermediate PCG outputs.
    cg_info = {
        'n_iter': 0,
        'pcg_estimate': [],
        'pcg_resid': [],
        'pcg_init': beta_scaled_init,
        'pcg_target': b,
        'precond_scale': precond_scale,
    }
    if (iter_list is not None) and (0 in iter_list):
        cg_info['pcg_estimate'].append(beta_scaled_init.copy())
        cg_info['pcg_resid'].append(
            Phi_precond_op.matvec(beta_scaled_init) - b)
    pcg_iter_timer = SmartTimer()

    def cg_callback(x_curr):
        pcg_iter_timer.off()
        cg_info['n_iter'] += 1
        if (iter_list is not None) and (cg_info['n_iter'] in iter_list):
            cg_info['pcg_estimate'].append(x_curr.copy())
            resid = Phi_precond_op.matvec(x_curr) - b
            cg_info['pcg_resid'].append(resid)
        pcg_iter_timer.on()

    if iter_list is not None:
        maxiter = np.max(iter_list)

    # Run PCG.
    rtol = atol / np.linalg.norm(b)
    pcg_iter_timer.on()
    beta_scaled, info = sp.sparse.linalg.cg(
        Phi_precond_op, b, x0=beta_scaled_init, maxiter=maxiter, tol=rtol,
        M=block_precond_op, callback=cg_callback
    )
    pcg_iter_timer.off()
    cg_info['per_iter_time'] = pcg_iter_timer.averaged_time
    cg_info['precond_time'] = precond_time

    if info != 0:
        self.warn_message_only(
            "The conjugate gradient algorithm did not achieve the requested " +
            "tolerance level. You may increase the maxiter or use the dense " +
            "linear algebra instead."
        )

    # Append the condition number info
    if return_cond_num:
        if 'block' in precond_by.split('+') and precond_blocksize > 0:
            cg_info['cond_num_info'] = \
                compute_condition_num(Phi_blockprecond_op)
        else:
            cg_info['cond_num_info'] = \
                compute_condition_num(Phi_precond_op)

    beta = precond_scale * beta_scaled
    return beta, cg_info
