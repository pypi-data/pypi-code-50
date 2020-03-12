from pathlib import Path
from tensorflow.keras import models
import os
import sys
from fcn.FCN import FCN
from tensorflow.keras.utils import plot_model

path = os.path.join(sys.path[0], "focus_detector.h5")
print(os.path.exists(path))
model = models.load_model(path)
model.summary()
plot_model(model, to_file='model.png')
print("Model saved to file")