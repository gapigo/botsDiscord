from PIL import Image, ImageOps
size = 2
imagem = Image.open('mono.png')
imagem.show()
im2 = ImageOps.fit(imagem, x)
#imagem.show()
