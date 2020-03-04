import scrybe
import keras
import pandas
from keras import Sequential
from keras.layers import Dense, Dropout
from sklearn import model_selection
from sklearn.preprocessing import LabelBinarizer


scrybe.init("scrybe e2e client testing")

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)


array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                random_state=seed)

encoder = LabelBinarizer()
y_train_one_hot = encoder.fit_transform(Y_train)
y_true_one_hot = encoder.fit_transform(Y_validation)
activation = 'sigmoid'
model = Sequential()
model.add(Dense(4, activation=activation))
model.add(Dense(20, activation=activation))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy', 'mse', 'mae'])

model.fit(x=X_train, y=y_train_one_hot, batch_size=4, epochs=3, validation_data=(X_validation, y_true_one_hot))
print(model.evaluate(x=X_validation, y=y_true_one_hot))
feature_importances = {
    'sepal-length': 0.2,
    'sepal-width': 0.4,
    'petal-length': 0.1,
    'petal-width': 0.3
}
scrybe.log_feature_importances(model, feature_importances=feature_importances)



