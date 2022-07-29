from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

src_dir='eps/'
dst_dir='png-grayscale/'
convertGray = True

black = (0,0,0)
white = (255,255,255)
color_threshold = 150
offset = 10

def rgb2gray(img):
	return ImageOps.grayscale(img)
	data = img.getdata()
	new_data = []
	for item in data:
		r,g,b = item[0], item[1], item[2]
		if r<10 and g<10 and b<10:
			new_data.append(item)
		elif r>220 and g>220 and b>220:
			new_data.append(item)
		elif r<100 and r==g and b==g:
			new_data.append(item)
		elif r>color_threshold and r>g-offset and r>b-offset:
			new_data.append(white)
		elif g>color_threshold and g>r-offset and g>b-offset:
			new_data.append(white)
		elif b>color_threshold and b>r-offset and b>g-offset:
			new_data.append(white)
		else:
			new_data.append(item)
	img.putdata(new_data)
	return img

def eps2png(src,dst):
	img = Image.open(src)
	if convertGray:
		img = rgb2gray(img)
	img.save(dst,dpi=(600,600))
	img.save(dst)
	img.close()

files = os.listdir(src_dir)
 
for eps in files:
	if eps.endswith(".eps"):
		png = eps.replace('.eps','.png')
		if not os.path.exists(dst_dir+png):
			print("conveting {} to {}!".format(eps,png))
			eps2png(src_dir+eps,dst_dir+png)


