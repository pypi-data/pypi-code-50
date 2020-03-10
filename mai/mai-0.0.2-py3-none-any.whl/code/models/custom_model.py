
# 更新模型权重
def set_weight(model, weight):
    save_model = torch.load(weight)
    model_dict =  model.state_dict()
    state_dict = {k:v for k,v in save_model.items() if k in model_dict.keys()}
    model_dict.update(state_dict)
    model.load_state_dict(model_dict)

def set_model(model_name, pretrained=False, weight="", gpu=False, testflag=True):
    if args.pretrained:
        print("Model", model_name, "have pretrained model")
        if model_name == 'resnet34':
            model = sai.models.resnet34(pretrained=pretrained)
            if len(weight) > 0: set_weight(model, weight)
            
        elif model_name == 'resnext50_32x4d':
            model = sai.models.resnext50_32x4d(pretrained=False)
            if len(weight) > 0: set_weight(model, weight)
                
        elif model_name == 'resnext101_32x8d':
            model = sai.models.resnext101_32x8d(pretrained=pretrained)
            if len(weight) > 0: set_weight(model, weight)
                
        num_ftrs = model.fc.in_features
        model.fc = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(num_ftrs, 1024),
            nn.Dropout(0.2),
            nn.Linear(1024, 256),
            nn.Dropout(0.2),
            nn.Linear(256, 10),
        )
    else:
        print("Model", args.arch, "isn't have pretrained model")
        model = models.resnet34(pretrained=False)
        model.fc=nn.Linear(num_ftrs, 10)
        
    if args.gpu > -1:
        model = model.cuda()
    else:
        model = model.cpu()
        
    if testflag:
        model = model.eval()
    else:
        model = model.train()
    
    return model

# model = set_model('resnet34', False, "")
