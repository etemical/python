import torch.nn as nn
import torch

class EncoderNet(nn.Module):

    def __init__(self):
        super(EncoderNet, self).__init__()
        self.layer = nn.Sequential(
            nn.Conv2d(1,32,3,1),  # 26
            nn.ReLU(),
            nn.MaxPool2d(2,2),# 13
            nn.Conv2d(32,64,3,1), # 11
            nn.ReLU(),
            nn.MaxPool2d(2,2),  # 5
            nn.Conv2d(64,128,3,1),   # 3
            nn.ReLU()
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(128,64,3,1),
            nn.ReLU(),
            nn.Conv2d(64,10,1,1),
            nn.ReLU(),
            DecoderNet()
        )


    def forward(self, x):
        x = self.layer(x)
        x = self.layer2(x)
        return x


class DecoderNet(nn.Module):

    def __init__(self):
        super(DecoderNet, self).__init__()
        self.layer = nn.Sequential(
            nn.ConvTranspose2d(10,64,3,1), # n=stride*(n-1) + k - 2*p k取4 方可输出大小为4的feature_map
            nn.ReLU(),
            nn.ConvTranspose2d(64,128,4,1), # 6
            nn.ReLU(),
            nn.ConvTranspose2d(128,64,2,2), # 12
            nn.ReLU(),
            nn.ConvTranspose2d(64,32,3,1), # 14
            nn.ReLU(),
            nn.ConvTranspose2d(32,1,2,2), # 28
            # nn.ReLU(),

    )

    def forward(self, x):
        return self.layer(x)


class AutoCodeNet(nn.Module):

    def __init__(self):
        super(AutoCodeNet, self).__init__()
        self.layer = nn.Sequential(
            EncoderNet(),
            DecoderNet()
        )

    def forward(self, x):
        x = torch.sigmoid(self.layer(x))
        return x


if __name__ == '__main__':
    x = torch.arange(64, dtype=torch.float).reshape(8,8) + 2
    print(x)
    x = x.unsqueeze(0)
    x = x.unsqueeze(0)
    maxPool = torch.nn.MaxPool2d(2, stride=2, return_indices=True)
    out, indices = maxPool(x)
    print(out)
    print(indices)
    unMaxPool = torch.nn.MaxUnpool2d(2, stride=2)
    print(unMaxPool(out, indices))

