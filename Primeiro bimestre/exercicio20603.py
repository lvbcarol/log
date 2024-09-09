##**Exercício 02**##
#Elaborar um programa Python que permita a leitura de dois números inteiros e exiba a soma deles apenas se o segundo número for um múltiplo de 3.
numeroA = int (input("Digite o primeiro número:"))
numeroB = int (input("Digite o segundo número:"))
if numeroB % 3 == 0:
   print (numeroA + numeroB)