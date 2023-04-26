# Image Optimizing
# pip install Pillow
import PIL
from PIL import Image

image = Image.open('Image1.jpg')
# image.show()
# RGB 代表彩色图像，L 代表光照图像也即灰度图像等
print(image.mode, image.size, image.format)
#转换图片模式
image2 = image.convert('L')
# image2.show()
image2.save('Image2.jpg')
#裁剪crop，box内为裁剪后的图片四角在原图片的坐标（左上角 X 坐标、Y 坐标，右下角 X 坐标、Y 坐标）
#
box = (100, 100, 300, 300)
image3 = image.crop(box)
#Image.FLIP_TOP_BOTTOM上下翻转,Image.FLIP_LEFT_RIGHT左右翻转，rotate逆时针旋转
image3 = image3.transpose(Image.ROTATE_180)
image.paste(image3, box)
out = image.point(lambda i: i * 1.2) # 对每个像素值乘以 1.2
source = image.split()#Image.split()方法用于将图像分成单独的波段。此方法从图像返回单个图像带的元组。
out = source[0].point(lambda i: i > 128 and 255) # 对 R 通道进行二值化
out.show()