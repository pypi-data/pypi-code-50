import scrybe
from sklearn.model_selection import KFold
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.datasets import mnist


scrybe.init("scrybe e2e client testing")
mnist_data = mnist.load_data()
batch_size = 128
num_classes = 10
epochs = 2

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


def get_compiled_model():
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


kf = KFold(n_splits=2, shuffle=True, random_state=43)  # Define the split - into 2 folds
print('get_n_splits:', kf.get_n_splits(x_train))
for train_index, test_index in kf.split(x_train):
    X_train, X_test = x_train[train_index], x_train[test_index]
    Y_train, Y_test = y_train[train_index], y_train[test_index]
    # fitting the model and evaluating metrics

    model = get_compiled_model()
    class_weights = {0: 0.1, 1: 0.2, 2: 0.05, 3: 0.05, 4: 0.1, 5: 0.2, 6: 0.05, 7: 0.05, 8: 0.1, 9: 0.1}
    history = model.fit(x=X_train, y=Y_train,
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=1,
                        validation_data=(X_test, Y_test),
                        class_weight=class_weights,
                        callbacks=[]
                        )
    score = model.evaluate(X_test, Y_test, verbose=0)
    print(score)
