from AI.code.utils.util import photo_process
import os,shutil
food_path = "I:\\AI\\数据集\\美食分类\\data\\images"
train_data_path = "data\\goodeat\\train"
val_data_path   = "data\\goodeat\\val"
test_data_path = "data\\goodeat\\test"

traintest_cent = 0.8
trainval_cent = 0.75

# 图片处理
photo_process(food_path, train_data_path, val_data_path, test_data_path, traintest_cent, trainval_cent)
