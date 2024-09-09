def soma_lista_it(lista):
    soma = 0
    for i in lista:
        soma = soma +1
    return soma

def soma_lista_rec(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista_rec(lista[1:])