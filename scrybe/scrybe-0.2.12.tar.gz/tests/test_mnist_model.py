import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K


def get_untrained_model(num_filter_1, input_shape, num_classes=10):
    activation = 'relu'
    num_filter_2 = 8
    kernal_size_1 = 3
    kernal_size_2 = 3
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
    return model


def get_dataset():
    num_classes = 10
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    # input image dimensions
    img_rows, img_cols = 28, 28

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
    y_train = keras.utils.to_categorical(y_train, num_classes)
    y_test = keras.utils.to_categorical(y_test, num_classes)
    return (x_train, y_train), (x_test[:5000], y_test[:5000]), (x_test[5000:], y_test[5000:]), input_shape
