#3 - Tabuada de um Número
#Dado um número, use um for loop para gerar a tabuada desse número até um determinado limite.
tabuada = 5
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for n in numeros:
    valor = n * tabuada
    print (valor)

multiplicado = 3
multiplicador = 0
for n in range(10):
    multiplicador += 1
    resultado = multiplicado * multiplicador
    print(multiplicado, "x", multiplicador, "=", resultado)