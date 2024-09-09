##**Exercício 05**##
#Elaborar um programa Python que, dada a idade de um nadador, classifique-o nas categorias:
#* infantil A (5 - 7 anos);
#* infantil B (8 - 10 anos);
#* juvenil A (11 - 13 anos);
#* juvenil B (14 -17 anos);
#* adulto (maiores que 18 anos).
idade = int(input ("Qual a sua idade?"))
if idade < 5:
    print ("Bebê")
elif 5 <= idade <= 7:
    print ("Infantil A")
elif 8 <= idade <= 10:
    print ("Infantil B") 
elif 11 <= idade <= 10:
    print ("Juvenil A")
elif 14 <= idade <= 17:
    print ("Juvenil B")
else:
    print ("Adulto")
