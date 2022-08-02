from PIL import Image, ImageDraw, ImageFont, ImageOps
import os
import math

src_dir='eps/'
dst_dir='png-grayscale/'
convertGray = True

black = (0,0,0)
white = (255,255,255)
color_threshold = 150
offset = 10

def getRGBRange(img):
	rgb_min, rgb_max = [255,255,255], [0,0,0]
	data = img.getdata()
	for item in data:
		r,g,b = item[0], item[1], item[2]
		if r<10 and g<10 and b<10: continue
		elif r>220 and g>220 and b>220: continue
		elif r==b and g==b: continue
		else:
			rgb_min[0] = min(rgb_min[0],r)
			rgb_min[1] = min(rgb_min[1],g)
			rgb_min[2] = min(rgb_min[2],b)
			rgb_max[0] = max(rgb_max[0],r)
			rgb_max[1] = max(rgb_max[1],g)
			rgb_max[2] = max(rgb_max[2],b)

	return rgb_min, rgb_max

def rgb2gray(img,offset_r=0,offset_b=0):
	# return ImageOps.grayscale(img)
	data = img.getdata()
	# rgb_min, rgb_max = getRGBRange(img)
	new_data = []
	for item in data:
		r,g,b = item[0], item[1], item[2]
		if r<10 and g<10 and b<10:
			new_data.append(item)
		elif r>230 and g>230 and b>230:
			new_data.append(item)
		elif r==b and g==b:
			new_data.append(item)
		elif r>=b:
			v = math.floor(255-0.5*g+offset_r)
			new_data.append((v,v,v))
		else:
			v = math.floor(0.5*g+offset_b)
			new_data.append((v,v,v))

	img.putdata(new_data)
	return img

def eps2png(src,dst,offset_r=0,offset_b=0):
	img = Image.open(src)
	if convertGray:
		img = rgb2gray(img,offset_r,offset_b)
	img.save(dst,dpi=(600,600))
	img.save(dst)
	img.close()

files = os.listdir(src_dir)
 
for eps in files:
	if eps.endswith(".eps"):
		png = eps.replace('.eps','.png')
		#if not os.path.exists(dst_dir+png):
		print("conveting {} to {}!".format(eps,png))
		offset_r, offset_b = 0, 0
		if "20a" in png or "20b" in png:
			offset_r, offset_b = -50, 100
		elif "17" in png:
			offset_r, offset_b = -0, 0
		elif "10" in png:
			offset_r, offset_b = -20, 0
		eps2png(src_dir+eps,dst_dir+png,offset_r=offset_r,offset_b=offset_b)


