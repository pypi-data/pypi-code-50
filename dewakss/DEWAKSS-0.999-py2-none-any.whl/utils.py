from anndata import AnnData as _AnnData
import scipy as _sp
from scipy.sparse import issparse as _issparse


def ftt(data, reversed=False, copy=False, correction=-1):
    """
    Freeman-Tukey transform (FTT), y = √(x) + √(x + 1) + correction

    reversed this is x = (y - correction)^2 - 1

    correction is default -1 to preserve sparse data.
    """

    if isinstance(data, _AnnData):
        adata = data.copy() if copy else data

        ftt(adata.X, reversed=reversed, copy=False)
        return adata if copy else None

    X = data.copy() if copy else data

    if _issparse(X):
        X.data = _sp.sqrt(X.data) + _sp.sqrt(X.data + 1) + correction

    else:
        X = _sp.sqrt(X) + _sp.sqrt(X + 1) + correction

    if reversed:
        raise NotImplementedError
        # X[nnz] = _sp.square(X[nnz] - correction) - 1

    return X if copy else None


def hyper_parameter_search(adata, neighbors=_sp.logspace(5, 200, 20), npcs=_sp.logspace(5, 200, 20), modes=['connectivities', 'distances'], decay=[1], symmetrize=[False], denoisetypes=['mean'], copy=True, set_diags=[0], verbose=True, run2best=False, figdir=None):

    adata = adata.copy() if copy else adata

    sc.pp.pca(adata, n_comps=max(npcss), random_state=0)

    hyperp = []

    for denoiset in denoisetypes:
        for N in neigbours:
            for pcs in npcss:
                for d in decay:
                    for m in modes:
                        for s in symmetrize:
                            for I in set_diags:
                                if verbose:
                                    print(d, m, s, I, N, pcs, denoiset)
                                tmpadata = adata.copy()

                                sc.pp.neighbors(tmpadata, n_neighbors=N, n_pcs=pcs)

                                dewaxer = dewakss.DEWAKSS(tmpadata, iterations=20, init_diag=I, set_diag=(I if I==0 else None), run2best=run2best, denoise_type=denoiset, decay=d, mode=m, symmetrize=symmetrize, verbose=False)

                                dewaxer.fit(tmpadata)

                                performance = pd.DataFrame(dewaxer.prediction_).T
                                performance.index.name = "iteration"
                                performance.columns = ['MSE', "R2"]
                                performance = performance.reset_index()
                                performance['decay'] = d
                                performance['mode'] = m
                                performance["symmetrize"] = s
                                performance["diag"] = I
                                performance['neighbors'] = N
                                performance['pcs'] = pcs
                                performance['denoisetype'] = denoiset
                                hyperp.append(performance)

    performance_data = pd.concat(hyperp)
    performance_data = performance_data.reset_index(drop=True)

    return performance_data


def plot_hyper_parameter_search(pdata, dosave=True, fold=1, fig=None, metric='MSE', figsplit=['neighbors', 'decay'], order='C'):

    for (mode, dt), df in pdata.groupby(combo):

        combos = df[figsplit].drop_duplicates()

        if fig is None:
            fig = plt.figure(figsize=(16, 6), constrained_layout=True)

        ax = fig.subplots(fold, combos.shape[0] // fold + combos.shape[0] % fold, sharex=True, sharey='row').flatten(order=order)

        nonused = ax[combos.shape[0]:]
        ax = ax[:combos.shape[0]]

        combos['axes'] = ax
        combos = combos.set_index(figsplit)

        labels = []
        for (neighbors, pcs, decay), subdf in df.groupby(['neighbors', 'pcs', 'decay']):
            axes = combos.loc[neighbors, decay][0]
            subdf = subdf[~(subdf['iteration'] == 0)]
            lab = axes.plot(subdf['iteration'].values, subdf[metric].values, label=pcs, zorder=-pcs + 1000, linewidth=2)

            if ax[0] == axes:
                labels.append(lab[0])

            axes.legend().set_visible(False)
            axes.set_xlabel('iteration')
            axes.set_ylabel(f"{metric}")

            axes.set_xticks(subdf['iteration'].values)
            axes.set_title(f"k={neighbors}")
            axes.grid(linewidth=0.5, linestyle='--')
            axes.label_outer()

        if nonused:
            nonused[0].legend(labels, [l._label for l in labels], title='PCs', ncol=3, loc='upper center')
        else:
            ax[0].legend(labels, [l._label for l in labels], title='PCs', ncol=3, loc='middle right')

        if metric == 'MSE':
            optind = df.groupby(figsplit)[metric].min()
        elif metric == 'R2':
            optind = df.groupby(figsplit)[metric].max()

        optit = df.set_index(figsplit)
        for (neighbors, decay), value in combos.iterrows():
            axes = value[0]
            minmse = optind.loc[neighbors, decay]
            opts = (optit.loc[neighbors, decay][metric] == minmse).values
            its = optit.loc[neighbors, decay][opts][figsplit[0]][0]
            optpcs = optit.loc[neighbors, decay][opts]['pcs'][0]
            sns.despine()
            ylims = np.array(axes.get_ylim())
            axes.vlines([its, its], *(ylims), zorder=500, linestyle=':')
            hl = 'left' if its < 10 else 'right'
            xl = its+1 if its < 10 else its-1

            axes.text(xl, ylims[1], f"MSE={minmse:.4f}\nPCs={optpcs}", ha=hl, va='top')
            axes.set_ylim(*ylims)

        if metric == 'MSE':
            opte = optit[optit[metric] == optind.min()]
        elif metric == 'R2':
            opte = optit[optit[metric] == optind.max()]

        for x in nonused:
            #     x.axis('off')

            shax = x.get_shared_x_axes()
            # shay = x.get_shared_y_axes()
            shax.remove(x)
            # shay.remove(x)
            # x.clear()
            x.set_frame_on('off')
            x.spines['top'].set_visible(False)
            x.spines['right'].set_visible(False)
            # x.spines['left'].set_visible(False)
            # x.spines['bottom'].set_visible(False)
            # x.set_xticks([])
            # x.set_yticks([])

        fig.suptitle(f"Denoise type={dt}, {mode}\nOptimal: MSE={opte['MSE'][0]:.4f}, it={opte['iteration'][0]}, PCs={opte['pcs'][0]}, k={opte.reset_index()['neighbors'][0]}")

        if figdir is not None:
            fdir = figdir
            fname = f"denoise_type_{dt}_{mode}_{metric}_hyper_paramters_"
            fnames = scpl.save_figure(fig, fdir, fname=fname, dpi=300)
            print_file = "[[file:" + fnames[0] + "]]"
            print(print_file, sep=",", end="")
            print("")
