
""""""
# if __name__ == "__main__":
#     print("ok")
#     i, a = 5, 2
#     try:
#         b = i / a
#         print(b)
#         c = [1, 2, 3, 4, 5, 6, 7, 8]
#         print(c[9])
#     except ZeroDivisionError as e:
#         print(e)
#     except IndexError as e:
#         print("索引越界了", e.args[0])
#     except Exception:
#         print("未知异常")

""" except: 后面不跟异常类型也可以，表示处理所有异常 """
# try:
#     s = input("请输入数字:\n")
#     print("result is :", 15 / int(s))
# except ZeroDivisionError:
#     print("除数不能为零")
# except:
#     print("其他异常")
# finally:
#     print("finish")


"""**************************************raise抛异常*****************************************"""

def validateAge(age):
    if age < 0:
        raise Exception("年龄不能小于0")
    else:
        return age
#
# try:
#     age = input("情输入年龄:\n")
#     age = validateAge(int(age))
#     print("年龄是:", age)
# except Exception as e:
#     print(e.args[0])

""" 导入自定义模块 """
# import test as tt
#
# tt.fun()

# import userinfo as us
#
# u = us.User("dd","dd")
# # u.name = "lis"
# # u.pwd = "123"
# u.work()

# from userinfo import User
#
# u = User("ww", "ddd")
# u.work()
import sys ,os
sys.path.append("/Users/Mical/Documents/python_module")
# a = sys.argv
# print(a[0])
#
#
# b = sys.byteorder
# print(b)
# copyright()
#
# path = sys.executable
# print(path)
#
# print(os.cpu_count())
# print(os.sysconf_names)
"""运行系统的终端命令"""
# os.system("open testx.py")

"""**************************************random 随机数模块*****************************************"""
import random
""" 生成 0~1之间的随机浮点数"""
num = random.random()
print(num)
"""生成 指定区间的随机整数"""
num2 = random.randint(1,50)
print(num2)
"""生成 指定区间的随机浮点数"""
num3 = random.uniform(1, 10)
print("%.2f" % num3)
"""生成 指定区间的随机整数 （可指定步长）"""
num4 = random.randrange(9, 22, 3)
print(num4)

obj = random.choice(['hello', 'world', 3, 5, 6, 23 ])
print(obj)
"""************************************** 日期时间模块 *****************************************"""

import time
# time.sleep(3)
# print("dd")
print(time.gmtime())

import re
p = re.compile("abc")
print(p.search("www.abc.com").group())
print(p.match("abc.com").group())
str = re.sub(r"-", "/", "2019-9-10")
print(str)

email = "^^&&etemical@qq.mail.com"

result = re.search(r"\w+@(\w+[.])+[a-z]{2,3}", email)
print(result.group())


s = set("123")
print(s)
s2 = {",", "2"}
print(type(s2))

print(time.ctime())

a, = (2,)
print(a)