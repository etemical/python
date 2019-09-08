import torch.nn as nn
import torch

conv = nn.Conv2d(3,1,3,1)


weight = list(conv.parameters())[0].clone().detach()
bias = list(conv.parameters())[1].clone().detach()

a = torch.randint(20,(6,6,3)).float()

a = a.permute(2,0,1)

a = a.unsqueeze(0)
out = conv(a)

channel1 = []
channel2 = []
channel3 = []

a = a.permute(0,2,3,1)

def getfeature_map1():
    panel1 = a[0,:, :, 0]
    rows = 0
    for i in range(4):
        cols = 0
        for j in range(4):
            x = panel1[rows:rows + 3, cols:cols + 3]
            channel1.append((x * weight[0, 0]).sum().item())
            cols += 1
        rows += 1

    feature_map1 = torch.tensor(channel1).view(4, 4)

    return feature_map1



def getfeature_map2():
    panel2 = a[0,:, :, 1]
    rows = 0
    for i in range(4):
        cols = 0
        for j in range(4):
            x = panel2[rows:rows + 3, cols:cols + 3]
            channel2.append((x * weight[0, 1]).sum().item())
            cols += 1
        rows += 1

    feature_map2 = torch.tensor(channel2).view(4, 4)

    return feature_map2



def getfeature_map3():
    panel3 = a[0,:, :, 2]
    rows = 0
    for i in range(4):
        cols = 0
        for j in range(4):
            x = panel3[rows:rows + 3, cols:cols + 3]
            channel3.append((x * weight[0, 2]).sum().item())
            cols += 1
        rows += 1

    feature_map3 = torch.tensor(channel3).view(4, 4)

    return feature_map3


x1 = getfeature_map1()
x2 = getfeature_map2()
x3 = getfeature_map3()

print("我的测算：",(x1+x2+x3)+bias)
print("系统的测算：",out, out.shape)



