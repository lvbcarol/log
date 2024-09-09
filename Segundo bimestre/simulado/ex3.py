#**Exercício 03**
#Elabore um programa modularizado que implemente uma agenda de contatos.
#Os contatos estarão armazenados em um dicionário cujas chaves são os nomes dos contatos e os valores são listas
#que contém o telefone e o perfil do contato no Instagram.
#Para ajudar no desenvolvimento do programa, execute a célula a seguir para criar um dicionário base.


# Agenda baseagenda = {'Gustavo Alves': ['(11) 99685-2345', '@gu_alves'],
agenda = {'Laura Alves': ['(11) 97428-2001', '@lalinha_alves'],
'Janaina Goulart': ['(21) 92134-0543', '@jango_25'],
'Maria Prado': ['(35) 93821-2289', '@mariaprado_insta'],
'Zenon Galhardo': ['(13) 92121-3997', '@zengalhardo']}

#a) Elabore uma função `adiciona_contato` que recebe um dicionário de contatos, insere as informações 
#do novo contato e retorna o dicionário de contatos atualizado. Execute a célula de teste para verificar o funcionamento da função.

# Função adiciona_contato
def adiciona_contato(dic):
  nome = input("Digite o nome do contato: ")
  numero = input("Digite seu número:" )
  insta = input("Digite o contato de seu instagram: ")
  lista = [numero, insta]
  dic [nome] = lista

# Teste da função adiciona_contato
# Informações do novo contato:
# Nome: Joaquim Santos
# Celular: (13) 94576-1209
# Instagram: @jocantos
adiciona_contato(agenda)
print (agenda)

#b)** Elabore uma função `apaga_contato` que recebe um dicionário de contatos e o nome do contato a ser apagado.
# Após a eliminação do contato, retorna o dicionário atualizado.
# Execute a célula de teste para verificar o funcionamento da função.

# Função apaga_contato
def apaga_contato(dic, nome):
  del dic [nome]
  return dic

# Teste da função apaga_contato
sla = apaga_contato(agenda, 'Maria Prado')
print(sla)

#c)Elabore uma função `encontra_contato` que recebe um dicionário de contatos e o nome do contato a ser localizado.
#caso o contato esteja na agenda, a função deve exibir suas informações; caso contrário, deve informar ao usuário que
#o contato não foi encontrado.
#execute a célula de teste para verificar o funcionamento da função.

# Função encontra_contato
def encontra_contato(dic, nome):
  encontrado = False
  for k in dic.keys():
    if nome == k:
      nome_encontrado = k
      encontrado = True
      break
    else:
      encontrado
  if encontrado == True:
    print(f'{nome_encontrado} = {dic [nome_encontrado]}')

  else:
    print("Usuário não encontrado!")

# Teste da função encontra_contato
encontra_contato(agenda, 'Laura Alves')
encontra_contato(agenda, 'Cleber Silva')

#d)** Elabore uma função `atualiza_contato` que recebe um dicionário de contatos e o nome do contato cujas informações 
#devem ser atualizadas.
#caso o contato esteja na agenda, a função deve perguntar ao usuário qual das informações deseja atualizar
# (1-celular, 2-Instagram). Após a atualização, a função deve retornar o dicionário de contatos atualizado. 
#Caso contrário, deve informar ao usuário que o contato não foi encontrado.
#execute a célula de teste para verificar o funcionamento da função.

# Função atualiza_contato
def atualiza_contato(dic, nome):
  if nome in agenda:
    atualizacao = dic[nome]
    escolha = int(input("Qual informação deseja atualizar?(1-celular, 2-instagram): "))
    if escolha == 1:
      sla = input("Digite o número de celular: ")
      atualizacao[0] = sla
    elif escolha == 2:
      sla = input("Digite o @ do insta: ")
      atualizacao[1] = sla
    else:
      print("digite uma informação válida!")

# Teste da função atualiza_contato
atualiza_contato(agenda, 'Laura Alves')
atualiza_contato(agenda, 'Cleber Silva')
print(agenda)