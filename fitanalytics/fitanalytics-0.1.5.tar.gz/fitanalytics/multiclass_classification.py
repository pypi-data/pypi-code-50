#!/usr/bin/python

# Imports & Setup.
import numpy as np
import pandas as pd
import pickle
import preprocessing as pp

from keras.callbacks import ReduceLROnPlateau, EarlyStopping
from keras.layers import Embedding
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import f1_score


class MulticlassClassification:

    def __init__(self, data: pd.DataFrame, text: str, target: str, output_filename: str, model=None,
                 word_embeddings=None, max_len=100, stop_words=None):
        self.data = data
        self.text = text
        self.target = target
        self.output_filename = output_filename
        self.tokenizer = Tokenizer()
        self.model = model
        self.w2v_model = word_embeddings
        self.max_len = max_len
        self.stop_words = stop_words

    @staticmethod
    def create_model(units=100, dense_neurons=3, embedding_layer=None):
        # print('creating model \n')
        model = Sequential()
        model.add(embedding_layer)
        model.add(Dropout(0.4, seed=5))
        model.add(LSTM(units, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(dense_neurons, activation='softmax'))

        model.summary()
        return model

    def classification(self):
        """ Returns a sentiment_analysis model, trained with 'text' inputs and 'target' labels in 'data' file
            also, saves the model with the 'output filename'.
        """

        # Clean texts
        if self.stop_words is None:
            from nltk.corpus import stopwords
            self.stop_words = stopwords.words('portuguese')

        # pipeline will execute all pré-processing processes:
            # create_emoticons_tags, create_url_tags, create_time_tags, clean_texts
        self.data = pp.pipeline(self.data, column=self.text, stop_words=self.stop_words)

        # Oversampling the data to fix class imbalance
        self.data = pp.oversampling(self.data, column=self.target)

        # Creating our Word2Vec model if it not exists
        if self.w2v_model is None:
            self.w2v_model = pp.w2v(self.data, column=self.text, max_len=self.max_len)

        # Tokenizing
        self.tokenizer.fit_on_texts(self.data[self.text])
        vocab_size = len(self.tokenizer.word_index) + 1

        # Padding texts to create our input data X
        x = pad_sequences(self.tokenizer.texts_to_sequences(self.data[self.text]), maxlen=self.max_len)

        # Creating the encoder to set our Y in categorical format
        encoder = LabelEncoder()
        encoder.fit(self.data[self.target].tolist())
        y_encoded = encoder.transform(self.data[self.target].tolist())
        y = np_utils.to_categorical(y_encoded)

        # Now that we have our data preprocessed, we can split it into train/test
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=52)

        # Creating Embedding Matrix
        embedding_matrix = np.zeros((vocab_size, self.max_len))
        for word, i in self.tokenizer.word_index.items():
            if word in self.w2v_model.wv:
                embedding_matrix[i] = self.w2v_model.wv[word]

        # Creating Embedding Layer with Embedding Matrix
        embedding_layer = Embedding(vocab_size, self.max_len, weights=[embedding_matrix], input_length=self.max_len,
                                    trainable=False)

        # Creating the Model
        if self.model is None:
            self.model = self.create_model(
                dense_neurons=self.data[self.target].value_counts().count(),
                embedding_layer=embedding_layer
            )

            # Compile and Run the model
            self.model.compile(loss='binary_crossentropy', optimizer="adam", metrics=['accuracy'])
            callbacks = [ReduceLROnPlateau(monitor='val_loss', patience=5, cooldown=0),
                         EarlyStopping(monitor='val_accuracy', min_delta=1e-4, patience=5)]

            self.model.fit(x_train, y_train, batch_size=1024, epochs=5, validation_split=0.3,
                           verbose=1, callbacks=callbacks)

        # Evaluating
        self.make_evaluation(x_test, y_test)

        # saving model to output file
        filename = str(self.output_filename + '.sav')
        pickle.dump(self.model, open(filename, 'wb'))
        return self.model

    @staticmethod
    def ohe(score):
        """ Returns One Hot Encoding of score """
        index = score.argmax()
        vector = np.zeros(len(score), dtype=int)
        vector[index] = 1
        return vector

    def make_evaluation(self, x_test, y_test):
        ev_score = self.model.evaluate(x_test, y_test, batch_size=1024)
        # print("Accuracy = ", ev_score[1])
        # print("\nLoss = ", ev_score[0])

        f1_y = np.array([self.ohe(y) for y in self.model.predict(x_test)])
        print('F1-Score:')
        f1_score(y_test, f1_y, average='samples')

        print('Precision, Recall, F-Score, Support')
        precision_recall_fscore_support(y_test, f1_y, average='samples')

    @staticmethod
    def decode_sentiment(score, label_order: list):
        return list(dict(label_order).keys())[score.argmax()]

    def make_prediction(self, sample: str):
        # start_at = time.time()

        # Tokenize text
        x_test = pad_sequences(self.tokenizer.texts_to_sequences([sample]), maxlen=self.max_len)

        # Predict
        score = self.model.predict([x_test])[0]

        label_order = self.data[self.target].value_counts().sort_index()

        # Decode sentiment
        label = self.decode_sentiment(score, label_order)
        print('Predicted: ', label)

        return label
