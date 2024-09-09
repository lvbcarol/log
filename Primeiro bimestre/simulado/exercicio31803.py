#Escreva um programa em Pyhton para calcular o salário total a ser pago por uma semana de trabalho. Horas extras trabalhadas acima das 40 
#horas contratuais são pagas com adicional de 50% por hora extra trabalhada.

#**Requerimento:**
#* Insira o número de horas trabalhadas na semana e valor a ser recebido por hora;
#* Calcule o número de horas adicionais e o pagamento extra por trabalhar mais de 40 horas por semana;
#* Calcule o pagamento a ser efetuado;
#* Os valores de saída devem ser definidos com 2 casas decimais.

#**Exemplos de saída:**

#$\Rightarrow$ Abaixo das 40 horas contratuais:

#`Digite o número de horas trabalhadas na semana: 25`

#`Digite o valor a ser recebido por hora trabalhada: 12`

#`O salário a ser recebido é de $300.00`

#$\Rightarrow$ Acima das 40 horas contratuais:

#`Digite o número de horas trabalhadas na semana: 57`

#`Digite o valor a ser recebido por hora trabalhada: 12`

#`Você trabalhou 17 horas extras nessa semana. O total pelas horas extras é de $306.00`

#`O salário a ser recebido é de $786.00`

horas = float(input("Digite o número de horas trabalhadas na semana:"))
valor = float(input("Digite o valor a ser recebido por hora:"))

if horas <= 40:
    salario = horas * valor 
    print ("O salário a ser recebido é de:", salario)
else:
    salario = 40 * valor 
    extra = horas - 40
    salario_extra = extra * (valor * 1.5)
    salario_final = salario + salario_extra
    print(f"Você trabalhou {extra} horas extras nessa semana. O total pelas horas extras é de ${salario_extra}")
    print("o salário a ser recebido é de:", salario_final)
