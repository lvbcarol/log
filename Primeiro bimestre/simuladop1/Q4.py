num = int(input("digite um número inteiro positivo."))
for i in range (2, int(num**0.5)+ 1):
    if num % i == 0:
        print(num, "não é primo")
        break
else:
    print(num, "é primo")