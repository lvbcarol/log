#**Exercício 02**
#Elabore um programa modularizado que calcule a soma dos n primeiros quadrados.
#a)** Desenvolva a função `soma_quadrados` que recebe um inteiro n (positivo) como um parâmetro e retorna a soma de todos os quadrados
# até n^2.
#Por exemplo, se n = 5, a função deve retornar a soma 1^2+2^2+3^2+4^2+5^2.
#execute a célula de teste para verificar o funcionamento da função.
#IMPORTANTE:* A função deve, obrigatoriamente, usar recursão no cálculo da soma.

# Função soma_quadrados
def soma_quadrados(n):
  if n == 0:
    return 0
  else:
    return n ** 2 + soma_quadrados(n - 1)
  

#b)** Elabore um programa que peça ao usuário a digitação do inteiro n e use a função do item anterior para determinar
# a soma dos n primeiros quadrados.
#IMPORTANTE:* Faça a validação da informação de entrada! n deve ser inteiro e positivo.

def soma_quadrados(n):
    return sum(i**2 for i in range(1, n+1))

while True:
    try:
        n = int(input("Digite um número inteiro positivo: "))
        if n > 0:
            break
        else:
            print("O número deve ser positivo. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

print(f"A soma dos {n} primeiros quadrados é {soma_quadrados(n)}")
