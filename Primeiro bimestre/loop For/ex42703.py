#4- Soma dos Números Pares em um Intervalo
#Dado um intervalo de números, use um for loop para calcular a soma dos números pares dentro desse intervalo.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = []
total = 0
for i in numeros:
    if i % 2 == 0:
        print(lista_pares)
        lista_pares.append(i)
        total += i
print("numeros pares:", lista_pares, "total:", total)