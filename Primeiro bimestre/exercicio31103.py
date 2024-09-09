#Escreva um programa Python que recebe um único carácter como entrada e decide se esse carácter é uma letra maiúscula, uma letra minúscula, um algarismo decimal ou um carácter especial.

#Na codificação ASCII:
#* As letras maiúsculas de 'A' a 'Z' são codificadas pelos decimais 65 a 90;
#* As letras minúsculas de 'a' a 'z' são codificadas pelos decimais 97 a 122;
#* Os algarismos decimais são codificados pelos decimais 48 a 57;
# Os decimais de 0 a 255, com exceção daqueles mencionados acima, codificam caracteres especiais.



original = input("Qual o caracter?")
convertido = ord (original)
if 65 <= convertido <= 90:
    print ("Letra maiúscula.")
elif 97 <= convertido <= 122:
    print ("Letra minúscula.") 
elif 48 <= convertido <= 57:
    print ("Algarismo decimal.")
else:
    print ("Caracter especial.")

