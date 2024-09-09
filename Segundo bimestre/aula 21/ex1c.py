#*c)** Escreva um programa que leia vários números reais em uma mesma linha, e imprima a soma.
num = input("Digite uam sequência de números separados por espaço.")
lista_num = num.split()
numeros = [float (numero) for numero in lista_num]
soma = sum(numeros)
print(soma)