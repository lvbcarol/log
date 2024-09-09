##**Exercício 01**
#Crie um programa que simule o lançamento de múltiplos dados, permitindo ao usuário escolher o número de dados a ser lançado e
#a quantidade de lados em cada dado.

#*Especificações:**
# O resultado do lançamento de um dado deve ser determinado com o uso da função `randint` do módulo `random`.
# Não há necessidade de validar os dados de entrada.
# O programa deve ser modularizado.



#a)** Desenvolva a função `sorteio` que recebe o número de lados de um dado e retorna o resultado do seu lançamento.
# Execute a célula de teste para verificar o funcionamento da função.

from random import randint
# Função sorteio
def sorteio(num_lados):
  return randint(1, num_lados)
  # o programa retornará um número inteiro e aleatório entre 1 e num_lados

#b)** Desenvolva a função `multiplos_sorteios` que recebe o número de dados a ser lançado e o número de lados de cada dado.
# A função deve retornar uma lista com todos os resultados dos lançamentos.
# Execute a célula de teste para verificar o funcionamento da função.
#IMPORTANTE:* A função `multiplos_sorteios` deve, obrigatoriamente, utilizar a função `sorteio`.

# Função multiplos_sorteios
def multiplos_sorteios(num_dados, num_lados):
  lista_aleatoria = []
  for i in range(1, num_dados + 1):
    aleatorio = randint(1, num_lados)
    lista_aleatoria.append(aleatorio)
  return lista_aleatoria

#c)** Elabore um programa que solicite ao usuário a digitação do número de lados dos dados >=3
# e a quantidade de dados que deverão ser lançados.
# O programa deve exibir uma lista com os resultados dos lançamentos e também a soma dos valores obtidos.

#Programa principal
def aleatorio():
  lista_aleatoria = []
  valor_ok = False
  while not valor_ok:
    num_lados = int(input("Digite o numero de lados (maior ou igual a 3): "))
    num_dados = int(input("Digite o numero de dados: "))
    if num_lados >= 3 and num_dados >= 1:
      valor_ok = True
    else:
      print("Digite numeros válidos!!!")
      valor_ok
  for i in range(1, num_dados + 1):
    num_aleatorio = randint(1, num_lados)
    lista_aleatoria.append(num_aleatorio)
  return lista_aleatoria, sum(lista_aleatoria)

a = aleatorio()
x, y = a
print(x)
print(y)

######

from random import randint 

def informacoes():
  qtd_lados = int(input("Quantos lados os dados têm?"))
  qtd_dados = int(input("Quantos dados você usará?"))
  return qtd_dados, qtd_lados

def sorteio(qtd_lados):
  return randint(1, qtd_lados)

def lista(qtd_lados, qtd_dados):
  resultado = []
  for i in range(1, qtd_dados):
    sorteio.append(resultado)
  soma = sum(resultado)
  return resultado, soma
