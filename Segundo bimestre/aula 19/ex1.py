##**Exercício 01 – Gerando o *user name***

#Em uma universidade, à cada estudante é atribuído um user name necessário para o acesso
# à rede discente. Como parte de seu estágio no Departamento de Tecnologia da Informação
# da universidade, foi-lhe atribuída a tarefa de escrever um programa responsável pela geração dos nomes
# de usuário para os estudantes. As regras para a construção são vistas a seguir:

# Selecione os três primeiros caracteres do nome do estudante (caso o nome possua menos de três caracteres, use o nome completo);

# Selecione os três primeiros caracteres do sobrenome do estudante (caso o sobrenome possua menos de três caracteres, use o sobrenome completo);

# Selecione os três últimos caracteres do registro acadêmico [RA ou ID] do estudante (caso o registro acadêmico ou ID possua menos de três caracteres, use o registro completo);

#O *user name* é criado pela concatenação dos três conjuntos de caracteres (em caixa baixa).

#Para a criação do programa, modularize seu código:

#a)** Crie uma função *gera_login* que recebe como parâmetros o nome, o sobrenome e o registro acadêmico de um estudante e retorna o user name criado.
def gera_login(nome, sobrenome, ID):
    if len(nome) > 3:
        inicio = nome[:3]
    else:
        inicio = nome
    if len(sobrenome) > 3:
        meio = sobrenome[:3]
    else:
        meio = sobrenome
    if len(ID) > 3:
        fim = ID[-3:]
    else:
        fim = ID
    return inicio + meio + fim
#b)** Elabore um programa que permita a entrada de dados de um estudante e exiba o respectivo user name.
import string
nome, sobrenome = input("Digite o nome e o sobrenome:").lower().split()
pontuacao = string.punctuation
ID = input("Digite o ID:")
minha_tabela = str.maketrans("","", pontuacao)
ID = ID.translate(minha_tabela)
login = gera_login(nome, sobrenome, ID)
print(f"\nSeu login na rede é {login}")