from PIL import Image,ImageFilter,ImageFont,ImageColor,ImageDraw
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("img/pic.jpg")

print(img.size)

print(Image.__version__)

"""加特效"""
""" 
 CONTOUR 轮廓滤波
 """
# img = img.filter(ImageFilter.CONTOUR)
# img.show()
# img.save("img/pic2.jpg")

"""模糊滤波"""
# img = img.filter(ImageFilter.BLUR)
# img.show()

"""自定义模糊程度 radius"""
# img = img.filter(ImageFilter.BoxBlur(radius=10))
# img.show()

"""细节滤波 可以锐化图片"""
# img = img.filter(ImageFilter.DETAIL)
# img.show()

"""细节增强滤波 高清大图"""
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img.show()

"""高斯模糊radius 不用教这个"""
# img = img.filter(ImageFilter.GaussianBlur(radius=2))
# img.show()


# """转成单通道模式"""
# img = img.convert("L")
# img.show()

"""获取通道模式"""
# bands = img.getbands()
# print(bands)
#
# img = img.convert("RGB")
#
# img.show()
#
# print(img.getbands())

"""获取单个像素的颜色值"""
# pixel = img.getpixel((300,670))
# print(pixel)

"""等比缩放"""
# print(img.size)
# w,h = img.size
# img.thumbnail((w//2,h//2))
# img.show()
# print(img.size)
#
"""像素直方图 获取0~255之间的颜色值出现的次数 """
# img = img.convert("L")
#
# his = img.histogram()
# print(his)
# print(len(his))

# img.show()

"""在matplot里显示"""
img = Image.open("img/valicode.jpg")
plt.subplot(2,1,1)
plt.axis("off") # 去掉坐标轴
plt.imshow(img)

plt.subplot(2,1,2)
data = np.array(img)
print(data)
# matplotlib的hist显示直方图
plt.hist(data.flatten(),bins=256,linewidth=10)
plt.show()


"""加水印"""
# logo = Image.open("img/pic1.jpg")
# img.paste(logo,(300,500))
# img.show()

"""抠图"""
# area = img.crop((260,400,400,600))
# area.show()

"""旋转多少度"""
# img = img.rotate(30)
# img.show()


import random

"""生成验证码"""
class ValidataCode:

    font = ImageFont.truetype(font="Avenir Next.ttc",size=36)

    def __init__(self,width,height):
        self.width = width
        self.height = height


    def __gen_code(self):
        return chr(random.randint(65,90)) # A~Z

    def __gen_background(self):
        return (random.randint(90,255),random.randint(90,255),random.randint(90,255))

    def __gen_foreground(self):
        return (random.randint(70, 120), random.randint(70, 120), random.randint(70, 120))

    def __gen_panel(self):
        panel = Image.new("RGB", (self.width, self.height), (255, 255, 255))
        return panel


    def drawcode(self):
        # 获取画板
        panel = self.__gen_panel();
        # 用imageDraw在画板上画东西
        drawObj = ImageDraw.Draw(panel)
        # 先画背景色（画每个像素点）
        for y in range(self.height):
            for x in range(self.width):
                drawObj.point((x,y),fill=self.__gen_background())

        # 再画随机字母
        for i in range(4):
            drawObj.text((65*i+10,10),self.__gen_code(),fill=self.__gen_foreground(),font=self.font)
        panel.show()
        panel.save("img/valicode.jpg")


if __name__ == '__main__':

    # gen = ValidataCode(240,60)
    # gen.drawcode()
    pass



print(np.__version__)