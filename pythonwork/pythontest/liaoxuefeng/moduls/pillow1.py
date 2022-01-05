print('--------------image 缩放尺寸')
from PIL import Image

im=Image.open(r'd:\2.jpg')
w,h=im.size
print('image size:%sx%s' % (w,h))

im.thumbnail((w//2,h//2))
print('resize image to :  %sx%s' % (w//2,h//2))
im.save('d:\\1.jpg','jpeg')


print('----------------image 模糊')
from PIL import Image,ImageFilter
im=Image.open('d:\\1.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.save('d:\\1-1.jpg','jpeg')

print('---------------生成字母验证码')
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#随机字母
def rndChar():
    return chr(random.randint(65,90))

#随机颜色1
def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

#随机颜色2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

#240x60
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#创建font对象
font=ImageFont.truetype('D:\\arial.ttf',35)
#创建Draw对象
draw=ImageDraw.Draw(image)
#填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())

#输出文字
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#模糊
image=image.filter(ImageFilter.BLUR)
image.save('D:\\code.jpg','jpeg')












