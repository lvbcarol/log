#dada um lista de números 0 a 50, retorne a lista com todos os números pares multiplicados por 2 
#e todos os números ímpares multiplicados por -1 
lista = [x * 2 if x % 2 == 0 else -x for x in range(50)]
#lembrando que esse x não será excluído, e sim se tornará negativo.

nova_lista = []
for i in range(11):
    if i % 2 == 0:
        nova_lista.append(i*2)
    else:
        nova_lista.append(-i)
print(lista)


number = int(input("Type a number:"))
list = [i * 2 if i % 2 == 0 else -i for i in range(number)]
print(list)

lista = [i * 2 if i % 2 == 0 else -i for i in range(0, 11)]
print(lista)