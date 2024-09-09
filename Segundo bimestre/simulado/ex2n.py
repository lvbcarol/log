def soma_quadrados(numero):
    return sum(i ** 2 for i in range(1, numero + 1))

while True:
    try:
        numero = int(input("Digite um número inteiro e positivo:"))
        if numero > 0:
            break
        else:
            print("ERRO! Digite um número positivo.")
    except ValueError: 
            print("ERRO! Digite um número inteiro.")

print(f"A soma dos {numero} primeiros números é {soma_quadrados}")
            
numero, lista, soma = soma_quadrados()

