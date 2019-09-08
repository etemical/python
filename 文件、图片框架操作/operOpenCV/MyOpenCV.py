import cv2
"""普通加载图像"""
# img = cv2.imread("img/pic.jpg")
# cv2.imshow("image", img)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()


"""灰度操作"""
img = cv2.imread("img/pic.jpg")
# img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

"""画一条线"""

green = (0,255,0)
# cv2.line(img,(0,0),(300,300),green,5)
# cv2.imshow("image",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


"""画矩形"""
cv2.rectangle(img,(280,380),(420,530),green,3)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
