# Exercício 5
from ColabTurtlePlus.Turtle import *

# Constantes
LADO = 150            # Lado da "janela" (canvas)
VELOCIDADE = 7        # Escala de 1 a 13

# Criação do canvas
clearscreen()             # Limpa a tela da execução anterior
setup(2*LADO, 2*LADO)     # Tamanho da janela
bgcolor('lightgray')      # Cor de fundo da tela
showborder()              # Mostra a borda

# Criação da tartaruga donatelo
donatelo = Turtle()         # Criação
donatelo.speed(VELOCIDADE)  # Alterando a velocidade

##### INSIRA O SEU CÓDIGO #####
donatelo.left(45)
donatelo.forward(100)       # donatelo.fd(100)
donatelo.right(90)           # donatelo.lt(45)
donatelo.forward(100)
donatelo.left(45)          # donatelo.rt(65)
donatelo.backward(140) 