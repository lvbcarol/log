#inicialize uma lista com 20 números inteiros entre 0 e 200 e a imprima. Armazene os números pares em uma lista
#`pares` e os números ímpares em uma lista `impares`. Organize os valores das listas em ordem crescente e as imprima.
from random import choices

#sorteio dos 20 numeros inteiros entre 0 e 20
numeros = list(range(201))
sorteio = choices(numeros, k=20)
print(f"Lista sorteada:\n{sorteio}")

#criação das listas pares e ímpares
pares = sorted([numero for numero in sorteio if numero % 2 == 0], reverse = False)
impares = sorted([numero for numero in sorteio if numero % 2 == 1])

#impressao de listas
print(f"Lista com números pares:\n{pares}")
print(f"Lista com números impares:\n{impares}")

#o que seria esse list
#como usar choices
#como usar sorted
#como usar reverse
