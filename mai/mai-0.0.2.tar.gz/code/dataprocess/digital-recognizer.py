# %load AI/code/dataprocess/digital-recognizer.py
# 数据处理，返回的是numpy类型的数据
import kaggle
import os


traindata = pathlib.Path("data\\digit-recognizer\\train.csv")
testdata = pathlib.Path("data\\digit-recognizer\\test.csv")
sample_subdata = pathlib.Path("data\\digit-recognizer\\knn_benchmark.csv")

digital_train_data = pd.read_csv(traindata, dtype=np.float32)
digital_test_data = pd.read_csv(testdata, dtype=np.float32)
# train.label.head()

# 分割数据
targets_np = digital_train_data.label.values
features_np = digital_train_data.loc[:, digital_train_data.columns != 'label'].values/255

final_test_np = digital_test_data.values/255
test_tn = torch.from_numpy(final_test_np)

# 创建一个虚拟的标志
test_target = np.zeros(final_test_np.shape)
test_target = torch.from_numpy(test_target)

# 分割训练与测试集
features_train, features_val, target_train, target_val = train_test_split(features_np, targets_np, test_size=0.2, random_state=42)


train_data = features_train
train_target = torch.from_numpy(target_train).type(torch.LongTensor) # data type is long

# create feature and targets tensor for test set.
val_data = features_val
val_target = torch.from_numpy(target_val).type(torch.LongTensor) # data type is long 

test_data = final_test_np
test_target = test_target.type(torch.LongTensor) # data type is long 
