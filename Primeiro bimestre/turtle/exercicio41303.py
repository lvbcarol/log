# Exercício 04
# !pip install ColabTurtlePlus
from turtle import *# Constantes
LADO = 300            # Lado da "janela" (canvas)
VELOCIDADE = 6       # Escala de 1 a 13

# Criação do canvas
clearscreen()             # Limpa a tela da execução anterior
setup(2*LADO, 2*LADO)     # Tamanho da janela
bgcolor('lightblue')      # Cor de fundo da tela
#showborder()              # Mostra a borda

# Criação da tartaruga donatelo
donatelo = Turtle()         # Criação
donatelo.speed(VELOCIDADE)  # Alterando a velocidade

# Movimentação       # donatelo.fd(100)
donatelo.right(135)           # donatelo.lt(45)
donatelo.forward(17500 ** (1/2))
donatelo.right(165)          # donatelo.rt(65)
donatelo.forward(200)      # donatelo.bk(150)
donatelo.right(120)
donatelo.forward(200)
donatelo.right(165)
donatelo.forward(17500 ** (1/2))
done()


