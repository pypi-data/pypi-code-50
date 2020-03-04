import itertools

import pandas as pd

from .config import logger
from multiprocessing import Pool


def child_initialize(_scorer, _id_hpo_integers):
    global scorer, id_hpo_integers
    scorer = _scorer
    id_hpo_integers = _id_hpo_integers


def pairwise_scores_from_dataframe(cohort_df, scorer, n_cpus=4):
    """Generate the cross-product of semantic similarity scores for all entities in cohort_df.
    Assumes that the pandas DataFrame has at least two columns [id, hpo_terms]

    :param cohort_df: Pandas DataFrame containing [id, hpo_terms]
    :param n_cpus: number of cpus to use to
    :return: A square pandas DataFrame with semantic similarity scores for the product of all ids.
    """
    if scorer.hrss_array is None:
        logger.critical \
            ('This method is computationally expensive, please pass a valid hrss_array.npy or hrss_array.npy.gz to the scorer class.')
        return

    if cohort_df['id'].duplicated().any():
        logger.critical('This requires unique entity ids, please drop duplicates.')
        return

    # cohort_df['hpo_integers'] = cohort_df['hpo_terms'].apply(scorer.convert_hpos_to_ints)
    id_hpo_integers = {}
    for _, row in cohort_df.iterrows():
        id_hpo_integers[row['id']] = scorer.convert_hpos_to_ints(row['hpo_terms'])

    pairwise_entities = itertools.product(cohort_df['id'], cohort_df['id'])

    if scorer.summarization_method == 'BMA':
        with Pool(n_cpus, initializer=child_initialize, initargs=(scorer, id_hpo_integers)) as p:
            results = p.starmap(scorer.score_bma_from_dataframe, zip(pairwise_entities, itertools.repeat(id_hpo_integers)))
        pairwise_df = pd.DataFrame(results, columns=['a', 'b', 'score'])
        return pairwise_df.set_index(['a', 'b']).unstack()
