import matplotlib.pyplot as plt
""" 解决中文显示  方案一： 
通过字体管理器 然后在需要设置的文字的地方通过 fontproperties 来引用
比较麻烦不推荐使用
"""
# import matplotlib.font_manager as fm
# font = fm.FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")
""" 解决中文显示  方案二： 动态设置字体 SimHei 黑体 （推荐）"""
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

import random
"""************************************** 普通绘制线条 *****************************************"""
x = list(range(1, 5))
y = [e**2 for e in x]
y2 = [e**3+random.uniform(10, 50) for e in x]
print(x, y, y2)
"""  linestyle 
   : 代表点线
   - 默认代表实现
   -- 代表虚线
   -. 代表短线、点相间的虚线
"""
# # plt.plot(x, y, color="red", linewidth=5.0,linestyle=":")
# a = plt.plot(x, y,  y2)
# print(len(a))
# plt.show()

""" 显示图例  方式一 """
# ln1 = plt.plot(x, y, color="red", linewidth=5.0, linestyle=":")
# ln2 = plt.plot(x, y2)
# plt.legend(handles=[ln1[0], ln2[0]], labels=["first label", "second label"],
#            loc="lower right")
# plt.show()

""" 显示图例  方式二 """
# plt.clf()
# ln1 = plt.plot(x, y, color="red", linewidth=5.0, linestyle=":", label="first label")
# ln2 = plt.plot(x, y2, color="blue", label="second label")
#
# plt.legend(loc="best")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.title("main title")
# plt.show()


"""************************************** 结合numpy绘制正弦曲线 *****************************************"""
import numpy as np

""" 生成 -π到π之间的均匀的64个数据 """
# x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)
# print(type(x_data))
# """ 再生成对应的sin函数的值 """`
# print(np.sin(x_data))

# plt.plot(x_data, np.sin(x_data), linestyle=":", linewidth="2.0", label="sin")
# plt.plot(x_data, np.cos(x_data), linestyle=":", linewidth="2.0", label="cos")
# plt.legend(loc="best")
# """通过 gca函数 改变坐标轴的位置，把它移动到原点中心 """
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.spines['left'].set_position(('data', 0))
# ax.spines['bottom'].set_position(('data', 0))
# plt.title("Sin line")
# plt.show()

"""*************************************实时画图 *****************************************"""

# ax, ay = [], []
# plt.ion()  # 开启交互模式
# for i in range(50):
#     ax.append(i)
#     ay.append(i**2)
#     plt.clf()
#     plt.plot(ax, ay)  # 在交互模式下会直接出图像
#     plt.pause(0.1)
#
# plt.ioff()    # 关闭交互模式
"""************************************** 绘制实时动态图 *****************************************"""

x = np.linspace(-5, 5, 200, endpoint=True, dtype=int)
w = -5
plt.ion()
for i in range(100):

    plt.clf()
    """ 限定 x轴和y轴的刻度数字 """
    plt.xlim(-5, 5)
    plt.ylim(-20, 20)
    plt.plot(x, w*x, label="正弦函数")
    """设置坐标轴的名称， rotation 旋转多少度 """
    plt.xlabel("X 轴", fontsize=10, color='red', rotation=0, verticalalignment="top")
    plt.ylabel("Y 轴", fontsize=10, color='blue', rotation=0, horizontalalignment='right')
    plt.legend(loc="upper right")
    """通过 gca函数 改变坐标轴的位置，把它移动到原点中心 """
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    w+=1
    plt.pause(0.1)

plt.ioff()

"""************************************** 绘制散点图 *****************************************"""
""" 随机生成 100个随机数 """
# x = np.random.randn(100)
# y = np.random.randn(100)
# y2 = np.random.randn(100)
# """
#     alpha：透明度
#     c： 颜色
#     s： 半径
# """
# plt.scatter(x, y, alpha=0.6, c="red", s=50)
# plt.scatter(x, y2, edgecolors="yellow", s=50)
# plt.show()
