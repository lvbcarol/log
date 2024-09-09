#10. Em um dicionário, todos os valores são listas, que contém vários números. Escreva um programa capaz de contar o número total de itens que aparecem dentro das listas.
#Entrada:  {'M1' : [67,79,90,73,36], 'M2': [89,67,84], 'M3': [82,57] }
#Saída: 10

dicionario =  {'M1' : [67,79,90,73,36], 'M2': [89,67,84], 'M3': [82,57] }

total = 0

for value in dicionario.values():
    total += len(value)
    #esse len é de lenght comprimento

print(f"Total de itens em listas: {total}")