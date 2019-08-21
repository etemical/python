# f = open("/Users/Mical/Documents/问题.txt", "r", True) # True表示加缓冲区，效果更好
# try:
#     while True:
#         ch = f.readline()
#         if not ch:
#             break
#         print(ch)
# except Exception as e:
#     print(e.args[0])
# finally:
#     f.close()

"""**************************************网络编程*****************************************"""

from urllib.parse import *
import json
result = urlparse("http://www.baidu.com")
print(result.path)

from urllib.request import *

f = open("/Users/Mical/Documents/home.html", "w", True, "utf-8")
result = urlopen("http://baijiahao.baidu.com/s?id=1640274268733626413&wfr=spider&for=pc")
data = result.read()
data = data.decode("utf-8")


f.write(data)
f.close()
result.close()
