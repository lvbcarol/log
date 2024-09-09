#**Exercício 05 – Soma dos n primeiros inteiros**

#Elabore uma função que recebe um inteiro `n` (positivo) como um parâmetro 
#e retorna a soma de todos os inteiros positivos até `n`. Por exemplo, se `n = 50`, 
#a função deve retornar a soma `1 + 2 + 3 + ⋯ + 48 + 49 + 50`. Use recursão no cálculo da soma.

#soma dos primeiros números inteiros
def soma_todos(n):
    if n==0:
        return 0
    else:
        return n + soma_todos(n - 1)
    
#testes
print("Soma recursiva de todos os os inteiros até n")
print(soma_todos(1))
print(soma_todos(10))
print(soma_todos(50))