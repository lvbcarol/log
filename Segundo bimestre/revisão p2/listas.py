#Quadrado de todos os valores entre 1 e 10:
quadrados = [i ** 2 for i in range(0, 11)]
print(quadrados)

#caps lock e lower case
nome1= "juReMa"
nome2= "AliCia"
novo_nome1 = nome1.lower()
novo_nome2 = nome2.upper()
print(novo_nome1, novo_nome2)

#Criando uma lista entre 1 e 10 que pule de dois em dois números
lista = [i for i in range(0, 11, 2)]
print(lista)

#retornar número par dobrado e ímpar negativo
função = [i ** 2 if i % 2 == 0 else -i for i in range(0, 11)]
print(função)

#Funções de Strings
String = "Me diz chegou bem em casa"
nova_string = String.split()
print(nova_string)

Frase = "Carolinal"
print(Frase[0])
print(Frase[3])
print(Frase[1:3])
print(Frase[-1])
print(Frase[:5])
print(Frase[5:])