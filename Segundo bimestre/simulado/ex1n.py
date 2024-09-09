from random import randint 

def informacoes():
  qtd_lados = int(input("Quantos lados os dados têm?"))
  qtd_dados = int(input("Quantos dados você usará?"))
  return qtd_dados, qtd_lados

def sorteio(qtd_lados):
  return randint(1, qtd_lados)

def lista(qtd_lados, qtd_dados):
  resultado = []
  for i in range(qtd_dados):
    resultado.append(randint(1, qtd_lados))
    #o nome da lista, append e só depois o que vai ser adicionado ao final da lista.
  soma = sum(resultado)
  return resultado, soma

def saída(resultado, soma):
    print(resultado)
    print(soma)
    return(resultado, soma)

# Chamar as funções
qtd_dados, qtd_lados = informacoes()
resultado, soma = lista(qtd_lados, qtd_dados)
saída(resultado, soma)