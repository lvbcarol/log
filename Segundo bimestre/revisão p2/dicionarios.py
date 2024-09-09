dicionario = {
    "Iguatemi" : "Iguatemi@gmail",
    "Plaza" : "plaza@gmail",
    "Barra" : "barra@gmail"
}

#pegar o email do shopping iguatemi
email_escolhido = dicionario["Iguatemi"]
print(email_escolhido)

#adicoinar um novo shopping
dicionario["leblon"] = "leblon@gmail"
print(dicionario)

#pegar todos os shoppings
#print
print(dicionario.keys())

#for
for i in (dicionario):
    print(i)

#pegar todos o e-mails
print(dicionario.values())

for i in (dicionario):
    emails = dicionario[i]
    print(emails)

#Retirar um shopping
#dicionario.pop("leblon")
#print(dicionario)

del dicionario["leblon"]
print(dicionario)

#Verificar se existe
if ("leblon") in dicionario:
    print("Existe")
else:
    print("não existe")
