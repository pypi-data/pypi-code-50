import torch.nn as nn

class SiameseNetwork(nn.Module):
      '''
      最简单的孪生网络
      输入形状：
            1，100，100
      输入：
            num_classes(int) 模型测试的类的数目
      例程：
            model = sai.models.twin.SiameseNetwork()
            criterion  = sai.losses.ContrastiveLoss()
            out1, out2 = model(torch.rand(1,1,100,100), torch.rand(1,1,100,100))
            loss = criterion(out1, out2, 1)
      '''
      def __init__(self, num_classes=2):
            super(SiameseNetwork, self).__init__()
            self.cnn1 = nn.Sequential(
                  nn.ReflectionPad2d(1),
                  nn.Conv2d(1, 4, kernel_size=3),
                  nn.ReLU(inplace=True),
                  nn.BatchNorm2d(4),
                  nn.Dropout2d(p=.2),
                  
                  nn.ReflectionPad2d(1),
                  nn.Conv2d(4, 8, kernel_size=3),
                  nn.ReLU(inplace=True),
                  nn.BatchNorm2d(8),
                  nn.Dropout2d(p=.2),
                      
                  nn.ReflectionPad2d(1),
                  nn.Conv2d(8, 8, kernel_size=3),
                  nn.ReLU(inplace=True),
                  nn.BatchNorm2d(8),
                  nn.Dropout2d(p=.2),
                  )
            
            self.fc1 = nn.Sequential(
                  nn.Linear(8*100*100, 500),
                  nn.ReLU(inplace=True),
                  
                  nn.Linear(500, 500),
                  nn.ReLU(inplace=True),
                  
                  nn.Linear(500, num_classes)
                  )

      def forward_once(self, x):
            output = self.cnn1(x)
            output = output.view(output.size()[0], -1)
            output = self.fc1(output)
            return output
      
      def forward(self, input1, input2):
             output1 = self.forward_once(input1)
             output2 = self.forward_once(input2)
             return output1, output2