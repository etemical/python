import cv2
import numpy as np

img = cv2.imread("../img/pic.jpg")
#
#
# img = cv2.addText(img,"小黄人",(200,300),"Avenir Next.ttc",pointSize=2,color=(255,255,0))
#
# cv2.imshow("image",img)

# cv2.resizeWindow("image",300,600)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 获取图片的总数据 三个通道加起来
print(img.size)
# 获取形状
# print(img.shape)
#
# cv2.imshow("img1",img[:,:,0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 可以直接打印img的数据内容，默认ndarray
print(img)
print(cv2.split(img))

# # 灰度处理
# img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# print(img)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# img = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.line(img,(0,0),(300,300),color=(0,255,0),thickness=3)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# img = cv2.rectangle(img,(300,400),(400,500),(0,255,0),3)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# img = cv2.circle(img,(350,450),80,(0,255,0),3)
# cv2.imshow("circle",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower_red = np.array([20, 15, 10])
# upper_red = np.array([220, 200, 200])
# mask = cv2.inRange(hsv, lower_red, upper_red)
# cv2.imshow("image",mask)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

""" 读取视频"""
# cap = cv2.VideoCapture("/Users/Mical/Movies/小视频/舞蹈.mp4")
# flag,frame = cap.read() # 读取每一帧
#
# cv2.imshow("video",frame)
# # 转换到 HSV
# hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
# # 设定红色的阈值
# lower_red=np.array([160,0,0])
# upper_red=np.array([360,255,255])
# # 根据阈值构建掩模
# mask=cv2.inRange(hsv,lower_red,upper_red)
# # 对原图像和掩模进行位运算
# res=cv2.bitwise_and(frame,frame,mask=mask)
# # 显示图像
# cv2.imshow('frame',frame)
# cv2.imshow('mask',mask)
# cv2.imshow('res',res)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

