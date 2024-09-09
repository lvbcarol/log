#**Exercício 04 – Soma recursiva dos elementos de uma lista**
#Construa uma função que recebe uma lista de números e retorna a soma dos elementos da lista, calculada recursivamente.
# Soma dos elementos de uma lista

def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])
    
def soma_lista2(lista):
    return 0 if len(lista) == 0 else lista[0] + soma_lista(lista[1:])

# Testes
print('-- Soma recursiva de elementos em uma lista --')
print(soma_lista([]))
print(soma_lista([2]))
print(soma_lista([-5, 0, 4, 6]))
print(soma_lista2([]))
print(soma_lista2([2]))
print(soma_lista2([-5, 0, 4, 6]))