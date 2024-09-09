codigo = int(input("Qual o código do brinquedo?"))
valor = int(input("Qual o valor do pedido?"))
if codigo == 1 and valor >= 1000:
    desconto = 0.10
    print (valor - (valor * desconto), "é seu novo valor a pagar.")
elif codigo == 2 and valor >= 100:
    desconto = 0.05
    print (valor - (valor * desconto), "é seu novo valor a pagar.")
elif codigo == 3 and valor >= 500:
    desconto = 0.10
    print (valor - (valor * desconto), "é seu novo valor a pagar.")
else:
    print("O preço a pagar será o original, de", valor, "reais.")