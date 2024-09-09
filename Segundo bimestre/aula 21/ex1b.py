#b)** Escreva um programa que leia duas palavras e diga qual deles vem primeiro na ordem
#alfabetica.

palavra1 = ("Digite uma palavra:")
palavra2 = input("Digite maai uma palavra:")

if palavra1.lower() < palavra2.lower():
    print(f"{palavra1}, {palavra2}") 

if palavra1.lower() > palavra2.lower():
    print(f"{palavra2}, {palavra1}") 

else:
    print("As palavras são iguais")