# -*- coding: utf-8 -*-

import torch
import torch.nn as nn
import torch.optim as optim

"""

   MSELoss （均）方差损失，公式为 (h-y)**2, 即返回矩阵或向量形式的一组loss，如果对其求均值的话，即返回标量形式的loss，即使把损失求和再除以样本数
   
   
 　Ａ reduce = False，返回向量形式的 loss　

　　Ｂ　reduce = True， 返回标量形式的loss

    C  size_average = True，返回 loss.mean();

　　D  如果 size_average = False，返回 loss.sum()
 
  现在不推荐 reduce和size_average了，转而用 reduction来代替

"""
input = torch.autograd.Variable(torch.randn(3,4))
target = torch.autograd.Variable(torch.randn(3,4))

# loss_fn = torch.nn.MSELoss(reduce=False, size_average=False)
# loss_fn2 = torch.nn.MSELoss(reduce=True, size_average=True)
loss_fn = nn.MSELoss(reduction='none') # 返回矩阵形式的loss，公式为 (h - y)**2
loss_fn2 = nn.MSELoss(reduction='mean' ) #  返回均值形式的loss，即标量
#loss_fn = torch.nn.MSELoss()

loss = loss_fn(input, target)
print(input);
print(target);


print("矩阵形式的loss：",loss)
print(input.size(), target.size(), loss.size())
print(loss.sum()/12)

print("=============================================================================================================")


loss2 = loss_fn2(input,target)
print("平均损失:", loss2)


