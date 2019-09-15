import cv2
import numpy as np
import dlib

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

#
#
# camera = cv2.VideoCapture(0)
# success , frame = camera.read()
# while success and cv2.waitKey(1) == -1:
#     success, frame = camera.read()    # TODO:在此处可放置各种对当前每一帧图像的处理
#     cv2.imshow("Camera", frame)
#
# camera.release()
# cv2.destroyAllWindows()


cameraCapture = cv2.VideoCapture(0)
success, frame = cameraCapture.read()
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(    "shape_predictor_68_face_landmarks.dat")

while success and cv2.waitKey(1) == -1:
    success, frame = cameraCapture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)            #生成灰度图
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  #生成直方图
    clahe_image = clahe.apply(gray)
    detections = detector(clahe_image, 1)
    for k, d in enumerate(detections):
        shape = predictor(clahe_image, d)  # 获取坐标
        for i in range(1, 68):  # 每张脸都有68个识别点
            cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0, 0, 255),
                       thickness=2)

    cv2.imshow("Camera", frame)

cameraCapture.release()
cv2.destroyAllWindows()