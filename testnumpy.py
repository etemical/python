import numpy as np

a = np.array([[1,2],[3,4]],dtype=np.int32)
print(a)
print(a.ndim,a.dtype,a.itemsize,a.size,len(a))
print(a.shape)
print(a.reshape(1,4))
b = np.nonzero(5)
print(b)

test = np.matrix([[1,2],[3,4],[5,6]])
print(test)
c = np.mat(np.eye(3))
print(c)

# 定义N阶矩阵
print(np.eye(3,3))
"""
  索引
  切片
  布尔索引
  花式索引
  
"""
a = np.array([1,2,3,4,5])
print(a)
a1 = np.arange(1,10,dtype=np.float)
print(a1[3])
a2 = np.array([[1,2],[3,4],[5,6],[7,8]])
print(a2[1][1])

zeros = np.zeros((3,2),dtype=np.int32)
print(zeros)
ones = np.ones((2,3))
print(ones)

x = a2.astype(np.float) # 复制一个数组，并指定类型
print(x)
x = np.array(['1','2','3','4','5'])
print(x.item(3))
print(a.item(2))
y = x.astype(np.int32)  # y is int type
print(y)

print(y.astype(str)) # y copy with string type
a = np.array([1,2,3],dtype=np.int32)
y = y.astype(a.dtype)
print(y)

""" numpy的运算"""

a = np.array([1,2,3,4,5])
b = np.array([2,4,6,8,1])
c = np.array([3])
print(a*2)
print(a**2)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
""" 向量相乘，求内积 四种写法都可以 矩阵这么用表示求矩阵乘法"""
print(a.dot(b))
print(np.dot(a,b))
print(np.matmul(a,b))
print(a @ b)
a = np.array([1,2,3,4,5])
print(a > 2)
x = a > 2   # x is  [False False  True  True  True]
print(a[x])  #以x为索引，找出True元素所对应的a的元素

b = np.array([1,2,3,3,4])

print(b/a)
c = b/a
""" argwhere 返回符合条件的元素的位置 """
print(np.argwhere(c==1))
print(len(np.argwhere(c==1)))

x = np.array([[0, 1, 2],[3, 4, 5]])
print(len(np.argwhere(x>1)))

"""索引操作 返回索引的最终维度"""
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x[1])
print(x[1][2])
print(x[1,1]) # 等价于x[1][1]
"""切片操作，给范围 : 返回的就是本维度的数组"""
print(x[0:2,0:1])  # [[1] [4]]
print(x[0:2,0])  # [1 4]
print(x[0:2,1:]) # [[2,3],[5,6]]
print(x[0:2,0:2][0]) # [1 2]
print(x[0:2,0:2][0:1]) # [[1 2]]
print(x[0:1,0:3]) # [[1 2 3]]
print(x[0:2,2:3])
print(x[0:2][0:1])
# x[0:1][0:1] = 0
# print(x)
# x[0:1][0:1] = 0,10,100
# print(x)
print(x[0:2,0:2])
x[0:2,0:2] = [(11,22),(44,55)]
print(x)

"""三维的数组"""
x = np.arange(24).reshape(3,4,2)
print(x)

print(x[0:2][0:2][0:1][0][2][1]) # 返回5

"""布尔索引"""
x = np.arange(5)
print(x)
y = np.array([True,False,True,False,False])
z = np.arange(24).reshape(2,3,4)
print(x[y])
print(x[y>0])
print(x[y==False])
print(x[x>1])  # 找出数组里大于1的元素
print(np.argwhere(x>1))
print(x[x==3])
print(z)

print(z[z>2])  # 找出数组里大于2的元素，返回一个一维的数组结果

"""花式索引 以一个整型数组作为索引"""
x = np.arange(6)

print(x)
print(x[[2,3,4]])  #以2，3，4为索引去一次性的索引数组
print(x[[-2,-3]])
"""轴变换 """
x = np.arange(18).reshape(3,6)
print(x)
print(x.T)
print(np.transpose(x,(1,0))) # transpose 轴变换等价于转置操作 对二维数组来说的话
print(x.transpose(1,0))
x = np.arange(18).reshape(2,3,3)
print(x)
print(x.transpose(1,0,2)) # tanspose方式比较复杂，每次都要写完所有维度参数
"""可以用 swapaxes代替 transpose """

print(x.swapaxes(0,1))  #等价于上面的写法


""" 通用函数  一元ufunc函数"""
a = np.array([1,2,3,4,5,6])
print(np.square(a))
print(np.sqrt(a))
print(np.sum(a))
print(np.exp2(a))  #  2的 a每个元素的次方
print(np.mean(a))

"""二元ufunc函数"""
b = np.array([1,3,5,7,8,3])
print(np.maximum(a,b))
print(np.minimum(a,b))  # 求a，b里最小的对应位置元素
print()

""" where函数 后面用的非常多"""
print(np.where(b>1,1,0)) # 返回由条件判断式的结果组成的新数组

print(np.where(b>1))
print(np.argwhere(b>1))  # b>1的元素的下标
"""基本统计操作求平均值"""

x = np.array([[1,2],[3,4],[5,6]])
print(x)
print(x.mean())
print(x.mean(axis=0))  # 行求均值 （感觉是在对列求） 反之亦然
print(x.mean(axis=1))

print(x.sum(axis=0)) # 行求和  [ 9 12]
print(x.sum(axis=1))  # 列求和 [3 7 11]
print(x.max(axis=0))
print(x.max(axis=1))

"""求逆"""
x = np.array([[1,2],[2,1]])
y = np.linalg.inv(x)
print(y)
print(x.dot(y))

x = np.random.rand(9)
print(x)
x2 = np.random.randint(0,2,size=10000)
print((x2>0).sum())