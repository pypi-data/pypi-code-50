from __future__ import print_function
import scrybe
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
import time

scrybe.init("scrybe e2e client testing")


def train_and_evaluate_keras_model(mnist_data):
    batch_size = 128
    num_classes = 10
    epochs = 3

    # input image dimensions
    img_rows, img_cols = 28, 28

    # the data, split between train and test sets
    (x_train, y_train), (x_test, y_test) = mnist_data

    if K.image_data_format() == 'channels_first':
        x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
        x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
        input_shape = (1, img_rows, img_cols)
    else:
        x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
        x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
        input_shape = (img_rows, img_cols, 1)

    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    print('x_train shape:', x_train.shape)
    print(x_train.shape[0], 'train samples')
    print(x_test.shape[0], 'test samples')

    # convert class vectors to binary class matrices
    x_train = x_train
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)

    activation = 'relu'
    num_filter_1 = 4
    num_filter_2 = 8
    kernal_size_1 = 3
    kernal_size_2 = 5
    num_perceptrons = 16

    model = Sequential()
    model.add(Conv2D(num_filter_1, kernel_size=(kernal_size_1, kernal_size_1),
                     activation=activation,
                     input_shape=input_shape))
    model.add(Conv2D(num_filter_2, (kernal_size_2, kernal_size_2), activation=activation))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(num_perceptrons, activation=activation))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes, activation='softmax'))

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy', 'mse', 'mae'])

    # callback = ModelCheckpoint()
    class_weights = {0: 0.1, 1: 0.2, 2: 0.05, 3: 0.05, 4: 0.1, 5: 0.2, 6: 0.05, 7: 0.05, 8: 0.1, 9: 0.1}
    history = model.fit(x=x_train, y=y_train,
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=1,
                        validation_data=(x_test, y_test),
                        class_weight=class_weights,
                        callbacks=[]
                        )
    score = model.evaluate(x_test, y_test, verbose=0)
    print(score)
    import os
    home_tmp_dir = '%s/tmp' % os.path.expanduser('~')
    model.save('%s/mnist_keras_%s.h5' % (home_tmp_dir, str(time.time())))
    # model.save_weights('mnist_keras_weights_%s.h5' % str(time.time()))

    from keras.models import load_model

    # model2 = load_model('data/mnist_keras.h5')
    # model2.load_weights('data/mnist_keras_weights.h5')

    # t = time.time()
    y_score = model.predict(x_test)
    # latency = (time.time() - t) / y_score.shape[0]
    y_pred = y_score.argmax(axis=-1)
    y_pred = keras.utils.to_categorical(y_pred, num_classes)
    classification_summary = classification_report(y_test, y_pred, output_dict=False)
    acc_score = accuracy_score(y_test, y_pred)
    print(acc_score)
    print(classification_summary)
    fpr = dict()
    tpr = dict()
    threshold = dict()
    roc_auc = dict()
    for i in range(num_classes):
        fpr[i], tpr[i], threshold[i] = roc_curve(y_test[:, i], y_score[:, i])
        roc_auc[i] = auc(fpr[i], tpr[i])

# artifact_model_summary = dict()
# artifact_model_summary['type'] = 'ArtifactModelSummary'
# artifact_model_summary['model_id'] = "id(model_obj)_timestamp"
# artifact_model_summary['model_name'] = "Conv2dnet"
# artifact_model_summary['timestamp'] = int(time.time() * 1000)
# artifact_model_summary['classification_report'] = classification_summary
# artifact_model_summary['accuracy'] = score[1]
# artifact_model_summary['loss'] = score[0]
# artifact_model_summary['latency'] = latency
#
#
# model = dict()
# model['type'] = "Model"
# model['model_id'] = "id(model_obj)_timestamp",
# model['model_name'] = "Conv2dnet"
# model['timestamp'] = int(time.time() * 1000)
# model['approach'] = "Neural Network"
# hyper_param = dict()
# hyper_param['learning_rate'] = "5e-4",
# hyper_param['epoch'] = epochs,
# hyper_param['minibatch'] = batch_size,
# hyper_param['momentum'] = 0.9,
# hyper_param['optimizer'] = "adam",
# hyper_param['loss'] = "categorical_crossentropy"
# spec = dict()
# spec['hyperparameters'] = hyper_param
# spec['model_architecture'] = [
#     {"filters": num_filter_1, "kernel_size": "(%s, %s)" % (kernal_size_1, kernal_size_1), "activation": activation, "kwargs": {"input_shape": "(28, 28, 1)"}, "layer_name": "Conv2D"},
#     {"filters": num_filter_2, "kernel_size": "(%s, %s)" % (kernal_size_2, kernal_size_2), "activation": activation, "layer_name": "Conv2D"},
#     {"pool_size": "(2, 2)", "layer_name": "MaxPooling2D"},
#     {"rate": 0.25, "layer_name": "Dropout"},
#     {"layer_name": "Flatten"},
#     {"units": num_perceptrons, "activation": "relu", "layer_name": "Dense"},
#     {"rate": 0.5, "layer_name": "Dropout"},
#     {"units": 10, "activation": "softmax", "layer_name": "Dense"}
# ]
# model['spec'] = spec
# model['training_metric'] = {
#     "train_accuracy": history.history['acc'],
#     "train_loss": history.history['loss'],
#     "validation_accuracy": history.history['val_acc'],
#     "validation_loss": history.history['val_loss'],
# }
# model['test_metric'] = {
#     'accuracy': score[1],
#     'loss': score[0],
#     'latency': latency
# }
# model['is_pinned'] = False
# model['visibility'] = 0
# # json.dump(model, open("model_%d.json" % int(time.time()), 'w'))
# # json.dump(artifact_model_summary, open("artifact_model_summary_%d.json" % int(time.time()), 'w'))
#
#
# plt.figure()
# for i in range(num_classes):
#     plt.plot(fpr[i], tpr[i], label='ROC curve %d (area = %0.2f)' % (i, roc_auc[i]))
#     plt.plot([0, 1], [0, 1], 'k--')
#     plt.xlim([0.0, 1.0])
#     plt.ylim([0.0, 1.05])
# plt.xlabel('False Positive Rate')
# plt.ylabel('True Positive Rate')
# plt.title('Receiver operating characteristic MNIST')
# plt.legend(loc="lower right")
# plt.show()


TEST_SETUP = """
from __main__ import train_and_evaluate_keras_model; 
from keras.datasets import mnist; 
mnist_data = mnist.load_data()
"""


def get_performance_hit():
    import sys
    from timeit import Timer
    timer = Timer(stmt="train_and_evaluate_keras_model(mnist_data)",
                  setup=TEST_SETUP)
    execs = int(sys.argv[1])
    loops = int(sys.argv[2])
    print("Test parameters execs=%d, loops=%d" % (execs, loops))
    # print(timer.timeit(number=execs))
    res = timer.repeat(repeat=loops, number=execs)
    print("Best of %d loops of %d executions: %f secs" % (loops, execs, min(res)))


def test_keras_model():
    from keras.datasets import mnist
    mnist_data = mnist.load_data()
    train_and_evaluate_keras_model(mnist_data=mnist_data)


test_keras_model()

# python tests/test_keras_model.py 1 5

# Results with 10K samples, 1 layer, 4 filters, batch size: 128
# [Without] Best of 10 loops of 1 executions: 3.410864 secs
# [With] Best of 10 loops of 1 executions: 3.860703 secs

# Results with 60K samples, 1 layer, 4 filters, batch size: 128
# [Without] Best of 5 loops of 1 executions: 7.181346 secs
# [With] Best of 5 loops of 1 executions: 7.664419 secs

# Results with 60K samples, 2 layer, 128 filters + 256 filters, batch size: 64
# [Without] Best of 5 loops of 1 executions: 7.109557 secs
# [With] Best of 5 loops of 1 executions: 7.450594 secs
