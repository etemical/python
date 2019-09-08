from PIL import Image, ImageFilter,ImageFont ,ImageDraw
import matplotlib.pyplot as plt
import numpy as np

img = Image.open("../img/pic.jpg")
a = np.array(img)
a = a.transpose(0,1,2)
print(a.shape)
print(a)
# img = img.rotate(360)
# img.show()
# plt.imshow(a)
# plt.show()
# img = Image.fromarray(a)
# img.show()
# # img.show()
# print(img.size)
def gen_pics():
    image_size = [512, 256, 144, 140, 128, 120, 108, 100, 88, 72, 48, 32, 28]
    _img = Image.open("../img/pic1.jpg")
    j = 1
    for i in (image_size):
        _img.resize((i,i),Image.ANTIALIAS).save("img/"+str(j)+"_"+str(i)+".jpg")
        j+=1
# gen_pics()


# logo = Image.open("validatecode2.jpg")
# img3 = img.copy()
# img3.show()

# img.show()
# print(img.size)  # width,height
#
# # 滤波器 （轮廓滤波） 手绘效果
# img = img.filter(ImageFilter.CONTOUR)
# img.show()
# img.save("../img/pic5.jpg")

# img = img.filter(ImageFilter.BLUR)
# img.show()

# 深度模糊 自定义模糊
# img = img.filter(ImageFilter.BoxBlur(radius=2))
# img.show()

#
# img = img.filter(ImageFilter.DETAIL)
# img.show()
# 深度清晰 高清大图
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img.show()

# 浮雕效果
# img = img.filter(ImageFilter.EMBOSS)
# img.show()

""" 转换通道"""
# print(list(img.getdata()))
# print(img.getbands())
# img = img.convert("L")
# # img.show()
# print(img)
# print(len(list(img.getdata())))
# print(img.getbands())
# img = img.convert("RGB")
# print(img.getbands())
# img.show()


# pixel = img.getpixel((300,600))
# print(pixel)


"""缩放"""

# width ,height = img.size
# print(width,height)
# img.thumbnail((width//2,height//2))
# print(img.size)
# img.show()

"""取出每个通道图像显示"""
# img.split()[0].show()

"""像素直方图"""
# his = img.histogram()
# print(his,"\n",len(his))

"""matplotlib显示"""
# img = img.split()[2]
# img = img.convert("L")
data= plt.imread("validatecode2.jpg")
# Image.fromarray(data).show()
print(data.shape)

print(data[0:,0:,1])
plt.subplot(2,1,1)
plt.imshow(data)
plt.axis("off")
plt.subplot(2,1,2)
# plt.plot(list(range(256)),img.histogram())
# plt.hist(data[0:,0:,0].flatten(),bins=256,color="r")
plt.hist(data[0:,0:,2].flatten(),bins=256,linewidth=5)
# plt.hist(data[0:,0:,2].flatten(),bins=256,color="b")
# plt.show()

"""粘贴图片"""
# img = Image.open("../img/pic.jpg")
# logo = Image.open("../img/pic1.jpg")
#
# img.paste(logo,(0,0))
# print("===========================================")
# print(np.array(img))
# # img.show()
#
# img2 = img.copy()
#
# img2.show()
#
#
# temp = img.crop((300,400,400,500))
# temp.show()
#
# img.rotate(30).show()

def getBoxArea():
    img = Image.open("../img/pic.jpg")
    x , y = img.size
    ax,ay = [],[]
    for _y in range(y):
        for _x in range(x):
            if img.getpixel((_x,_y)) < (253,253,253):
                ax.append(_x)
                ay.append(_y)
    # print(ax,ay)
    # print(max(ax),min(ax))
    # print(max(ay),min(ay))
    x1,y1=min(ax),min(ay)
    x2,y2=max(ax),max(ay)
    draw = ImageDraw.Draw(img)
    draw.rectangle((x1,y1-5,x2,y2),fill=None, width=5, outline=(0,255,0))
    img.show()
    img.save("img/rectangle.jpg")

# getBoxArea()

import random
width ,height = 60,240
def randcode():
    return chr(random.randint(65,90))

def backgourndColor():
    return (random.randint(100,170),random.randint(100,170),random.randint(100,170))

def foregroundColor():
    return (random.randint(60,120),random.randint(60,120),random.randint(60,120))

def getPanel():
    return Image.new("RGB",(width,height),(255,255,255))


def genValidateCode():
    font = ImageFont.truetype("Avenir Next.ttc",size=36)
    panel = getPanel()
    draw = ImageDraw.Draw(panel)
    for h in range(height):
        for w in range(width):
            draw.point((w,h),fill=backgourndColor())

    for i in range(4):
        # draw.text((i*60+15,10),randcode(),fill=foregroundColor(),font=font)
        draw.text((10,i * 60 + 15), randcode(), fill=foregroundColor(), font=font)

    panel.show()
    # panel.save("validatecode2.jpg")


# genValidateCode()



