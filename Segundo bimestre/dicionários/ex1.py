#1. Execute as seguintes tarefas:

#a. Crie um dicionário chamado carro com as seguintes chaves e valores: marca (valor "Ford"), modelo
# (valor "Mustang"), e ano (valor 1964). Depois, imprima o valor associado à chave modelo;
carro = {"marca": "ford", "modelo":"mustang", "ano": "1964"}
print(carro["modelo"])

#b. Dado o dicionário carro do exercício anterior, adicione uma nova chave cor com o valor "vermelho"
# e mude o ano para 2020. Imprima o dicionário modificado;
carro = {"marca": "ford", "modelo":"mustang", "ano": "2020", "cor" : "vermelho"}
print(carro)

#c. Remova a chave modelo do dicionário carro e imprima o dicionário após a remoção;
carro = {"marca": "ford","ano": "2020", "cor" : "vermelho"}
print(carro)

#d. Usando o dicionário carro, escreva um loop que imprima todas as suas chaves e valores no formato "Chave: Valor".
for chave, valor in carro.items():
    print(f"chave: {chave}, valor: {valor}")