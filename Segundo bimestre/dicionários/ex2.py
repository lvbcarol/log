#2. Armazena todas as chaves de um dicionário em uma lista.
#Considere o dicionário {'a': 10, 'b': 7, 'c': 'vazio'}
lista = []
d = {"a" : "10", "b" : "7", "c" : "vazio"}
for k in d.keys():
    lista.append(k)
print(lista)