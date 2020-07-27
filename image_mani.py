from PIL import Image, ImageFilter, ImageEnhance
from sys import argv

filename = argv[1]

im = Image.open(filename)
print(im.size[0])
'''
im_sharp = im.filter(ImageFilter.SHARPEN)
im_sharp.save('sharpend_escher.jpg', 'JPEG')
source = im.split()
'''

#Rotating while fading with changing speed

acc = 0.1
speed = 2.0
images = []
size_c = im.size[0] - im.size[0]/3.0, im.size[1] - im.size[1]/3.0

for i in range(180):	
	out = im.rotate(speed * i)
	enh = ImageEnhance.Contrast(out).enhance(5*i/float(180))
	enh.thumbnail( (im.size[0] - i*size_c[0]/float(180), im.size[1] - i*size_c[1]/float(180))  , Image.ANTIALIAS)
	images.append(enh)
	speed += acc

for i in range(180, 1, -1):
	out = im.rotate(speed * i)
	enh = ImageEnhance.Contrast(out).enhance(5*i/float(180))
	enh.thumbnail( (im.size[0] - i*size_c[0]/float(180), im.size[1] - i*size_c[1]/float(180))  , Image.ANTIALIAS)
	images.append(enh)
	speed -= acc
	out = im.rotate(speed * i)

images[0].save('escher_ani.gif', save_all=True, append_images=images[1:], durations=100, loop=0)

'''
mask = source[0].point(lambda i: i * 2)
out = source[1].point(lambda i: i * 3)
source[1].paste(out, None, mask)
enh.enhance(9).show("30% more")

im = Image.merge(im.mode, source)
'''
