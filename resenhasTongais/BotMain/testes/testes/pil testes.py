from PIL import Image, ImageOps
im = Image.open('MONOPOLY.png')
im2 = im.crop((0, 1304,  194, 1498))
im2.show()

'''
im = Image.open('MONOPOLY.png')
virar90 = Image.ROTATE_90
virar270 = Image.ROTATE_270
proporção = 5

lista2 = [
            20,   0,  0, 195, 195,
            21, 194,  0, 316, 197,
            22, 316,  0, 438, 197,
            23, 438,  0, 562, 197,
            24, 562,  0, 685, 197,
            25, 685,  0, 808, 197,
            26, 808,  0, 931, 197,
            27, 931,  0, 1054, 197,
            28, 1054, 0, 1177, 197,
            29, 1177, 0, 1300, 197,
            30, 1300, 0, 1500, 197,
        ]
for i in range(0, 40):
    if i in range(20, 31):
        im2 = im
        im3 = im2.crop((lista2[1],lista2[2],lista2[3],lista2[4]))
        print('image cropped')
        del lista2[0:5]
    else:
        if i in range(0, 11):
            im2 = im
        elif i in range(11, 20):
            im2 = im.transpose(virar90)
        elif i in range(31, 40):
            im2 = im.transpose(virar270)
        lista = [0, 1300, 1304, 1500, 1500,
                 1, 1178, 1304, 1300, 1498,
                 2, 1054, 1305, 1177, 1498,
                 3, 931, 1304, 1054, 1498,
                 4, 809, 1304, 931, 1498,
                 5, 685, 1304, 809, 1498,
                 6, 562, 1304, 685, 1498,
                 7, 439, 1304, 562, 1498,
                 8, 317, 1304, 439, 1498,
                 9, 194, 1304, 317, 1498,
                 10,    0, 1304,  194, 1498]
        for j in range(0, len(lista)):
            if i == lista[j]:
                im3 = im2.crop((lista[j+1],lista[j+2],lista[j+3],lista[j+4]))
                print('image cropped')
                break
            elif ((i - 10) == lista[j]) or ((i - 30) == lista[j]):
                im3 = im2.crop((lista[j + 1], lista[j + 2], lista[j + 3], lista[j + 4]))
                print('image cropped')
                break

    x = im3.size
    print('image sized')
    y = x[1]
    x = x[0]
    x = (x * proporção, y * proporção)
    im3 = ImageOps.fit(im3, x)
    im3.save(f'{i}.png')
    print('image saved')
'''
'''
im2 = im.crop((1300, 1304, 1500, 1500))
x = im2.size
lista = []
proporção = 10
lista.append(x[0]*proporção)
lista.append(x[1]*proporção)
x = (lista[0], lista[1])
im2 = ImageOps.fit(im2, x)
im2.save('mono.png')
virar90 = Image.ROTATE_90
virar270 = Image.ROTATE_270
im3 = im.transpose(virar90)
im3.save('90.png')
im4 = im.transpose(virar270)
im4.save('270.png')
print(x)'''
