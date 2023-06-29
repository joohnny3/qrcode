from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer, RoundedModuleDrawer, HorizontalBarsDrawer, SquareModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer
from qrcode.image.styledpil import StyledPilImage
import qrcode


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data('''
BEGIN:VCARD
FN:CHANG Yu-cheng
TEL;CELL:0929312288
EMAIL:johnny31258@gmail.com
URL:https://github.com/joohnny3
END:VCARD
''')
qr.make(fit=True)


img1 = qr.make_image(image_factory=StyledPilImage,
                     module_drawer=SquareModuleDrawer(),
                     color_mask=RadialGradiantColorMask((255,255,255),(0,255,255),(0,0,255)))
img2 = qr.make_image(image_factory=StyledPilImage,
                     module_drawer=GappedSquareModuleDrawer(),color_mask=RadialGradiantColorMask())
img3 = qr.make_image(image_factory=StyledPilImage,
                     module_drawer=CircleModuleDrawer(),color_mask=RadialGradiantColorMask((255,255,255),(255,0,0),(0,0,255)))
img4 = qr.make_image(image_factory=StyledPilImage,
                     module_drawer=RoundedModuleDrawer(),color_mask=RadialGradiantColorMask((255,255,255),(255,255,0),(0,0,255)))
img5 = qr.make_image(image_factory=StyledPilImage,
                     module_drawer=VerticalBarsDrawer(),color_mask=RadialGradiantColorMask((255,255,255),(255,0,255),(0,0,255)))
img6 = qr.make_image(image_factory=StyledPilImage,
                     module_drawer=HorizontalBarsDrawer(),
                     color_mask=RadialGradiantColorMask((255,255,255),(0,255,0),(0,0,255)))
img1.save('qrcode1.png')
img2.save('qrcode2.png')
img3.save('qrcode3.png')
img4.save('qrcode4.png')
img5.save('qrcode5.png')
img6.save('qrcode6.png')
