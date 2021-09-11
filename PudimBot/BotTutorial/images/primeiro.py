from PIL import Image, ImageEnhance, ImageFilter
import os
# img1 = Image.open('imagem.jpg')
# img1.save('imagem.pdf')
# img1.show()
# MAX_SIZE = (250, 250)
# img1.thumbnail(MAX_SIZE)
# img1.save('smallimagem.jpg')

#for item in os.listdir():
#    if item.endswith('.jpg'):
#        img1 = Image.open(item)
#        filename, extension = os.path.splitext(item)
#        img1.save(f'{filename}.png')

# img1 = Image.open('jacaré.jpg')
# enhancer = ImageEnhance.Sharpness(img1)
# enhancer.enhance(2).save('jacaréEditado.jpg')

# 0 : blurry
# 1 : original image
# 2: image with increased sharpness

# --------- color ---------
# img = Image.open('jacaré.jpg')
# enhancer = ImageEnhance.Color(img)
# enhancer.enhance(0).save('jacaréCor.jpg')

# ---------- brightness -------------
# img = Image.open('jacaré.jpg')
# enhancer = ImageEnhance.Brightness(img)
# enhancer.enhance(2).save('jacaréBrilhoso.jpg')
# 1 = 100% | 0.5 = 50%

# img = Image.open('jacaré.jpg')
# enhancer = ImageEnhance.Contrast(img)
# enhancer.enhance(2).save('jacaréContrastoso.jpg')

# image blur

# img1 = Image.open('jacaré.jpg')
# img1.filter(ImageFilter.GaussianBlur(radius=2)).save('JacaréGaussian.jpg')
