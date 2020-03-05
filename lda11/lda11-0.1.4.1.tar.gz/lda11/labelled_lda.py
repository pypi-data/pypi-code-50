import numpy as np
from numbers import Number
from gc import collect
from ._lda import LDATrainer, log_likelihood_doc_topic, Predictor
from tqdm import tqdm
from ._lda import LabelledLDATrainer
from .lda import (
    RealType, IntegerType, IndexType,
    MultipleContextLDA, number_to_array, check_array,
    bow_row_to_counts, LDAPredictorMixin
)

class LabelledLDA(LDAPredictorMixin):
    def __init__(self, alpha=1e-2, epsilon=1e-30, topic_word_prior=None):
        self.n_components = None
        self.topic_word_prior = topic_word_prior
        self.alpha = alpha 
        self.epsilon = 1e-20
        self.n_vocabs = None
        self.docstate_ = None
        self.components_ = None
        self.predictor = None

    def fit(self, X, Y, n_iter=1000): 
        self._fit(X, Y, n_iter=n_iter)
        return self

    def fit_transform(self, X, Y, **kwargs):
        result = self._fit(X, **kwargs) + self.doc_topic_prior[np.newaxis, :]
        result /= result.sum(axis=1)[:, np.newaxis]
        return result 

    def _fit(self, X, Y, n_iter=1000, ll_freq=10):
        if isinstance(Y, np.ndarray):
            Y = Y.astype(IntegerType) 
        else:
            Y = Y.toarray().astype(IntegerType)

        self.n_components = Y.shape[1]

        self.topic_word_prior = number_to_array(
            X.shape[1], 1 / float(self.n_components),
            self.topic_word_prior
        )

        try:
            count, dix, wix = check_array(X)
        except:
            print('Check for X failed.')
            raise

        doc_topic = np.zeros( (X.shape[0], self.n_components), dtype=IntegerType)
        word_topic = np.zeros( (X.shape[1], self.n_components), dtype=IntegerType) 

        docstate = LabelledLDATrainer(
            self.alpha,
            self.epsilon,
            Y,
            count, dix, wix, self.n_components, 42
        )
        docstate.initialize( doc_topic, word_topic )

        topic_counts = doc_topic.sum(axis=0).astype(IntegerType)

        with tqdm(range(n_iter)) as pbar:
            for i in pbar:
                docstate.iterate_gibbs(
                    self.topic_word_prior,
                    doc_topic,
                    word_topic,
                    topic_counts
                )

        doc_topic_prior = ( self.alpha * np.ones(self.n_components, dtype=RealType) )

        self.components_ = word_topic.transpose() 
        wt = self.components_
        wt = wt + doc_topic_prior[:, np.newaxis]
        wt /= wt.sum(axis=0)[np.newaxis, :]
        wt = wt.astype(RealType)
 
        predictor = Predictor(self.n_components, doc_topic_prior, 42)
        predictor.add_beta(wt)
        self.predictor = predictor

        return doc_topic


