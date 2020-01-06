import torch.nn as nn
import torch
import torch.nn.functional as F
class AutoEncodeNet(nn.Module):

    """
    这是用的上采样算法
    效果一般，不如转置卷积好
    """

    def __init__(self):
        super(AutoEncodeNet, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 32, 3, 1),  # 26
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  # 13
            nn.Conv2d(32, 64, 3, 1),  # 11
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  # 5
            nn.Conv2d(64, 128, 3, 1),  # 3
            nn.ReLU()

        )

        self.decoder = nn.Sequential(

            nn.Conv2d(128, 128, 3, 1,padding=2),  # n=stride*(n-1) + k - 2*p k取4 方可输出大小为4的feature_map
            nn.ReLU(),
            nn.Conv2d(128, 64, 3, 1, padding=2),  # n=stride*(n-1) + k - 2*p k取4 方可输出大小为4的feature_map
            nn.ReLU(),
            nn.UpsamplingBilinear2d(scale_factor=2),
            nn.Conv2d(64, 32, 3, 1, padding=1),
            nn.ReLU(),
            nn.UpsamplingBilinear2d(scale_factor=2),
            nn.Conv2d(32, 1, 3, 1 ,padding=1)

        )


    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# class DecoderNet(nn.Module):
#
#     def __init__(self):
#         super(DecoderNet, self).__init__()
#         self.layer = nn.Sequential(
#             nn.ConvTranspose2d(10,64,3,1), # n=stride*(n-1) + k - 2*p k取4 方可输出大小为4的feature_map
#             nn.ReLU(),
#             nn.ConvTranspose2d(64,128,3,1), # 5
#             nn.ReLU(),
#             nn.UpsamplingBilinear2d(size=torch.Size((11,11))),
#             nn.ConvTranspose2d(128,64,3,1),
#             nn.ReLU(),
#             nn.UpsamplingBilinear2d(scale_factor=2),
#             nn.ConvTranspose2d(64,32,3,1),
#             nn.ReLU(),
#             nn.ConvTranspose2d(32,1,1,1)
#     )
#
#     def forward(self, x):
#         return self.layer(x)
#
#
# class AutoCodeNet(nn.Module):
#
#     def __init__(self):
#         super(AutoCodeNet, self).__init__()
#         self.layer = nn.Sequential(
#             AutoEncodeNet(),
#             DecoderNet()
#         )
#
#     def forward(self, x):
#         return self.layer(x)


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





