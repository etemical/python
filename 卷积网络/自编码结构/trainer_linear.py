import torch
import torch.nn as nn
from torch.utils.data import DataLoader,Dataset
from AutoCoder.CodeNet_linear import AutoCodeNet
from torchvision.datasets import MNIST
import torchvision.transforms as trans
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

class Trainer:

    def __init__(self):

        self.net = AutoCodeNet().cuda() if torch.cuda.is_available() else AutoCodeNet()
        self.loss_func = nn.MSELoss()
        self.optimizer = torch.optim.Adam(self.net.parameters())
        self.train_set, self.test_set = self.get_dataset()


    def get_dataset(self):
        transforms = trans.Compose([
            trans.ToTensor(),
            # trans.Normalize((0.5,),(0.5,))
        ])
        train = MNIST(root="datasets/", train=True,  download=False, transform=transforms)
        test =  MNIST(root="datasets/", train=False, download=False, transform=transforms)
        return train,test

    def train(self):

        train_loader = DataLoader(dataset=self.train_set, batch_size=512, shuffle=True)

        for i in range(10):
            print("epochs:{}".format(i))
            for j, (x, y) in enumerate(train_loader):
                if torch.cuda.is_available():
                    x = x.cuda()
                out = self.net(x)
                x = x.reshape(-1, 784)
                loss = self.loss_func(out, x)

                if j % 10 == 0:
                    print("{}/{},loss:{}".format(j, len(train_loader),loss.float()))

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

            torch.save(self.net, "models/net.pth")

    def test(self):
        net = torch.load("models/net.pth")
        # net.eval()
        test_loader = DataLoader(dataset=self.test_set, batch_size=512, shuffle=True)
        for x, y in test_loader:
            if torch.cuda.is_available():
                x = x.cuda()

            out = net(x)
            out = out.reshape(-1,28,28)

            out = (out.data.numpy() * 255).astype(np.uint8)

            x = x.reshape(-1, 28, 28)

            _x  = (x.data.numpy() * 255).astype(np.uint8)

            for i in range(out.shape[0]):
                plt.clf()
                plt.subplot(1,2,1)
                plt.imshow(_x[i])
                plt.subplot(1,2,2)
                plt.imshow(out[i])
                plt.pause(1)


if __name__ == '__main__':

    t = Trainer()
    # t.train()
    t.test()