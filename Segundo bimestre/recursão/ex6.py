#**Exercício 06 – Potência recursiva**
#Escreva uma função que recebe dois inteiros `x` e `y`. A função deve usar a recursão para o cálculo de `x` elevado a potência `y`.

def potencia(x,y):
    if y ==0:
        return 1
    elif y == 1:
        return x
    else: 
        return x * potencia(x, y-1)

# Testes
print('-- Potência recursiva --')
print(potencia(3, 0))
print(potencia(4, 1))
print(potencia(3, 4))