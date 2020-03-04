import scrybe
import os
from tests.test_mnist_model import get_untrained_model, get_dataset

scrybe.init("scrybe e2e client testing")

(x_train, y_train), (x_test, y_test), (x_val, y_val), input_shape = get_dataset()
x_train = x_train
y_train = y_train

batch_size = 128
epochs = 3
num_classes = 10

mnist_model = get_untrained_model(num_filter_1=2, input_shape=input_shape)
scrybe.log_custom_hyperparameter(model=mnist_model, param_name="model_type", param_value="convnet")
mnist_model.fit(x=x_train, y=y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_val, y_val))
results = mnist_model.evaluate(x_test, y_test)
mnist_model.save("/tmp/convnet_mnist.h5")


from keras.models import load_model
import keras

loaded_model = load_model("/tmp/convnet_mnist.h5")
probas = loaded_model.predict(x_test)
# probas = mnist_model.predict(x_test)
predictions = probas.argmax(axis=-1)
predictions_one_hot = keras.utils.to_categorical(predictions, 10)
y_test_one_hot = y_test
y_test = y_test.argmax(axis=-1)
scrybe.log_code_files(filepaths=[os.path.abspath(__file__), 'test_mnist_model.py'])

from sklearn.metrics import jaccard_score, classification_report, roc_curve, auc, confusion_matrix, \
    precision_recall_curve, multilabel_confusion_matrix, precision_score, recall_score


print("Classification Report")
print(classification_report(y_test, predictions))
print("Jaccard Score")
print(jaccard_score(y_test, predictions, average=None))
print("Precision Score")
print(precision_score(y_test, predictions, average=None))
print("Recall Score")
print(recall_score(y_test, predictions, average=None))
print("multilabel_confusion_matrix")
print(multilabel_confusion_matrix(y_test, predictions))
print("confusion_matrix")
print(confusion_matrix(y_test, predictions))


for i in range(num_classes):
    predicted_digit_probability = probas[:, i]
    actual_digit_probability = y_test_one_hot[:, i]
    fpr, tpr, threshold = roc_curve(actual_digit_probability, predicted_digit_probability)
    precision, recall, _ = precision_recall_curve(actual_digit_probability, predicted_digit_probability)
    print(auc(fpr, tpr))

scrybe.log_code_files(filepaths=[os.path.abspath(__file__), 'test_mnist_model.py'])
