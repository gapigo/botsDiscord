from PIL import Image

im1 = Image.open('as1.png')  # branco
im2 = Image.open('as2.png')  # preto
mask = Image.open('bla.png').convert('1')
im3 = Image.composite(im1, im2, mask)  # a primeira imagem vai no branco, a segunda imagem vai no preto
im3.save('mascarado.png')

"""
jogadores = ['verde', 'amarelo', 'azul', 'vermelho']

for jogador in jogadores:
    if jogador == 'verde':
        pattern = 'verde'
    elif jogador == 'amarelo':
        pattern = 'amarelo'
    elif jogador == 'azul':
        pattern = 'azul'
    elif jogador == 'vermelho':
        pattern = 'vermelho'

    mask = Image.open(f'./{pattern}/{pattern} 0.png').convert("1")

    im4 = Image.composite(im2, im1, mask)
    im4.save(f'{pattern}.png')
"""

