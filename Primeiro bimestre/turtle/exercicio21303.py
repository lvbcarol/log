# Exercício 02
!pip install ColabTurtlePlus
from ColabTurtlePlus.Turtle import *
# Constantes
LADO = 400            # Lado da "janela" (canvas)
VELOCIDADE = 5        # Escala de 1 a 13

# Criação do canvas
clearscreen()             # Limpa a tela da execução anterior
setup(2*LADO, 2*LADO)     # Tamanho da janela
bgcolor('lightblue')      # Cor de fundo da tela
showborder()              # Mostra a borda

# Criação da tartaruga donatelo
donatelo = Turtle()         # Criação
donatelo.speed(VELOCIDADE)  # Alterando a velocidade

# Movimentação
donatelo.forward(200)       # donatelo.fd(100)
donatelo.right(90)           # donatelo.lt(45)
donatelo.forward(200)
donatelo.left(90)          # donatelo.rt(65)
donatelo.backward(200)      # donatelo.bk(150)
donatelo.right(90)
donatelo.backward(200)
donatelo.forward(100)
donatelo.circle(100)

//aqui apareceria um circulo circunscrito em um quuadrado se rodado no colab do google