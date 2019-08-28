import torch.nn as nn
import torch
class NeuralNet(nn.Module):

    def __init__(self):
        super(NeuralNet, self).__init__()
        self.layer1 = nn.Linear(28*28,128)
        self.relu1 = nn.ReLU()
        self.layer2 = nn.Linear(128,256)
        self.relu2 = nn.ReLU()
        self.layer3 = nn.Linear(256,128)
        self.relu3 = nn.ReLU()
        self.layer4 = nn.Linear(128,10)

    def forward(self, x_data):
        x_data = torch.reshape(x_data,(-1,28*28))
        out1 = self.relu1(self.layer1(x_data))
        out2 = self.relu2(self.layer2(out1))
        out3 = self.relu3(self.layer3(out2))
        return self.layer4(out3)
