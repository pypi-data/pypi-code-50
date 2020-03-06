import pickle
import gensim
import numpy as np
from scipy import sparse
import time


from argument_esa_model.similarity import Similarity
import sys
from argument_esa_model.preprocessor import Preprocessor
import argument_esa_model.matrix
sys.modules['matrix'] = argument_esa_model.matrix


class ESA:
    def __init__(self, matrix_path, model_path, vocab_path = None, similarity = "cos"):
        self._pre = Preprocessor(vocab_path)
        self._mat = pickle.load(open(matrix_path, "rb"))
        self._mat_2= self._mat.get_mat().transpose().todense()
        self.index_map = {}
        for term in self._mat.get_terms():
            self.index_map[term]=self._mat.get_terms().index(term)
        self._sim = similarity
        self._model = None
        if similarity != "cos":
            self._model = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format(model_path, binary = True)

    def _to_vector(self, document, lemma):
        if lemma:

            bow = self._pre.to_bow(document, lemma)
            terms_document = tuple(bow.keys())
            length = sum(bow.values())
            vec = sparse.lil_matrix(np.zeros((len(terms_document), 1), dtype = np.longdouble))
            for term in terms_document:
                vec[terms_document.index(term), 0] = bow[term] / length
            vec = sparse.csc_matrix(vec)
            vec.eliminate_zeros()
            return vec, terms_document
        else:
            start = time.time()
            bow = self._pre.to_bow(document, lemma)
            end = time.time()
            print("tokenizing time is %d"%(end - start))
            terms_document = tuple(bow.keys())
            length = sum(bow.values())
            vec = sparse.lil_matrix(np.zeros((len(self._mat.get_terms()), 1), dtype = np.longdouble))
            start = time.time()
            for term in self._mat.get_terms():
                try:
                    vec[self.index_map[term], 0] = bow[term] / length
                except:
                    vec[self.index_map[term], 0] = 0.0
            end = time.time()
            print("tf calculating is %d"%(end - start))
            vec = sparse.csc_matrix(vec)
            vec.eliminate_zeros()
            return vec, terms_document


    def process(self, document, word_level = False):
        if not word_level:
            return self._process_document(document)
        else:
            raise NotImplementedError
            #return self._process_words(document)


    def _process_document(self, document):
        lemma = False
        if self._sim != "cos":
            lemma = True

        start = time.time()
        document_vec, terms_document = self._to_vector(document, lemma)
        end = time.time()
        print("processing time is %d"%(end - start))
        result = {}

        if self._sim == "cos":
            start = time.time()
            result_vector= Similarity.cosine_similarity(document_vec, self._mat_2)
            end = time.time()
            print("similarity calculating time is %d"%(end - start))
            for i,concept in enumerate(self._mat.get_concepts()):
                result[concept] = result_vector[i]

        elif self._sim == "max":
            for concept in self._mat.get_concepts():
                res = Similarity.maximum_matching_similarity(self._model, document_vec, self._mat[concept], terms_document, self._mat._terms)
                result[concept] = res
        elif self._sim == "avg":
                raise NotImplementedError
        return result

'''
    def _process_words(self, document):
        results = {}
        terms = self._mat.get_terms()
        for word in self._pre.to_bow(document):
            if word in terms:
                vec = sparse.lil_matrix(np.zeros((len(terms), 1), dtype = np.longdouble))
                vec[terms.index(word), 0] = 1.0
                vec = sparse.csc_matrix(vec)
                vec.eliminate_zeros()
                intermediate = {}
                for concept in self._mat.get_concepts():
                    intermediate[concept] = self._sim.compute_similarity(vec, self._mat[concept])
                intermediate = sorted(intermediate.items(), key = lambda x : x[1], reverse = True)
                results[word] = intermediate[0][0]
        return results
'''
