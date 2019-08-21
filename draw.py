import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams['font-sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


 # """ 第一个画直线 """
# x = list(range(10))
# y = [ 2*i  for i in x]
# # return None
# plt.plot(x,y,linewidth="2.0", linestyle="-.")
# plt.show()
# """第二个 画 二次函数的那种凸函数图像"""
plt.figure("静态单图")
x = np.linspace(-3,3,50)
y = x ** 2
plt.plot(x,y,label="凸函数" ,color="red")
plt.legend(loc="lower right")
plt.show()
#
# """ 第三个 画z=w*x的函数动图"""
#
# def move_origin(plt):
#     ax = plt.gca()
#     ax.spines['right'].set_color('none')
#     ax.spines['top'].set_color('none')
#     ax.spines['left'].set_position(('data', 0))
#     ax.spines['bottom'].set_position(('data', 0))
# # x = np.linspace(-5,5,100)
# # w = -10
# # plt.ion()
# # for i in range(100):
# #     y = w*x
# #     w += 1
# #     plt.clf()  #清空后再限定
# #     plt.xlim(-5,5)  # 限定坐标轴的显示范围
# #     plt.ylim(-20,20)
# #     # 画图
# #     plt.plot(x,y)
# #     move_origin(plt)
# #     plt.pause(0.1)  #单位秒
# #
# #     # plt.show()
# # plt.ioff()
#
# """ 第四个 画sigmoid的函数动图"""
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
# x = np.linspace(-5,5,300)
# w = -5
# plt.ion()
# for i in range(60):
#     y = sigmoid(w*x)
#     plt.clf()
#     plt.xlabel("x轴")
#     plt.ylabel("y轴")
#     plt.xlim(-5,5)
#     plt.ylim(0,1)
#     plt.plot(x,y, label="sigmoid函数")
#     plt.legend(loc="upper left")
#     # move_origin(plt)
#     plt.pause(0.1)
#     w += 0.3
# plt.ioff()
# plt.show()
#
# """ 第五个 画正弦曲线的函数图"""
# x = np.linspace(-np.pi, np.pi, 50, endpoint=True)
# y = np.sin(x)
# plt.plot(x,y,label="正弦曲线")
# plt.legend()
# move_origin(plt)
# plt.show()

""" 第六个 画散点图"""
x = np.random.randn(100)
y = np.random.randn(100)
y2 = np.random.randn(100)
# alpha 透明度0~1 越低越透明
plt.scatter(x,y, color="green")
plt.scatter(x,y2, color="red")
plt.show()

""" 第七个 多图"""
x = np.linspace(-5,5,100)
y = 3 * x
y2 = x**2
# plt.figure("多图")
plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.plot(x,y2)
plt.subplot(2,1,2)
plt.plot(x,x**3)
plt.show()


# """"""
#
plt.figure()
plt.subplot(2, 1, 1)  # 分成两行一列，起始点为1
plt.plot([0, 1], [0, 1])  # 设置xy轴范围

plt.subplot(2, 3, 4)  # 分成两行三列，起始点位4
plt.plot([0, 1], [0, 2])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 4])
plt.show()