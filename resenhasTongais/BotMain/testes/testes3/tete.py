from PIL import Image
Im1 = Image.open('5.png')
Im2 = Image.open('b0.png')
lista = [(8, 20), (266, 20), (524, 20), (782, 20), (1040, 20)]
for i in range(0, 5):
    Im2 = Image.open(f'b{i}.png')
    Im1.paste(Im2, lista[i])
Im1.save('g0.png')