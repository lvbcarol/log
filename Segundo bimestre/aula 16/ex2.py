#some os números pares divisiveis por 7 entre 0 e 100
valores = [x for x in range(0, 101) if x % 2 ==0 and x % 7 == 0]
soma_valores = sum(valores)
print(valores)
print(f"A soma dos valores da lista é de: {soma_valores}")

#5 between 0 and 50
values = [i for i in range(0,50) if i % 2 == 0 and i % 7 == 0]
calculator = sum(values)
print(values)
print(f"The result of them added is {calculator}.")
