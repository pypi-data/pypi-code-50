#!/usr/bin/python

""" Pre-processing data to do Sentiment Analysis & Multiclass Classification of portuguese Tweets. """

# Imports & Setup.
import pandas as pd
from nltk.stem import RSLPStemmer
import re
import string
import gensim
from fitanalytics import emoticons


def create_emoticons_tags(column: pd.Series):
    """ Return texts with tags on emoticons. """

    emoticon = emoticons.emoticons_dict
    dict_emoticons = {}
    for key in emoticon.keys():
        for value in emoticon[key]:
            dict_emoticons.update({value: key})

    tagged_texts = []
    for item in column:
        for emj in dict_emoticons.keys():
            if emj in item:
                item = re.sub(emj, dict_emoticons[emj], item)
        tagged_texts.append(item)
    return tagged_texts


def create_url_tags(column: pd.Series):
    """
        Return texts with tags on URLs
        http://www.link.com -> "URL"
    """

    for index, item in enumerate(column):
        for word in item.split():
            if re.match('(https?://(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?://(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})', word):
                item = item.replace(word, 'URL')

    return pd.Series(column)


def create_time_tags(column: pd.Series):
    """
        Return texts with tags on time
        13:30 -> 'horário'
        13h -> 'hora'
        12 min -> 'minuto'
        and so on..
    """
    clear_column = []
    for text in column:
        clear_text = []
        for word in text.split():
            word = re.sub('[1-9]hora|[0-5][0-9]horas|[0-5][0-9]h|[0-9]h', 'hora', word)
            word = re.sub('[1-9]minuto|[0-5][0-9]minutos|[0-5][0-9]min|[0-9]min|[0-5][0-9]m|[0-9]m', 'minuto', word)
            word = re.sub("[1-9]segundo|[0-5][0-9]segundos|[0-5][0-9]seg|[0-9]seg|[0-5][0-9]s|[0-9]s", 'segundo', word)
            word = re.sub('(?:[01]\d|2[0-3]):[0-5][0-9]', 'horário', word)

            clear_text.append(word.lower())
        clear_column.append(' '.join(clear_text))
    return clear_column


def clean_texts(column: pd.Series, stop_words: list):
    """ Return texts free of stopwords, accents, punctuations and twitter mentions """

    string.punctuation = string.punctuation.replace('#', '')
    string.punctuation = string.punctuation.replace('@', '')

    clear_column = []
    for text in column:
        """ Removing stopwords. """
        clear_text = [word for word in str(text).split() if word not in stop_words]

        clear_words = []
        for word in clear_text:

            """ Removing Accents. """
            word = re.sub('[ÂâÃãÄä]', 'a', word)
            # word = re.sub('[Çç]', 'c', word)
            word = re.sub('[ÈèËë]', 'e', word)
            word = re.sub('[ÌìÎîÏï]', 'i', word)
            word = re.sub('[Ññ]', 'n', word)
            word = re.sub('[ÒòÕõÖö]', 'o', word)
            word = re.sub('[Šš]', 's', word)
            word = re.sub('[ùÛÜûÙü]', 'u', word)
            word = re.sub('[ÝýŸÿ]', 'y', word)
            word = re.sub('[Žž]', 'z', word)

            """ Removing multiple vocaaaaals. """
            word = re.sub('[áàãa][áàãa]+', 'a', word.lower())
            word = re.sub('[êe][êe]+', 'e', word.lower())
            word = re.sub('[ií][ií]+', 'i', word.lower())
            word = re.sub('[oóõô][oóõô][oóõô]+', 'o', word.lower())
            word = re.sub('[uú][uú]+', 'u', word.lower())

            """ Removing @user and not A-Z chars. """
            word = re.sub('@\S+|[^A-Za-záÁãÃéÉêÊíÍóÓôÔõÕúÚçÇ]+', ' ', word)
            clear_word = ''.join([letter for letter in word if letter not in string.punctuation])

            """ Removing grouped blank spaces. """
            clear_word = re.sub('(\s)+', ' ', clear_word)

            clear_words.append(clear_word.lower())
        clear_column.append(' '.join(clear_words))

    return clear_column


def stemming(column: pd.Series, stemmer=None):
    """ Return texts stemmed. """
    if stemmer is None:
        stemmer = RSLPStemmer()
    stemmed_texts = []
    for text in column:
        stemmed_texts.append([' '.join(stemmer.stem(word)) for word in text.split()])

    return stemmed_texts


def oversampling(df: pd.DataFrame, column: str):
    """ Balance the DataFrame into equals samples of each class. """
    dict_ = {}
    for key in df[column].value_counts().keys():
        dict_.update({key: df[column].value_counts()[key]})

    sample = max(dict_.values())

    df_oversampled = pd.concat(
        [df[df[column] == key].sample(sample, replace=True, random_state=2) for key in dict_.keys()])

    return df_oversampled


def w2v(df: pd.DataFrame, column: str, max_len: int):
    """ Creates and train word2vec model. """

    w2v_model = gensim.models.word2vec.Word2Vec(size=max_len, window=7, min_count=10, workers=8, seed=5)

    """ Splitting all texts into words. """
    tweets = [text.split() for text in df[column]]

    """ Building the vocabulary. """
    w2v_model.build_vocab(tweets)

    """ Getting size of vocab. """
    # words = w2v_model.wv.vocab.keys()
    # vocab_size = len(words)
    # print("Vocab size: ", vocab_size)

    """ Training the w2v model. """
    w2v_model.train(tweets, total_examples=len(tweets), epochs=32)

    return w2v_model


def pipeline(df: pd.DataFrame, column: str, stop_words):
    """ Executes all pre-processing methods. """

    df[column] = create_emoticons_tags(df[column])
    df[column] = create_url_tags(df[column])
    df[column] = create_time_tags(df[column])
    df[column] = clean_texts(df[column], stop_words)

    return df
