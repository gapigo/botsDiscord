from PIL import Image, ImageMath, ImageOps, ImageChops
im1 = Image.open('lena.jpg')
im2 = Image.open('rocket_resize.jpg')
im3 = Image.open('mask_circle.jpg')

out = ImageChops.composite(im1, im2, im3)
out.save("result.png")
