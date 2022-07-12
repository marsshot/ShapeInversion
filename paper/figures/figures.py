from PIL import Image, ImageDraw, ImageFont
import shutil


import sympy
from sympy.vector import Del
sympy.preview('${.\qquad\mathrm{\kappa/\kappa_{Ref}}\qquad.}$', dvioptions=["-D 180"], viewer='file', filename='txt_perm.png', euler=False)
sympy.preview('${.\qquad\mathrm{p/p_{Ref}}\qquad.}$', dvioptions=["-D 150"], viewer='file', filename='txt_p.png', euler=False)
sympy.preview('${.\qquad\mathrm{\phi_{\epsilon}}\qquad.}$', dvioptions=["-D 180"], viewer='file', filename='txt_phi.png', euler=False)
sympy.preview('${.\qquad\qquad\mathrm{\kappa_{xx}/\kappa_{Ref}}\qquad\qquad.}$', dvioptions=["-D 180"], viewer='file', filename='txt_perm_xx.png', euler=False)
sympy.preview('${.\qquad\qquad\mathrm{\kappa_{zz}/\kappa_{Ref}}\qquad\qquad.}$', dvioptions=["-D 180"], viewer='file', filename='txt_perm_zz.png', euler=False)


sympy.preview('$.\mathrm{(g/cm^3)}~~~.$', dvioptions=["-D 210"], viewer='file', filename='txt_rho.png', euler=False)


def modify_figure(src,dst,label='txt_perm.png',x_offset=660,y_offset=180):
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

# modify_figure("originals/201.png", "3a.png", "txt_perm.png",x_offset=655)
# modify_figure("originals/202.png", "3b.png", "txt_p.png")

# modify_figure('originals/203.png', "4a.png", "txt_perm.png",x_offset=650)
# modify_figure('originals/204.png', "4b.png", "txt_perm.png",x_offset=650)

# modify_figure('originals/205.png', "5a.png", "txt_perm.png",x_offset=650)
# modify_figure('originals/206.png', "5b.png", "txt_phi.png",x_offset=655,y_offset=210)

# shutil.copyfile('originals/207.png', "6.png")

# modify_figure('originals/208.png', "7a.png", "txt_perm_xx.png",x_offset=655,y_offset=100)
# modify_figure('originals/209.png', "7b.png", "txt_perm_zz.png",x_offset=655,y_offset=100)
# modify_figure('originals/210.png', "7c.png", "txt_p.png",x_offset=800,y_offset=250)

# modify_figure('originals/211.png', "8a.png", "txt_perm_xx.png",x_offset=655,y_offset=100)
# modify_figure('originals/212.png', "8b.png", "txt_perm_zz.png",x_offset=655,y_offset=100)

# modify_figure('originals/213.png', "9a.png", "txt_perm_xx.png",x_offset=655,y_offset=100)
# modify_figure('originals/214.png', "9b.png", "txt_perm_zz.png",x_offset=655,y_offset=100)
# modify_figure('originals/215.png', "9c.png", "txt_phi.png",x_offset=660,y_offset=200)

# shutil.copyfile('originals/216.png', "10.png")

# shutil.copyfile('originals/301.png', "11a.png")
# shutil.copyfile('originals/302.png', "11b.png")
# shutil.copyfile('originals/303.png', "11c.png")

# shutil.copyfile('originals/304.png', "12a.png")
# shutil.copyfile('originals/305.png', "12b.png")
# shutil.copyfile('originals/306.png', "12c.png")
# shutil.copyfile('originals/307.png', "12d.png")

# shutil.copyfile('originals/401.png', "13a.png")
# shutil.copyfile('originals/402.png', "13b.png")

# modify_figure('originals/501.png', "14a.png", "txt_rho.png",x_offset=1390,y_offset=8)
# shutil.copyfile('originals/502.png', "14b.png")

# modify_figure('originals/503B.png', "15a.png", "txt_rho.png",x_offset=1390,y_offset=8)
# modify_figure('originals/506.png', "15b.png", "txt_rho.png",x_offset=1390,y_offset=8)

# shutil.copyfile('originals/601.png', "16a.png")
# modify_figure('originals/602.png', "16b.png", "txt_rho.png",x_offset=1390,y_offset=8)

# shutil.copyfile('originals/604.png', "17a.png")
# shutil.copyfile('originals/605.png', "17b.png")
# shutil.copyfile('originals/606.png', "17c.png")
# shutil.copyfile('originals/607.png', "17d.png")

# shutil.copyfile('edited/701.png', "18a.png")
# shutil.copyfile('edited/702.png', "18b.png")

# shutil.copyfile('edited/704.png', "19a.png")
# shutil.copyfile('edited/705.png', "19b.png")

# shutil.copyfile('originals/706.png', "20a.png")
# shutil.copyfile('originals/707.png', "20b.png")