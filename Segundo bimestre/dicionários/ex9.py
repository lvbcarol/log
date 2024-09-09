#9. Dado um dicionário onde as chaves são números inteiros, escreva um código que remova todas as chaves que são múltiplos de 3.
# Imprima o dicionário resultante.
dicionario = {1 : "a", 2 : "b", 3 : "c", 4 : "d"}
resultado = {}
for key, value in dicionario.items():
    if key % 3 != 0:
      resultado[key] = value
print(resultado)