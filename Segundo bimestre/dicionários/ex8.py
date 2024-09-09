#8. Escreva um script para imprimir um dicionário onde as chaves são números entre 1 e 15
#(ambos incluídos) e os valores são o quadrado das chaves.

dicionario = {}
for i in range(1, 16):
    dicionario[i] = i ** 2
print(dicionario)