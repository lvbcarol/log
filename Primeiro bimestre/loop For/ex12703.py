#1 - Calculando a Média de uma Lista de Notas:
#Dada uma lista de notas de alunos, use um for loop para calcular a média das notas.


lista_notas = [9, 8,10, 7.5, 10, 4]
total = 0
for nota in lista_notas:
    total += nota 
print("total:", total)
print("média:", total/len(lista_notas))
#len é para somar todos da lista e dividir pela quantidade de notas inseridas


lista_notas = [6,8]
contador= 0 
for nota in lista_notas:
    contador += nota   #total = total + nota
    
print("total:", contador)
print("média", contador/len(lista_notas))