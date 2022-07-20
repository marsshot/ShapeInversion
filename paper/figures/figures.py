from PIL import Image, ImageDraw, ImageFont
import shutil


import sympy
from sympy.vector import Del
sympy.preview('${.\qquad\mathrm{\kappa/\kappa_{Ref}}\qquad.}$', dvioptions=["-D 180"], viewer='file', filename='png/txt_perm.png', euler=False)
sympy.preview('${.\qquad\mathrm{p/p_{Ref}}\qquad.}$', dvioptions=["-D 150"], viewer='file', filename='png/txt_p.png', euler=False)
sympy.preview('${.\qquad\mathrm{\phi_{\epsilon}}\qquad.}$', dvioptions=["-D 180"], viewer='file', filename='png/txt_phi.png', euler=False)
sympy.preview('${.\qquad\qquad\mathrm{\kappa_{xx}/\kappa_{Ref}}\qquad\qquad.}$', dvioptions=["-D 180"], viewer='file', filename='png/txt_perm_xx.png', euler=False)
sympy.preview('${.\qquad\qquad\mathrm{\kappa_{zz}/\kappa_{Ref}}\qquad\qquad.}$', dvioptions=["-D 180"], viewer='file', filename='png/txt_perm_zz.png', euler=False)


sympy.preview('$.\mathrm{(g/cm^3)}~~~.$', dvioptions=["-D 210"], viewer='file', filename='png/txt_rho.png', euler=False)


def modify_figure(src,dst,label='png/txt_perm.png',x_offset=660,y_offset=180):
	shutil.copyfile(src,dst)
	txt = Image.open(label)
	width, height = txt.size
	txt = txt.crop((5,0,width-5,height))
	txt = txt.rotate(90, expand = 1)
	# scale = 0.3
	# txt = txt.resize( [int(scale * s) for s in txt.size] )
	img = Image.open(dst)
	Image.Image.paste(img, txt, (x_offset, y_offset))
	img.show()
	img.save(dst,dpi=(225,225))



# shutil.copyfile('originals/105.png', "2.png")

# modify_figure("originals/201.png", "png/3a.png", "png/txt_perm.png",x_offset=655)
# modify_figure("originals/202.png", "png/3b.png", "png/txt_p.png")

# modify_figure('originals/203.png', "png/4a.png", "png/txt_perm.png",x_offset=650)
# modify_figure('originals/204.png', "png/4b.png", "png/txt_perm.png",x_offset=650)

# modify_figure('originals/205.png', "png/5a.png", "png/txt_perm.png",x_offset=650)
# modify_figure('originals/206.png', "png/5b.png", "png/txt_phi.png",x_offset=655,y_offset=210)

# shutil.copyfile('originals/207.png', "png/6.png")

# modify_figure('originals/208.png', "png/7a.png", "png/txt_perm_xx.png",x_offset=655,y_offset=100)
# modify_figure('originals/209.png', "png/7b.png", "png/txt_perm_zz.png",x_offset=655,y_offset=100)
# modify_figure('originals/210.png', "png/7c.png", "png/txt_p.png",x_offset=800,y_offset=250)

# modify_figure('originals/211.png', "png/8a.png", "png/txt_perm_xx.png",x_offset=655,y_offset=100)
# modify_figure('originals/212.png', "png/8b.png", "png/txt_perm_zz.png",x_offset=655,y_offset=100)

# modify_figure('originals/213.png', "png/9a.png", "png/txt_perm_xx.png",x_offset=655,y_offset=100)
# modify_figure('originals/214.png', "png/9b.png", "png/txt_perm_zz.png",x_offset=655,y_offset=100)
# modify_figure('originals/215.png', "png/9c.png", "png/txt_phi.png",x_offset=660,y_offset=200)

# shutil.copyfile('originals/216.png', "png/10.png")

# shutil.copyfile('originals/301.png', "png/11a.png")
# shutil.copyfile('originals/302.png', "png/11b.png")
# shutil.copyfile('originals/303.png', "png/11c.png")

# shutil.copyfile('originals/304.png', "png/12a.png")
# shutil.copyfile('originals/305.png', "png/12b.png")
# shutil.copyfile('originals/306.png', "png/12c.png")
# shutil.copyfile('originals/307.png', "png/12d.png")

# shutil.copyfile('originals/401.png', "png/13a.png")
# shutil.copyfile('originals/402.png', "png/13b.png")

# modify_figure('originals/501.png', "png/14a.png", "png/txt_rho.png",x_offset=1390,y_offset=8)
# shutil.copyfile('originals/502.png', "png/14b.png")

# modify_figure('originals/503B.png', "png/15a.png", "png/txt_rho.png",x_offset=1390,y_offset=8)
# modify_figure('originals/506.png', "png/15b.png", "png/txt_rho.png",x_offset=1390,y_offset=8)

# shutil.copyfile('originals/601.png', "png/16a.png")
# modify_figure('originals/602.png', "png/16b.png", "png/txt_rho.png",x_offset=1390,y_offset=8)

# shutil.copyfile('originals/604.png', "png/17a.png")
# shutil.copyfile('originals/605.png', "png/17b.png")
# shutil.copyfile('originals/606.png', "png/17c.png")
# shutil.copyfile('originals/607.png', "png/17d.png")

# shutil.copyfile('edited/701.png', "png/18a.png")
# shutil.copyfile('edited/702.png', "png/18b.png")

# shutil.copyfile('edited/704.png', "png/19a.png")
# shutil.copyfile('edited/705.png', "png/19b.png")

# shutil.copyfile('originals/706.png', "png/20a.png")
# shutil.copyfile('originals/707.png', "png/20b.png")
