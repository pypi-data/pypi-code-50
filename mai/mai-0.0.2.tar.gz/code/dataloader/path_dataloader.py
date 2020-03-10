# %load AI/code/dataloader/data_dataloader.py
# 制作图片的数据导入器
'''
数据输入：图片路径
类型：
默认值：

数据输出：Tensor
类型：
默认值：
'''
def set_transforms(size):
    normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    train_transformer = transforms.Compose([
        transforms.Resize((size,size)),
#         transforms.Resize((84, 84)),
#         transforms.CenterCrop(84),
        transforms.RandomHorizontalFlip(), # 依概率p水平翻转
        transforms.RandomAffine(degrees=5, translate=(0.05, 0.05), scale=(0.95, 1.05)), # 依概率p转为灰度图
        transforms.ToTensor(),
        normalize
    ])
     
    val_transformer = transforms.Compose([
        transforms.Resize((size,size)),
        transforms.RandomHorizontalFlip(), # 依概率p水平翻转
        transforms.ToTensor(),
        normalize
    ])
    test_data_transform = transforms.Compose([
        transforms.Resize((84, 84)),
        transforms.CenterCrop(84),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return train_transformer,val_transformer,test_data_transform

# 为了划分数据集，和自定义transform 所以参考如下链接写了一个这个
# refer https://blog.csdn.net/ncc1995/article/details/91125964
class MyDataset(Dataset):
    def __init__(self, filenames, labels, transform):
        self.filenames = filenames
        self.labels = labels
        self.transform = transform
 
    def __len__(self):
        return len(self.filenames)
 
    def __getitem__(self, idx):
        image = Image.open(self.filenames[idx]).convert('RGB')
        image = self.transform(image)
        return image, self.labels[idx]
    
def split_Train_Val_Data(data_dir, ratio, size, tbs=64, vbs=64):
    global train_len
    global val_len
    """ the sum of ratio must equal to 1"""
    train_transformer,val_transformer,test_transformer = set_transforms(size)
    dataset = ImageFolder(data_dir)     # data_dir精确到分类目录的上一级
    character = [[] for i in range(len(dataset.classes))]
    print(dataset.class_to_idx)
    print('Train batch-size is {train} Val batch-size is {val}'.format(train=tbs, val=vbs))
    for x, y in dataset.samples:  # 将数据按类标存放
        character[y].append(x)
#     print(dataset.samples)
    train_inputs, val_inputs, test_inputs = [], [], []
    train_labels, val_labels, test_labels = [], [], []
    for i, data in enumerate(character):   # data为一类图片
        num_sample_train = int(len(data) * ratio[0])
        #print(num_sample_train)
        num_sample_val = int(len(data) * ratio[1])
        num_val_index = num_sample_train + num_sample_val
        # 这里打乱一下数据，实验表明，不打乱也没事
        random.seed(7)
        random.shuffle(data)
        
        for x in data[:num_sample_train]:
            train_inputs.append(str(x))
            train_labels.append(i)
        for x in data[num_sample_train:num_val_index]:
            val_inputs.append(str(x))
            val_labels.append(i)
    
    train_len = len(train_inputs)
    val_len = len(val_inputs)
    print("train_length:%d,val length:%d" %(train_len,val_len))
    
    train_dst = MyDataset(train_inputs, train_labels, train_transformer)
    valid_dst = MyDataset(val_inputs, val_labels, val_transformer)
    train_dataloader = DataLoader(train_dst,
                                  batch_size=tbs, shuffle=True)
    val_dataloader = DataLoader(valid_dst,
                                  batch_size=vbs, shuffle=False)
 
    return train_dataloader, val_dataloader
