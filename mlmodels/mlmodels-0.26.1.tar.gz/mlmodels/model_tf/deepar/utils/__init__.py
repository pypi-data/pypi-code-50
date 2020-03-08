import numpy as np
import tensorflow as tf
from keras import backend as K


def set_seed_and_reset_graph(seed=42):
    tf.reset_default_graph()
    tf.set_random_seed(seed)
    np.random.seed(seed)


def clear_keras_session():
    K.clear_session()
