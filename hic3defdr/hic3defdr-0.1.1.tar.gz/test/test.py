import numpy as np

from hic3defdr import HiC3DeFDR, plot_fdr, plot_roc, compare_disp_fits, \
    plot_fn_vs_fp, plot_distance_bias
from hic3defdr.analysis.alternatives import Global3DeFDR

#repnames = ['ES_1', 'ES_3', 'NPC_2', 'NPC_4']
repnames = ['ES_1', 'ES_3', 'NPC_1', 'NPC_2']
#chroms = ['chr%i' % i for i in range(1, 20)] + ['chrX']
chroms = ['chr18', 'chr19']
#chroms = ['chr1']
base_path = 'd:/lab-data/bonev/'

def main():
    if False:
        import sys
        import scipy.sparse as sparse
        from hiclite.steps.filter import filter_sparse_rows_count
        from hiclite.steps.balance import kr_balance
        infile_pattern = base_path + '<rep>/<chrom>_raw.npz'
        for repname in ['NPC_1']:
            for chrom in chroms:
                sys.stderr.write('balancing rep %s chrom %s\n' % (repname, chrom))
                infile = infile_pattern.replace('<rep>', repname)\
                    .replace('<chrom>', chrom)
                outfile = infile.replace('_raw.npz', '_kr.bias')
                _, bias, _ = kr_balance(
                    filter_sparse_rows_count(sparse.load_npz(infile)), fl=0)
                np.savetxt(outfile, bias)

        import sys; sys.exit()

    h = HiC3DeFDR(
        [base_path + '<rep>/<chrom>_raw.npz'.replace('<rep>', repname)
        for repname in repnames],
        [base_path + '<rep>/<chrom>_kr.bias'.replace('<rep>', repname)
        for repname in repnames],
        chroms, 'design.csv', 'output-small',
        loop_patterns={c: base_path + 'clusters/%s_<chrom>_clusters.json' % c
                       for c in ['ES', 'NPC']},
        dist_thresh_max=200
    )

    #from hic3defdr.util.clusters import load_clusters, cluster_to_slices
    #chrom = 'chr18'
    #clusters = load_clusters(h.loop_patterns['ES'].replace('<chrom>', chrom))
    #slices = cluster_to_slices(clusters[23])
    #_ = h.plot_heatmap('ES_1', chrom, *slices, outfile='zoomin.png')
    #h.plot_grid('chr18', 2218, 2236, 20, outfile='grid.png')

    #h.plot_correlation_matrix(outfile='correlation.png')
    #h.run_to_qvalues(n_threads=-1)
    #h.prepare_data(n_threads=-1)
    #h.estimate_disp(n_threads=-1)
    #h.lrt(n_threads=-1)
    #h.bh()
    #h.classify(n_threads=None)
    #h.simulate('ES', n_threads=None)
    #compare_disp_fits([h.load_disp_fn(cond) for cond in h.design.columns],
    #                  h.design.columns, max_dist=100, legend='outside', outfile='disp_comparison.png')
    #h.plot_dispersion_fit('ES', xaxis='mean', yaxis='var', logx=True, logy=True, outfile='mvr.png')
    #h.plot_dispersion_fit('ES', distance=10, hexbin=True, xaxis='mean', yaxis='var', logx=True, logy=True, outfile='mvr_10.png')
    sim_path = 'sim/'
    sim_repnames = ['A1', 'A2', 'B1', 'B2']
    h_sim = HiC3DeFDR(
        raw_npz_patterns=[sim_path + '<rep>_<chrom>_raw.npz'.replace('<rep>', repname) for repname in sim_repnames],
        bias_patterns=[sim_path + '<rep>_<chrom>_kr.bias'.replace('<rep>', repname) for repname in sim_repnames],
        chroms=chroms,
        design=sim_path + 'design.csv',
        outdir='output-sim',
        loop_patterns={'ES': base_path + 'clusters/ES_<chrom>_clusters.json'}
    )
    #h.plot_heatmap('ES_1', 'chr18', slice(1000, 1100), slice(1000, 1100), outfile='heatmap.png')
    #h_sim.run_to_qvalues()
    #h_sim.evaluate('ES', 'sim/labels_<chrom>.txt')
    dist_bins = [
        ('short', (None, 15)),
        ('mid', (16, 30)),
        ('long', (31, None))
    ]
    #for _, (min_dist, max_dist) in dist_bins:
    #    h_sim.evaluate('ES', 'sim/labels_<chrom>.txt', min_dist=min_dist, max_dist=max_dist, rerun_bh=False)

    #plot_roc([np.load('output-sim/eval_%s_%s.npz' % (min_dist, max_dist))
    #          for _, (min_dist, max_dist) in dist_bins],
    #         [label for label, _ in dist_bins],
    #         outfile='roc.png')
    #plot_fdr([np.load('output-sim/eval_%s_%s.npz' % (min_dist, max_dist))
    #          for _, (min_dist, max_dist) in dist_bins],
    #         [label for label, _ in dist_bins], p_alt=0.4,
    #         outfile='fdr.png')
    #plot_fn_vs_fp([np.load('output-sim/eval_%s_%s.npz' % (min_dist, max_dist))
    #               for _, (min_dist, max_dist) in dist_bins],
    #              [label for label, _ in dist_bins], xlabel='distance subset', colors='r', outfile='fn_vs_fp.png')
    #plot_fn_vs_fp([[np.load('output-sim/eval_%s_%s.npz' % (min_dist, max_dist))
    #                for _, (min_dist, max_dist) in dist_bins],
    #               [np.load('output-sim/eval_%s_%s.npz' % (min_dist, max_dist))
    #                for _, (min_dist, max_dist) in dist_bins]],
    #              [['a', 'b'], [label for label, _ in dist_bins]], colors=['m', 'c'], xlabel='distance subset', outfile='fn_vs_fp2.png')

    #plot_distance_bias(h, [b for _, b in dist_bins], outfile='distance_bias.png')
    plot_distance_bias([h, h_sim], [b for _, b in dist_bins], idx='disp', threshold=0.05, labels=['real', 'sim'], colors=['m', 'c'], bin_labels=['short', 'mid', 'long'], legend_label='data', outfile='distance_bias2.png')

    #h.prepare_data()
    #h.estimate_disp(n_threads=-1)
    #h.lrt()
    #h.bh()
    #h.classify()
    #h.plot_dispersion_fit('ES', outfile='ddr_es_new.png')
    #h.plot_dispersion_fit('ES', xlim=(0, 20), ylim=(0, 0.004), outfile='ddr_es_zoomed_new.png')
    #h.plot_dispersion_fit('NPC', outfile='ddr_npc_new.png')
    #h.plot_dispersion_fit('NPC', xlim=(0, 20), ylim=(0.001, 0.005), outfile='ddr_npc_zoomed_new.png')
    #h.plot_dispersion_fit('ES', xaxis='mean', yaxis='var',  outfile='mvr_es.png')
    #h.plot_dispersion_fit('NPC', outfile='ddr_npc.png')
    #h.plot_dispersion_fit('NPC', xaxis='mean', yaxis='var',  outfile='mvr_npc.png')
    #h.plot_dispersion_fit('ES', xaxis='dist', yaxis='var', hexbin=False,
    #                      logx=False, logy=False, outfile='dvr_es.png')
    #h.plot_dispersion_fit('ES', xaxis='mean', yaxis='disp', hexbin=False,
    #                      logx=False, outfile='mdr_es.png')
    #h.plot_dispersion_fit('ES', xaxis='mean', yaxis='var', hexbin=False,
    #                      outfile='mvr_es.png')
    #h.plot_dispersion_fit('ES', xaxis='dist', yaxis='disp', logx=False, logy=False,
    #                      outfile='ddr_es.png')
    #h.plot_dispersion_fit('ES', xaxis='dist', yaxis='var', logx=False, logy=False,
    #                      outfile='dvr_es.png')
    #h.plot_dispersion_fit('ES', xaxis='mean', yaxis='disp', logx=False,
    #                      outfile='mdr_es.png')
    #h.plot_dispersion_fit('ES', xaxis='mean', yaxis='var', outfile='mvr_es.png')
    #for d in [5, 10, 25, 50, 75, 100]:
    #    h.plot_dispersion_fit('ES', xaxis='mean', yaxis='var', distance=d,
    #                          xlim=(5, 500), ylim=(1e-5, 1e3),
    #                          logx=False, logy=False,
    #                          outfile='mvr_es_%i.png' % d)

    #h.plot_qvalue_distribution(outfile='qvalues.png')
    #h.plot_ma(0.05, include_non_loops=False, outfile='ma.png')

    #h.simulate('ES')

    #g = Global3DeFDR(
    #    [base_path + '<rep>/<chrom>_raw.npz'.replace('<rep>', repname)
    #    for repname in repnames],
    #    [base_path + '<rep>/<chrom>_kr.bias'.replace('<rep>', repname)
    #    for repname in repnames],
    #    chroms, 'design.csv', 'output-global',
    #    loop_patterns={c: base_path + 'clusters/%s_<chrom>_clusters.json' % c
    #                   for c in ['ES', 'NPC']},
    #    dist_thresh_max=500
    #)
    #g.run_to_qvalues(n_threads=-1)

    #import numpy as np
    #import matplotlib.pyplot as plt
    #xs = np.arange(1001)
    #disp_fn = h.load_disp_fn('ES')
    #disp_per_dist = h.load_data('disp_per_dist')[:, h.design.columns.tolist().index('ES')]
    #plt.plot(xs, disp_fn(xs), color='purple', linewidth=3, label='lowess fit')
    #plt.scatter(xs, disp_per_dist, color='orange', label='per-distance dispersion')
    #plt.ylabel('dispersion')
    #plt.xlabel('distance (bin units)')
    #plt.legend()
    #plt.savefig('fit.png', bbox_inches='tight')


if __name__ == '__main__':
    main()
