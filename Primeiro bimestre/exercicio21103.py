idade = int(input ("Quantos anos você tem?"))
if idade < 2:
    print ("Você é um bebê.")
elif 2 < idade < 4:
    print ("Você é uma criança de colo.")
elif idade < 13:
    print ("Você é uma criança.")
elif idade < 20:
    print ("Você é um adolescente.")
elif idade < 65:
    print ("Você é um adulto.")
else:
    print ("Você é um idoso.")