#Conte o número de vogais na frase "Um pouco mais sobre listas"
frase = "um pouco mais sobre listas"
vogais = "a", "e", "i", "o", "u"
contador = 0
for caractere in frase:
    if caractere in vogais:
        contador += 1
print(f"O número de vogais na frase '{frase}' é {contador} vezes.")

string = "I love yo so very much, my darlin."
vowels = "a", "e", "i", "o", "u"
counting = 0
for character in string:
    if character in vowels:
        counting += 1
print(f"The quantity of vowels in the string {string} is {counting} times.")

nome = "Carolina Lansoni Vilas Boas"
novo_nome = nome.lower()
vogais = "a", "e", "i", "o", "u"
contador = 0
for i in novo_nome:
    if i in vogais:
        contador += 1
print(contador)
print(novo_nome)