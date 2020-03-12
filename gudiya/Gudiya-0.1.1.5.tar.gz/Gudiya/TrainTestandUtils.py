
'''

This code has been proudly written by Ravi Teja with inspiration from his team
members

Noopur Agrawal
GaneshKumar C
Nithyaganesh



'''


from tqdm import tqdm
import torch
import torch.nn.functional as F
from torchsummary import summary
import matplotlib.pyplot as plt
import numpy as np
import torchvision
import torchvision.transforms as transforms

class TrainTestandUtils():
    def __init__(self, model,optimizer,criterion,scheduler,epochs,input_size,classes):
        self.transform = transforms.Compose(
            [transforms.RandomCrop(32, padding=4),
             transforms.RandomHorizontalFlip(),
             transforms.ToTensor(),
             transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

        self.trainset = torchvision.datasets.CIFAR10(root='./data', train=True,
                                                download=True, transform=self.transform)
        self.trainloader = torch.utils.data.DataLoader(self.trainset, batch_size=256,
                                                       shuffle=True, num_workers=4)

        self.testset = torchvision.datasets.CIFAR10(root='./data', train=False,
                                               download=True, transform=self.transform)
        self.testloader = torch.utils.data.DataLoader(self.testset, batch_size=256,
                                                      shuffle=False, num_workers=4)
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.scheduler = scheduler
        self.epochs=epochs
        self.train_losses =[]
        self.test_losses = []
        self.train_acc=[]
        self.total_train_accuracy =[]
        self.total_test_accuracy =[]
        self.misclassified_images = []
        self.input_size = input_size
        self.classes = classes
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


    # Function to display the summary
    def disp_summary(self):
        summary(self.model,input_size=self.input_size)


    # Training model function
    def trainModel(self,curr_epoch):
        self.model.train()
        correct = 0
        processed = 0
        pbar = tqdm(self.trainloader)
        for batch_idx, (data, target) in enumerate(pbar):
            # get samples
            data, target = data.to(self.device), target.to(self.device)

            # Init
            self.optimizer.zero_grad()
            # In PyTorch, we need to set the gradients to zero before starting to do backpropragation because PyTorch accumulates the gradients on subsequent backward passes.
            # Because of this, when you start your training loop, ideally you should zero out the gradients so that you do the parameter update correctly.

            # Predict
            y_pred = self.model(data)

            # Calculate loss
            # loss = F.nll_loss(y_pred, target)
            loss = self.criterion(y_pred, target)
            self.train_losses.append(loss)

            # Backpropagation
            loss.backward()
            self.optimizer.step()

            # Update pbar-tqdm

            pred = y_pred.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
            correct += pred.eq(target.view_as(pred)).sum().item()
            processed += len(data)
            pbar.set_description(
                desc=f'Loss={loss.item()} Batch_id={batch_idx} Accuracy={100 * correct / processed:0.2f}')
            self.train_acc.append(100 * correct / processed)

        train_acc = 100 * correct/processed
        self.total_train_accuracy.append(train_acc)


    def TestModel(self,curr_epoch):
        self.model.eval()
        testloss = 0
        correct = 0
        with torch.no_grad():
            for data, target in self.testloader:
                data, target = data.to(self.device), target.to(self.device)
                output = self.model(data)
                testloss += self.criterion(output, target).item()  # sum up batch loss
                pred = output.argmax(dim=1, keepdim=True)  # get the index of the max log-probability
                is_correct = pred.eq(target.view_as(pred))
                if curr_epoch == self.epochs:
                    misclassified_inds = (is_correct == 0).nonzero()[:, 0]
                    for mis_ind in misclassified_inds:
                        if len(self.misclassified_images) == 25:
                            break
                        self.misclassified_images.append({
                            "target": target[mis_ind].cpu().numpy(),
                            "pred": pred[mis_ind][0].cpu().numpy(),
                            "img": data[mis_ind].cpu().numpy()
                        })
                correct += is_correct.sum().item()

        testloss /= len(self.testloader.dataset)
        self.test_losses.append(testloss)

        test_acc = 100. * correct / len(self.testloader.dataset)
        self.total_test_accuracy.append(test_acc)

        print('Test set: Average loss: {:.4f}, Accuracy: {}/{} ({:.2f}%)\n'.format(
            testloss, correct, len(self.testloader.dataset), test_acc))

    def runModel(self):
        for curr_epoch in range(1,self.epochs+1):
            print ("EPOCH  {}".format(curr_epoch))
            self.trainModel(curr_epoch)
            self.scheduler.step()
            self.TestModel(curr_epoch)


    def plot_misclassified(self,img_name):
        # new function here
        plt.figure(figsize=(10, 10))

        num_of_images = len(self.misclassified_images)
        for index in range(1, num_of_images + 1):
            img = self.misclassified_images[index - 1]["img"] / 2 + 0.5  # unnormalize
            plt.subplot(5, 5, index)
            plt.axis('off')
            plt.imshow(np.transpose(img, (1, 2, 0)))
            plt.title("Predicted: %s\nActual: %s" % (
            self.classes[self.misclassified_images[index - 1]["pred"]],
            self.classes[self.misclassified_images[index - 1]["target"]]))

        plt.tight_layout()
        plt.savefig(img_name)
        plt.show()

    # Defining classwise Accuracy
    def classwise_acc(self):
        class_correct = list(0. for i in range(10))
        class_total = list(0. for i in range(10))
        with torch.no_grad():
            for images, labels in self.testloader:
                images, labels = images.to(self.device), labels.to(self.device)
                outputs = self.model(images)
                _, predicted = torch.max(outputs, 1)
                c = (predicted == labels).squeeze()
                for i in range(4):
                    label = labels[i]
                    class_correct[label] += c[i].item()
                    class_total[label] += 1

        # print class-wise test accuracies
        print()
        for i in range(10):
            print('Accuracy of %5s : %2d %%' % (
                self.classes[i], 100 * class_correct[i] / class_total[i]))
        print()

    # Function to plot the image
    def plot_train_images(self):
        dataiter = iter(self.trainloader)
        images,labels = dataiter.next()
        disp_img = torchvision.utils.make_grid(images)
        disp_img = disp_img / 2 + 0.5  # unnormalize
        npimg = disp_img.numpy()
        plt.imshow(np.transpose(npimg, (1, 2, 0)))

    # Display accuracy of the total network
    def total_accuracy(self):
        correct = 0
        total = 0
        with torch.no_grad():
            for data in self.testloader:
                images, labels = data[0].to(self.device), data[1].to(self.device)
                outputs = self.model(images)
                _, predicted = torch.max(outputs.data, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        print('Accuracy of the network on the 10000 test images: %d %%' % (100 * correct / total))

    # Plot graph
    def plot_train_test_acc(self):
        plt.figure(1, figsize=(20, 8))
        plt.xticks(range(1, self.epochs+1), fontsize=15)
        plt.yticks(fontsize=15)
        #print ("Length of train acc is {}".format(len(self.total_train_accuracy)))
        #print("Length of test acc is {}".format(len(self.total_test_accuracy)))
        plt.plot(range(1, self.epochs+1), self.total_test_accuracy, '-b', label='Test Accuracy')
        plt.plot(range(1, self.epochs+1), self.total_train_accuracy, '-r', label='Train Accuracy')
        plt.legend(loc=0, fontsize=15)
        plt.title("ACC FOR {} EPOCHS".format(self.epochs))
        plt.show()

