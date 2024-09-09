#Escreva um programa em Python que exiba todos os divisores de um número inteiro fornecido pelo usuário.
#Valide os dados de entrada (*Sugestão:* pesquise sobre a estrutura `try-except`.)
#Os divisores do número fornecido devem ser armazenados em uma lista, em ordem crescente.
# Use a função `time` da biblioteca `time` para medir o tempo de processamento para a entrada 123456789.

#from time import time
#divisores = []
#verificacao = False
#while not verificacao:
    #try:
        #num = int(input("Digite um número inteiro e positivo."))
        #if num > 0:
            #verificacao = True
        #else:
            #print("ERRO! Digite um número inteiro positivo.")
    #except:
        #print("ERRO! Digite um número inteiro.")

#inicio = time()
#print(inicio)
#for sequencia in range(1, num +1):
    #if num % sequencia == 0:
        #divisores.append(sequencia)
#fim = time()
#print(fim)

#print(f"Lista de divisores de {num}")
#print(divisores)
#tempo = fim - inicio
#print(f"tempo de execução; {tempo:10f} segundos.")

#append serve para adicionar o valor dentro do () ao final da lista.

from time import time
dividers = []
checked = False 
while not checked:
    try:
        number = int(input("Type an entire and positive number:"))
        if number > 0:
            checked = True
        else: print("ERROR! Type a positive number!")
    except:
        print("ERROR! Type an entire number ")

start = time()
for list in range(1, number +1):
    if number % list == 0:
        dividers.append(list)
end = time()

print(f"Dividers list of the number {number}")
print(dividers)
timer = end - start 
print(f"The time of excecution has been of about {timer:10f} seconds. ")
