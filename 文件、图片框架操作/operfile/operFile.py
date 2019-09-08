"""只读操作"""
# f = open("/Users/Mical/Documents/问题.txt",'r')
# data = f.read() # read(n)
# n为字符数，一次读指定字符数的字符
# # data = f.readline() # 一次读取一行，结尾带有 \n
# # data2 = f.readline()
# # data3 = f.readline()
# # print(data)
# # print(data2)
# # print(data3)
# data = f.readlines() # 读取所有文本装到一个list中，容易造成内存溢出，不推荐
# print(data)
# f.close()


"""循环读取，一次读取一行 (推荐，不会造成内存溢出)"""
# f = open("/Users/Mical/Documents/问题.txt",'r')
# for line in f:
#     print(line.strip())
# f.close()


"""只写文件"""
f = open("mical.txt","w")
f.write("hello")
f.writelines("\n")
f.write("world")
f.flush()
f.close()
#
# """追加模式a, 会在末尾追加 (不可以读)"""
# f = open("mical.txt","a")
# f.write("你好吗")
# f.flush()
# f.close()

"""读写模式（先读后写）光标在开头 r+模式，可读可写，"""
# f = open("mical.txt","r+")
# print(f.read())
# f.write("hello")
# f.write("world")
# f.flush()
# f.close()

"""写读模式（先写后读，读不到，因为写完光标在后面没内容）"""
# f = open("mical.txt","w+")
# f.write("123")
# f.write("456")
# print(f.read())
# f.flush()
# f.close()

"""追加读模式，a+ 无论先读后写还是先写后读都读不到内容"""
f = open("mical.txt","a+")
# data = f.read()
# print(data)
f.write("杂七杂八")
f.flush()
f.close()


with open("/Users/Mical/Documents/问题.txt") as f,\
        open("/Users/Mical/Documents/问题3.txt","w") as f2:
    f2.write(f.read())


"""复制，移动文件的模块 """
import shutil

s  = shutil.copy("/Users/Mical/Documents/问题.txt","/Users/Mical/Documents/问题2.txt")

print(s)