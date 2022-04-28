from PIL import Image,ImageDraw

im = Image.open('dogTest.png')
pix = im.load()
print(im.size) # Get the width and hight of the image

x=im.size[0]
y=im.size[1]
print(x)
print(y)
imgList = []
for p in range(1,x):
    for q in range(1,y):
        imgList.append(pix[p,q])
im.save('dogTest.png', quality=100)
print(pix[x-1,y-1])
canvas = Image.new('RGB', (x, y), 'white')
img_draw = ImageDraw.Draw(canvas)
imgListLen = len(imgList)
print(imgListLen)
print(x*y)
t = 1
try:
    for i in range(x-1):
        for o in range(y-1):
            if t<imgListLen:
                img_draw.point((i, o), fill=imgList[t])
                t += 1
    print('i=',i)
    print('o=',o)
except:
    print('t=',t)
print(canvas.size)
canvas.save('drawn_image.png', quality = 100)