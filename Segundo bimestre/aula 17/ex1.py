#**Exercício 01 – Quanto custa renovar a pintura?**

#Uma empresa de serviços de pintura determinou que para finalizar 112 ft² de espaço de parede
# são necessários um galão de tinta e oito horas de trabalho. A taxa de mão-de-obra é de $ 35,00/h.

#Escreva um programa que peça ao usuário para inserir a área a ser pintada e o preço por galão da tinta escolhida. 
#O programa deve exibir os seguintes dados:

#O número de galões de tinta necessário para o serviço;
#A quantidade de horas de trabalho previstas para a obra;
#O custo relativo à tinta escolhida;
#A taxa de mão de obra associada;
# O custo total da obra.

#Para tanto, modularize seu código:

#a)** Crie uma função para a entrada de dados.
def obter_dados():
    area = float(input("Digite a área a ser pintada em pés:"))
    preco_por_galao = float(input("Digite o preço por galão da tinta esolhida:"))
    return area, preco_por_galao 

area, preco_por_galao  = obter_dados()

#b)** Crie uma função responsável por determinar cada informação de saída.
def informações(area, preco_por_galao):
    num_galoes = (area // 112) + 1
    horas = num_galoes * 8
    custo_tinta = num_galoes * preco_por_galao
    taxa_mao_de_obra = horas * 35
    custo_total = num_galoes + horas + custo_tinta + taxa_mao_de_obra
    return num_galoes, horas, custo_tinta, taxa_mao_de_obra, custo_total 

num_galoes, horas, custo_tinta, taxa_mao_de_obra, custo_total = informações(area, preco_por_galao)

#c)** Use as funções dos itens anteriores e escreva o programa.
print("----------------------------")
print("Informações sobre a pintura:")
print(f"O número de galões é {num_galoes:.0f}")
print(f"O número de horas é {horas:.0f}")
print(f"O custo da tinta é de R${custo_tinta:.2f}")
print(f"A taxa da mão de obra é de R${taxa_mao_de_obra:.2f}")
print(f"O custo total é de R${custo_total:.2f}")
