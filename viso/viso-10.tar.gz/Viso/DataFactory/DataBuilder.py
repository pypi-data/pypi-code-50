import pandas as pd
import json


def pandaBuilder(output, actual, predicted, classes):
    probdf = pd.DataFrame(output, columns=["P-" + str(mclass) for mclass in classes])

    predicted = [str(classes[int(pre)]) for pre in predicted]
    predicteddf = pd.DataFrame(predicted, columns=['Predicted'])

    actual = [str(classes[int(act)]) for act in actual]
    actualdf = pd.DataFrame(actual, columns=['A-Digit'])

    df = actualdf.join(predicteddf.join(probdf))

    j = df.to_dict(orient="records")
    return j


def importData(epochs, output, actual, predicted, classes):
    data = []
    for i in range(epochs):
        epochJson = pandaBuilder(output[i], actual, predicted, classes)
        data.append(epochJson)
    return data