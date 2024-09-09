# Exercício 04
valorInicial = print (("Digite o valor inicial:") input(float))
taxaJuros = print (("Digite a taxa de juros:") input (float))
periodoInvestimento = print (("Digite o período de investimento:") input (float))

resultado =  valorInicial * (1 + (taxaJuros / 100) ** periodoInvestimento)

print (resultado)