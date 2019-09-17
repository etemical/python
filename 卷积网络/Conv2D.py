import torch.nn as nn
import torch
"""
conv = nn.Conv2d(3,1,3,1)

param = conv.parameters()
weight = next(param).data
bias = next(param).data  

#
# weight = list(conv.parameters())[0].clone().detach()
# bias = list(conv.parameters())[1].clone().detach()
# r = torch.relu(torch.tensor([0,3],dtype=torch.float32))
# print(r) 
# a = torch.randint(20,(6,6,3)).float()
# a = a.permute(2,0,1)
# a = a.unsqueeze(0)

a = torch.randn(1,3,6,6)
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



import numpy as np

try:
    assert(2 == 2)
    print("正确")
except:
    print("错误")


print(5 / np.sqrt(5), np.sqrt(5))
np.random.seed(1)
print(np.multiply(2.1,3.4))
print(np.random.randn(4,5) / 2.23606797749979)
print(np.random.randn(4,5))
"""

"""使用矩阵乘法实现卷积前向计算"""
conv = nn.Conv2d(3,1,3,1)
param = conv.parameters()
w = next(param).data
b = next(param).data
x = torch.randn(1,3,6,6)
y = conv(x)
print(w,b)

w_mat = torch.tensor([])
for i in range(3):
    w_mat = torch.cat((w_mat, w[0,i].flatten()), dim=0)
zeros = torch.zeros((27,16))

print("原始数据:",x)
i = 0
for row in range(4):
    for col in range(4):
        w = torch.tensor([])
        for c in range(3):
            t = x[0,c,row:row+3,col:col+3].flatten()
            w = torch.cat((w,t))
        zeros[0:,i] = w.t()
        i+=1
w_mat = w_mat.unsqueeze(0)

res = torch.matmul(w_mat,zeros) + b
print("系统的结果是:",y)
print("我的结果是:", res.reshape(4,4))