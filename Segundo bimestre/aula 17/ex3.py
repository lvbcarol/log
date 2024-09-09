#Exercício 03 – Jo Ken Po!**
#Escreva um programa que gerencie um jogo de Pedra, Papel e Tesoura entre o usuário e o computador. Para tanto:
#a)**  Elabore a função `jogador` que retorna a escolha do usuário. Para guiar tal escolha, a função deve exibir um menu
# que informe ao usuário para digitar:
#0 para “Pedra”;
#1 para “Papel”;
#2 para “Tesoura”.
#Essa associação será a base da lógica do programa.
def escolha():
    Pedra = 0
    Papel = 1
    Tesoura = 2
    escolha_jogador = int(input("Digite 0 para Pedra, 1 para Papel e 2 para Tesoura."))
    if escolha_jogador == "0":
        return Pedra
    if escolha_jogador == "1":
        return Papel
    if escolha_jogador == "2":
        return Tesoura

#b)** Elabore a função `computador` que retorna a escolha aleatória do computador (você pode usar a função `randint` do módulo random
from random import random
def computador(escolha):
    escolhas = ['pedra', 'papel', 'tesoura']
    return escolhas[random.randint(0, 2)]

# Exemplo de uso:
escolha_do_computador = computador()
print(f"A escolha aleatória do computador é: {escolha_do_computador}")
{escolha_do_computador}


#*c)** Elabore a função `quem_ganhou` que recebe as escolhas do jogador e do computador, as exibe e então determina o vencedor segundo o critério:
#Se algum dos jogadores escolhe “Pedra” e o outro escolhe “Tesoura”, então “Pedra” vence o jogo (“Pedra” esmaga “Tesoura”).
#Se algum dos jogadores escolhe “Tesoura” e o outro escolhe “Papel”, então “Tesoura” vence o jogo (“Tesoura” corta “Papel”).
#Se algum dos jogadores escolhe “Papel” e o outro escolhe “Pedra”, então “Papel” vence o jogo (“Papel” embrulha “Pedra”).
#Se ambos os jogadores fazem a mesma escolha, o jogo deve ser reiniciado.
def quem_ganhou(escolha_jogador, escolha_computador):
    print(f"Jogador: {escolha_jogador} - Computador: {escolha_computador}")
    
    if escolha_jogador == escolha_computador:
        print("Empate! O jogo será reiniciado.")
        return 'empate'
    elif (escolha_jogador == 'pedra' and escolha_computador == 'tesoura') or \
         (escolha_jogador == 'tesoura' and escolha_computador == 'papel') or \
         (escolha_jogador == 'papel' and escolha_computador == 'pedra'):
        print("Jogador vence!")
        return 'jogador'
    else:
        print("Computador vence!")
        return 'computador'

#d)** Use as funções dos itens anteriores e escreva o programa.