"""打开文件,默认是读"""
import os
f = open("question.txt")
print(f.readable())
# ch = f.read(5)#读取5个字符
# print(ch)
# print(f.read())

# ch = f.readline() # 参数n同样指定读取的字符数,读取的都是上次一没读完的剩下的部分
# print(len(ch))
ch = f.readlines() # 一次性读完所有的返回一个list
print(ch,len(ch))
f.close()
print("=================================================================================")
"""循环读取"""
with open("question.txt") as f:
    ch = f.readlines()
    print(ch)

with open("question.txt") as f:
   for line in f:
       print(line)

f = open("question.txt")
line2 = f.readline()
while  line2 is not "":
    print(line2)
    line2 = f.readline()

print("===========================================================================================================================")

"""写入"""
f = open("newfile.txt","w")
# f.write("hello")
f.write("""你好吗？
我很好，你在哪里呢
我在新加坡
""")

f.close()


f = open("newfile.txt","a")
f.write("wo ai ni ")
f.write("hello")
f.close()

"""追加也不能读"""
f = open("newfile.txt","a")
f.close()

"""写读模式，写完光标在最后，故而读不到，先读也不行，因为此时没内容"""
f = open("newfile.txt","w+")
f.write("这是一个段落")
print(f.read())
f.close()

"""读写模式，光标在开头，可读可写（推荐） 一般先读后写，如果先写后读，则会覆盖已有的内容，读总是在写完以后光标的位置接着读"""
f = open("newfile.txt","r+")
f.write("我再写点")
print(f.read())
f.flush()
f.close()

f = open("question.txt","a+")
# print(f.read())
# f.write("你好吗？")
print(f.fileno())
f.close()
# #
# if not os.path.exists("temp.txt"):
#     # os.mkfifo("temp.txt")
#     f = open("temp.txt","w")
#     f.write("123")
#     f.flush()
#
# else:
#     f = open("temp.txt", "r")
#     print(f.read())
#
# f.close()

import time
f = open("temp.txt","w")
f.write("dddd")
f.flush() # 立即写入硬盘
# time.sleep(5)
print("ok")
f.close()


for i in os.walk(os.getcwd()+"/userinfo"):
    print(i)


#
# j=0
# for i in os.listdir():
#     print(i)
#     os.renames(os.getcwd()+"/temp/"+i,"aa"+str(j+1)+".txt")

    # s = i.replace(i.split(".")[1],str(j+1))
    # print(i,s)
    # os.rename(i,s)
    # j+=1

"""创建文件夹和文件"""

dirpath = os.path.join(os.getcwd(),"temp")
# os.removedirs(dirpath)
#
# 创建文件夹和文件，如果存在就不创建
def createDirAndFile(dirpath,filename):
    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)
    elif not os.path.isfile(os.path.join(dirpath,filename)):
        f = open(os.path.join(dirpath,filename),'w')
        f.close()
    else:
        return True

for i in range(0,10):
    createDirAndFile(dirpath,"{}.0.txt".format(i+1))


def renameFileBybatch(dirpath):

    filelist = os.listdir(dirpath)

    filelist.sort(key=lambda x: int(x[0:x.index(".")]))

    for i, e in enumerate(filelist,start=1):

        newname = e.replace(".{}.".format(e.split(".")[1]) , ".{}.".format(i))
        os.rename(dirpath+"/"+e, dirpath+"/"+newname)

renameFileBybatch(os.path.join(os.getcwd(),"temp"))


# os.getcwd() 返回当前工作目录
# os.path.dirname(path) 返回path的上一层目录
print(os.path.dirname(os.getcwd()))
print(os.getcwd())

# 获取绝对路径
print(os.path.abspath("../../../.."))
for i in os.listdir(os.path.abspath("../..")):
    print(i)
