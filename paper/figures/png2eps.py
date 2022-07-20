from PIL import Image, ImageDraw, ImageFont
import os

src_dir='png/'
dst_dir='eps/'

def remove_transparency(im, bg_color=(255, 255, 255)):
	if im.mode in ('RGBA') or (im.mode == 'P' and 'transparency' in im.info):
		alpha = im.convert('RGBA').split()[-1]
		bg = Image.new("RGBA", im.size, bg_color+(255,))
		bg.paste(im, mask=alpha)
		return bg
	else:
		return im


def png2eps(src,dst):
	img = Image.open(src)
	if img.mode == 'RGBA':
		img = remove_transparency(img)
		img = img.convert('RGB')
	img.save(dst,dpi=(300,300))
	img.close()

files = os.listdir(src_dir)
 
for png in files:
	if png.endswith(".png"):
		eps = png.replace('.png','.eps')
		if not os.path.exists(dst_dir+eps):
			print("conveting {} to {}!".format(png,eps))
			png2eps(src_dir+png,dst_dir+eps)
