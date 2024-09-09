#4. Crie uma função que multiplica todas os valores de um dicionário por 5. Considere o dicionário {'e1': 10, 'e2': 20, 'e3': 6}

dicionario = {'e1': 10, 'e2': 20, 'e3': 6}
#só colocar "" quando for string, pq sn ele não consegue entender que o valor é numérico
for key, value in dicionario.items():
        dicionario[key] = value * 5
        #por exemplo: key: e1; value: 10
print(dicionario) 