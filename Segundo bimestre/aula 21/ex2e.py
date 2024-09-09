#e)** Elabore um programa modular que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas.
#Exemplo de uso:
#Nome = Vanessa
#Resultado gerado pelo programa:
#V
#VA
#VAN
#VANE
#VANES
#VANESS
#VANESSA
def imprimir_escada(nome):
    nome = nome.upper()
    for i in range(1, len(nome) + 1 ):
        print(nome[:i])

nome = input("Digite seu nome:")

imprimir_escada(nome)

#texto
#01234
#[0:1] = t
#[1:4] = ext
#[:2] = te