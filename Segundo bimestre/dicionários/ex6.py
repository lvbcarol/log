#6. Escreva um programa para remover duplicatas do dicionário. Como duplicata, entenda duas entradas que possuem valores iguais. 
#(Não pode haver duas chaves iguais no mesmo dicionário.)
#Teste com o dicionário {'a': 12, 'b': 20, 'c': 12, 'd': 40}
dicionario = {'a': 12, 'b': 20, 'c': 12, 'd': 40}
resultado = {}
for key, value in dicionario.items():
    if value not in resultado.values():
        resultado[key] = value
print(resultado)