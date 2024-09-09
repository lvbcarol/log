#verficação
valor_ok = False
while not valor_ok:
    try:
        valor = int(input("digite um valor inteiro e par."))
        if valor % 2 == 0:
            valor_ok = True
        else:
            print("Erro! O valor não é par.")
    except:
        print("Erro!O valor não é inteiro.")

#conta
notas100 = valor//100
valor %= 100                 #valor = valor % 100
notas50 = valor//50
valor %= 50
notas20 = valor//20
valor %= 20
notas10 = valor//10
valor %= 10
notas5 = valor//5
valor %= 5
notas2 = valor//2

#impressão
print(f"Valor sacado: R$ {valor}")
print("notas de R$100:", notas100)
print("notas de R$50:", notas50)
print("notas de R$20:", notas20)
print("notas de R$10:", notas10)
print("notas de R$5:", notas5)
print("notas de R$2:", notas2)