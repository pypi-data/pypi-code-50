# %load AI/code/dataloader/data_dataloader.py
# 制作数据的数据导入器
'''
数据输入：numpy
类型：
默认值：

数据输出：Tensor
类型：
默认值：
'''

train_data_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])
val_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])
test_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize([0.5], [0.5])
])

# 设置batch大小
train_batch_size = 256
val_batch_size = 256
test_batch_size = 256

# DataSet类 - （数字类）
train_dataset = torch.utils.data.TensorDataset(torch.from_numpy(train_data), train_target)
val_dataset = torch.utils.data.TensorDataset(torch.from_numpy(val_data), val_target)
test_dataset = torch.utils.data.TensorDataset(torch.from_numpy(test_data), test_target)

# 数据加载器
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size = train_batch_size, shuffle = True)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size = val_batch_size, shuffle = True)
test_loader = torch.utils.data.DataLoader(test_dataset, batch_size = test_batch_size, shuffle = False)
