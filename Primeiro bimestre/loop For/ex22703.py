#2 - Contagem de Caracteres em uma String
#Dada uma string, use um for loop para contar quantas vezes um determinado caractere aparece nela.
texto = "exemplo de string"
caractere = "e"
count = 0
for c in texto:
    if c == caractere:
        count = count + 1
print(count)

string = "Carolina Lansoni Vilas Boas "
caractere = "a"
contador = 0
for a in string:
    if a == caractere:
        contador += 1
print("O número de vezes que", caractere, "aparece em", string, "é", contador, "vezes.")
        
        