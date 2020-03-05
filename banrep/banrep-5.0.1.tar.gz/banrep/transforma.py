# coding: utf-8
"""Módulo para crear modelos de transformación de texto."""
from collections import defaultdict
import warnings

from gensim.corpora import Dictionary
from gensim.models import CoherenceModel
from gensim.models import Phrases
from gensim.models.ldamodel import LdaModel
from gensim.models.phrases import Phraser


def frases_de_palabras(docs):
    """Extrae palabras de cada frase.

    Parameters
    ----------
    docs : Iterable[dict (text: str, tokens: list, meta: dict)]
        Anotaciones lingüísticas de cada frase.

    Yields
    ------
    tuple (list, dict (text: str, tokens: list, meta: dict))
        Palabras de cada frase y Anotaciones lingüísticas.
    """
    for frase in docs:
        yield [t.get("lower_") for t in frase.get("tokens")], frase


def model_ngrams(docs, th=10.0):
    """Crea modelos de ngramas a partir de corpus.

    Parameters
    ----------
    docs : Iterable[dict (text: str, tokens: list, meta: dict)]
        Anotaciones lingüísticas de cada frase.
    th : float
        Score Threshold para formar n-gramas.
        Ver https://radimrehurek.com/gensim/models/phrases.html

    Returns
    -------
    dict
        Modelos Phraser para bigramas y trigramas
    """
    g = (words for words, frase in frases_de_palabras(docs))
    big = Phrases(g, threshold=th)
    bigrams = Phraser(big)

    g = (words for words, frase in frases_de_palabras(docs))
    trig = Phrases(bigrams[g], threshold=th)
    trigrams = Phraser(trig)

    return dict(bigrams=bigrams, trigrams=trigrams)


def ngram_frases(docs, ngrams):
    """Extrae tokens (palabras y n-gramas) de cada frase.

    Parameters
    ----------
    docs : Iterable[dict (text: str, tokens: list, meta: dict)]
        Anotaciones lingüísticas de cada frase.
    ngrams : dict (str, gensim.models.phrases.Phraser)
        Modelos de n-gramas (bigrams, trigrams).

    Yields
    ------
    tuple (list, dict (text: str, tokens: list, meta: dict))
        Palabras y n-gramas de cada frase, y Anotaciones lingüísticas.
    """
    bigrams = ngrams.get("bigrams")
    trigrams = ngrams.get("trigrams")

    for words, frase in frases_de_palabras(docs):
        yield list(trigrams[bigrams[words]]), frase


class Bow:
    """Colección de documentos Bag Of Words.

    Itera frases de documentos y obtiene las palabras de cada uno.
    """

    def __init__(self, docs, ngrams, id_doc, id2word=None):
        """Requiere docs, ngramas, id_doc. Opcional: id2word.

        Parameters
        ----------
        docs : Iterable[dict (text: str, tokens: list, meta: dict)]
            Anotaciones lingüísticas de cada frase.
        ngrams : dict (str: gensim.models.phrases.Phraser)
            Modelos de n-gramas (bigrams, trigrams).
        id_doc : str
            Llave de Metadata que identifica documentos.
        id2word : gensim.corpora.Dictionary, optional
            Diccionario de tokens a considerar.
        """
        self.docs = docs
        self.ngrams = ngrams
        self.id_doc = id_doc
        self.id2word = id2word

        self.n = 0

        if not self.id2word:
            self.id2word = Dictionary(
                tokens for tokens, frase in ngram_frases(self.docs, self.ngrams)
            )
            print(f"Diccionario con {len(self.id2word)} términos creado...")

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"BOW: {self.__len__()} documentos y {len(self.id2word)} términos."

    def __iter__(self):
        """Tokens de cada documento como Bag Of Words.

        Yields
        ------
        tuple (str, list(str), list(tuple(int, int)))
            Identificación única de cada documento y Bags of Words.
        """
        self.n = 0
        for id_doc, tokens in self.doc_tokens().items():
            yield id_doc, tokens, self.id2word.doc2bow(tokens)
            self.n += 1

    def doc_tokens(self):
        """Tokens de cada documento, ya con ngramas.

        Returns
        -------
        dict (str, list(str))
            Tokens de un documento.
        """
        todos = defaultdict(list)
        for tokens, frase in ngram_frases(self.docs, self.ngrams):
            todos[frase.get("meta").get(self.id_doc)].extend(tokens)

        return todos


class ModelosLda:
    """Modelos de tópicos basados en LDA.

    Itera Bags of Words de documentos y crea modelos para diferentes k.
    """

    def __init__(self, bow, kas, params):
        """Requiere bow, kas, params.

        Parameters
        ----------
        bow : banrep.transforma.Bow
            Colección de documentos Bag of Words.
        kas : Iterable[int]
            Diferentes k tópicos para los cuales crear modelo.
        params : dict
            Parámetros requeridos en modelos LDA.
            Ver https://radimrehurek.com/gensim/models/ldamodel.html
        """
        self.bow = bow
        self.kas = kas
        self.params = params

        self.best = 0
        self.score = 0
        self.doc_ids = None

    def __repr__(self):
        fmstr = f"Mejor k={self.best} con Coherence Score={self.score:.3f}"
        return f"Modelos LDA para k en {self.kas}: {fmstr}"

    def __iter__(self):
        """Modelo LDA para cada k.

        Yields
        ------
        dict (k:int, modelo: gensim.models.ldamodel.LdaModel, score: float)
        """
        doc_ids, toks, sparsed = zip(*self.bow)
        self.doc_ids = doc_ids

        for k in self.kas:
            modelo = self.crear_modelo(k, sparsed)
            score = self.evaluar_modelo(modelo, toks)

            if score > self.score:
                self.score = score
                self.best = k

            yield dict(k=k, modelo=modelo, score=score)

    def crear_modelo(self, k, sparsed):
        """Crea modelo LDA de k tópicos.

        Parameters
        ----------
        k : int
            Número de tópicos a usar en modelo.
        sparsed : Iterable[list(tuple(int, int))]
            Bag of Words con id, freq de tokens.

        Returns
        -------
        gensim.models.ldamodel.LdaModel
            Modelo LDA de k tópicos.
        """
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            modelo = LdaModel(
                sparsed, num_topics=k, id2word=self.bow.id2word, **self.params
            )

        return modelo

    def evaluar_modelo(self, modelo, textos):
        """Calcula Coherence Score de modelo de tópicos.

        Parameters
        ----------
        modelo : gensim.models.ldamodel.LdaModel
        textos : Iterable (list[str])
            Palabras de cada documento en un corpus.

        Returns
        -------
        float
            Coherencia calculada.
        """
        cm = CoherenceModel(
            model=modelo,
            texts=textos,
            dictionary=self.bow.id2word,
            coherence="c_v",
        )

        return cm.get_coherence()
