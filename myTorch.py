import torch
from torch.autograd import Variable

#  3行2列的tensor矩阵
a = torch.Tensor(3,2)
print(a)
print(a.size())
b = torch.Tensor(3,2,2)
print(b)
c = torch.IntTensor(2,2)
print(c)
print(torch.ByteTensor(3,2))
print(torch.CharTensor(3,2))
print(torch.DoubleTensor(3,2))

a = torch.arange(6).view(3,2)
print(a)
b = torch.arange(6).view(2,3)
print(b)

print(a @ b)

# print(torch.dot(a,b))# dot只能用于一维向量
print(torch.matmul(a,b))
print(torch.mm(a,b))  # 数学中的矩阵乘法

print(a.t())
print(a.numel()) # 求a中的元素个数

a = torch.arange(1,4)
b = torch.arange(1,4)
print(a,b)
print(a.dot(b))  # 向量相乘 ，求内积 这点和numpy一样

"""反向求导 链式法则"""
# a = torch.tensor([1.,3.], requires_grad=True)
# print(a)
# y = a + 2
# y = Variable(y, requires_grad=True) # 通过Variable包装张量
# # y = (a +2).clone().detach().requires_grad_(True)
#
# print(y)
# z = y ** 2
# g = z.mean()
# g.backward()
# print(y.grad)

        

a = torch.tensor([[1.,3.],[2,4]], requires_grad=True)
print(a)
y = a + 2
y = Variable(y, requires_grad=True) # 通过Variable包装张量
# y = (a +2).clone().detach().requires_grad_(True)

print(y)
z = y ** 2
g = z.mean()
g.backward()
print(y.grad)
