#Escreva um programa em Python que calcule e exibe um relatório de investimento.
#As entradas para o programa são:
#O valor inicial a ser investido (número real)
#O período do investimento em anos (número inteiro)
#A taxa de juros (porcentagem expressa como número real)

#O programa utiliza uma forma simplificada de juros compostos, em que os juros são calculados uma vez 
#ao ano e adicionados ao valor investido. A saída do programa é um relatório em formato tabular que 
#mostra, para cada ano do investimento, o saldo inicial, os juros ganhos no ano e o saldo final.

#Após a saída tabular, o programa imprime o valor total do saldo do investimento
#e o valor total de juros auferidos no período, como visto no exemplo de uso a seguir:

#`Digite o valor do investimento: 15000`

#`Digite o período do investimento (em anos): 10`

#`Digite a taxa de juros anual (em %): 5`

#lista de listas com os balanços anuais do investimento
balanco = []

#entrada de dados (sem validação)
investimento = float(input("Digite o valor do investimento:"))
anos = int(input("Digite o periodo do investimento em anos:"))
taxa = float(input("Digite a taxa de juros anual em %:"))
taxa = taxa / 100

#cabeçalho de tabela 
print(f"\n*************** Balanço anual ***************")
print(f"Ano\tValor inicial\tJuros\tValor final")

#Calculo do balanço
inicio_ano = investimento 
for ano in range(1, anos +1):
    juros = inicio_ano * taxa
    fim_ano = inicio_ano + juros
    print(f"{ano}\t{inicio_ano:.2f}\t{juros:.2f}\t{fim_ano}")
    balanco.append([ano, inicio_ano, juros, fim_ano])
    inicio_ano = fim_ano

#saída de dados
print(f"\nValor disponível ao final do período: {fim_ano:.2f}")
print(f"Juros auferidos no períodos: {fim_ano - investimento:.2f}")

#impressão da lista com os balanços anuais 
print(f"\nLista com valores anuais:")
for item in balanco:
    print(item)






