#Acumular um único valor resultante de uma série de outros valores é uma operação muito comum na Computação.
#Elabore um programa em Python que acumula a soma de uma sequência de números inteiros com início em um limite
#inferior e término em um limite superior, ambos fornecidos pelo usuário. O programa deve exibir também a 
#sequência de números no formato de uma lista.
#IMPORTANTE:* O código deve validar os dados de entrada. Assim, tenha atenção ao tipo dos dados e à ordem dos valores digitados.

from time import time
inicio = time()
print(inicio)
verificacao = False
while not verificacao:
    try:
        if min and max > 0:
            min = int(input("Qual o número mínimo?"))
            max = int(input("Qual o número máximo?")) 
            lista = []
            for i in range(min, max):
                if i < max:
                    i += 1
                    lista.append(i)
            soma = sum(lista)
            print(lista)
            print("Soma dos números foi", soma)
            verificacao = True
            break
        else:
            print("número positivo!")
    except:
        print("Número inteiro!") 
    finally:
        fim = time()
        print(fim)
        tempo = fim - inicio
        print(f"O tempo de execução foi de {tempo:.10f} segundos.")