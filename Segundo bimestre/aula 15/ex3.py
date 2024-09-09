#No jogo *Lucky Sevens*, o jogador rola um par de dados. Se os pontos somarem 7, o jogador ganha $\$4$; caso contrário, perde $\$1$.
#Elabore um programa em Python que implemente uma versão eletrônica do *Lucky Sevens*. O programa deve receber como entrada a quantia
# de dinheiro que o jogador quer disponibilizar para apostas.
#Após cada rodada, o jogador decide se quer continuar ou não.
# O jogo acaba quando os recursos acabarem ou quando o jogador decidir pelo término.
#Se o término ocorrer por falta de recursos, o programa deve exibir o número de jogadas que foram necessárias para derrotar o jogador.
import random

def jogar_dados():
    return random.randint(1, 6) + random.randint(1, 6)

def lucky_sevens():
    dinheiro = int(input("Digite a quantia de dinheiro que você quer apostar: "))
    jogadas = 0

    while dinheiro > 0:
        jogadas += 1
        if jogar_dados() == 7:
            dinheiro += 4
        else:
            dinheiro -= 1

        continuar = input("Você tem \$" + str(dinheiro) + ". Quer continuar jogando?")
        if continuar.lower() != 's':
            break
        print("O jogo acabou após", jogadas, "jogadas.")

lucky_sevens()

#randit serve para random de números inteiros
#str(dinheiro) é para converter dinheiro que é int para string