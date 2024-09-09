##**Exercício 04**##
#Elaborar um programa Python que permita a leitura de três números reais. Calcule (se possível) e exiba as raízes reais da equação $ax^2+bx+c=0$. O algoritmo 
#deve checar se a entrada de dados de fato representa uma equaçção de segundo grau.
import math
a = float (input ("Digite o primeiro número"))
b = float (input ("Digite o segundo número"))
c = float (input ("Digite o terceior número"))

if a != 0:
    delta = b**2 - 4 * a * c
    if delta > 0:
        raiz1 = (-b + math.sqrt (delta))/ 2 * a 
        raiz2 = (-b - math.sqrt (delta))/ 2 * a
        print (raiz1, raiz2)
    elif delta == 0:
        raiz3 = (-b)/ 2 * a
        print (raiz3)
    else:
        print ("Não há raiz.")

# esse != significa diferente de 