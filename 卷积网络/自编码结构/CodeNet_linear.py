import torch.nn as nn
import torch
import torch.nn.functional as F
class EncoderNet(nn.Module):

    def __init__(self):
        super(EncoderNet, self).__init__()
        self.layer = nn.Sequential(
            nn.Linear(784,128),
            nn.ReLU(),
            nn.Linear(128,256),
            nn.ReLU(),
            nn.Linear(256,512),
            nn.ReLU(),
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,10)
        )

    def forward(self, x):
        # x = x.reshape(-1, 784)
        x = self.layer(x)
        return x


class DecoderNet(nn.Module):

    def __init__(self):
        super(DecoderNet, self).__init__()
        self.layer = nn.Sequential(
            nn.Linear(10,128),
            nn.ReLU(),
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Linear(256,512),
            nn.ReLU(),
            nn.Linear(512,256),
            nn.ReLU(),
            nn.Linear(256,128),
            nn.ReLU(),
            nn.Linear(128,784)

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
        x = x.reshape(-1,784)
        x = self.layer(x)
        x = torch.sigmoid(x)
        return x



if __name__ == '__main__':
    x = torch.arange(16, dtype=torch.float).reshape(4,4) + 2

    x = x.unsqueeze(0)
    x = x.unsqueeze(0)
    print(x)
    # maxPool = torch.nn.MaxPool2d(2, stride=2, return_indices=True)
    # out, indices = maxPool(x)
    # print(out)
    # print(indices)
    # unMaxPool = torch.nn.MaxUnpool2d(2, stride=2)
    # print(unMaxPool(out, indices))
    x = nn.UpsamplingBilinear2d(size=torch.Size((9,9)))(x)
    # x = F.interpolate(x, mode="bilinear", align_corners=True, size=torch.Size((9,9)))

    print(x)





