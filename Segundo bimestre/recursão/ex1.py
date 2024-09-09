#**Exercício 01 – Multiplicação Recursiva**

#Elabore uma função recursiva que recebe dois parâmetros `x` e `y` (assuma valores maiores ou iguais a zero).
# A função deve retornar o valor de `x` multiplicado por `y`.
#Lembre-se que a multiplicação pode ser realizada por meio de adições sequenciais.
#veja um exemplo:
#`7 × 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4`

def mult_rec(x,y):
    if x == 0 or y == 0:
        return 0
    return y + mult_rec(x-1, y)

#testes
print("Multiplicação recursiva")
print(mult_rec(4,6))
print(mult_rec(5,1))
print(mult_rec(0,456))