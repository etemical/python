import torchvision as tv
from torchvision.transforms import transforms
import torch.optim as optim
import torch.utils.data as data
import torch.nn as nn
import torch
from com.MyNet import NeuralNet
class TrainNet:

    # 初始化网络及相关数据
    def __init__(self):
        self.net = NeuralNet()
        self.loss_func = nn.MSELoss()
        self.optim = optim.Adam(self.net.parameters())
        self.datasets = self.get_datasets()

    #获取数据集
    def get_datasets(self):
        """
         在手写数字识别项目中，Normalize((0.5,), (0.5,)) 归一化且去均值是必须的
         因为训练样本是黑底白字，但是我们手写的图片是白底黑字的
         归一化后可以通过给图片数据乘以-1来达到黑底白字的效果
         以利于检测训练成效
        :return: 字典型数据集
        """
        transform = transforms.Compose([
            transforms.Resize(28),
            transforms.ToTensor(),  # 转张量，并做最大值归一化，即： 0~255 都除以255得到0~1
            transforms.Normalize((0.5,), (0.5,))  # 再做均值方差归一化 (x-mean)/std 得到 -1~1 均值为0.5，标准差也为0.5
        ])
        train_data = tv.datasets.MNIST(root="datasets/",train=True,transform=transform, download=True)
        test_data = tv.datasets.MNIST(root="datasets/", train=False, transform=transform, download=True)
        return {"traindata":train_data,"testdata":test_data}

    # 加载数据集
    def load_data(self,datasets:dict):
        trainloader = data.DataLoader(datasets.get("traindata"),batch_size=600, shuffle=True)
        testloader = data.DataLoader(datasets.get("testdata"), batch_size=500, shuffle=True)
        return trainloader,testloader


    def train(self):
        trainlist , testlist = self.load_data(self.datasets)
        for i in range(10):
            print("epochs:{}".format(i))
            for j, (input,target) in enumerate(trainlist):
                output = self.net(input)
                target = torch.zeros(input.size(0),10).scatter(1,target.view(-1,1),1)
                loss = self.loss_func(output,target)

                self.optim.zero_grad()
                loss.backward()
                self.optim.step()
                if j % 10 == 0:
                    print("{}/{}, 损失为:{}".format(j, len(trainlist), loss.item()))
            with torch.no_grad():
                total = 0
                for input,target in testlist:
                    out = self.net(input)
                    prediction = torch.argmax(out,dim=1)
                    total += (prediction == target).sum()
                accuracy = total.item() / len(self.datasets.get("testdata").data)
                print("正确率:{}".format(str(accuracy * 100) + "%"))
        torch.save(self.net,"models/mynet.pth")





