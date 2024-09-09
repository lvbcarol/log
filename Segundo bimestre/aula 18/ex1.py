##**Estudo de Caso - Aliados políticos**
#um ambiente como a Câmara dos Deputados ou o Senado Federal é muito importante que um membro dessas casas seja capaz de detectar potenciais aliados, colegas que estejam alinhados em termos de propósitos, valores morais e éticos.
#uma forma de se determinar o alinhamento ideológico entre dois congressistas é determinar a concordância entre os registros de votação de cada um.
#assim, se na votação de determinado projeto de lei ou emenda constitucional é possível votar a favor (1) ou contra (0), o alinhamento se dá na medida da concordância entre os votos de cada congressista.
#podemos então medir a concordância ideológica entre dois congressistas ao identificarmos quantas vezes votaram da mesma forma. Vejamos um exemplo. Considere os registros de votação de três congressistas:
#cong_A = [1, 1, 0, 0, 1]`
#cong_B = [1, 0, 0, 1, 1]`
#cong_C = [1, 1, 0, 1, 1]`
#Nota-se que Concordância$_{AB}=3$ e Concordância$_{AC}=4$. Então, o congressista 
#$A$ deveria se aliar ao congressista $C$, em detrimento de uma aliança com o congressista $B$.
#vamos construir um programa que, a partir de listas de votação geradas aleatoriamente, 
#seja capaz de indicar qual o melhor aliado para um determinado congressista. Para tanto:

#a)** Elabore a função `gera_votos` que recebe o número de votos desejado (`num_votos`) e retorna uma lista contendo `num_votos` elementos sorteados aleatoriamente entre 0 e 1. Exemplo de uso:

#import random`
#random.seed(10) # Para garantir o mesmo sorteio!`
#votos1 = gera_votos(5)`
#print(votos1)`
#[0, 1, 1, 0, 0]`
#random.seed(10) # Para garantir o mesmo sorteio!`
#votos2 = gera_votos(8)`
#print(votos2)`
#[0, 1, 1, 0, 0, 1, 1, 1]`

import random 

def gera_votos(num_votos):
    return [random.randint(0,1) for _ in range(num_votos)]
 
#Testes
random.seed(486123784) #para garantir o mesmo sorteio
votos1 = gera_votos(5)
print(votos1)
votos2 = gera_votos(5)
print(votos2)

#b)** Elabore a função `concordancia` que recebe duas listas de mesmo comprimento
# (contendo somente `0's` e `1's`) e retorna a concordância ideológica entre as duas. Exemplo de uso:
#x = [1, 1, 0, 0, 1]`
#y = [1, 1, 0, 1, 1]`
#print(concordancia(x, y))`
#4`

def concordancia():
    x = [1, 1, 0, 0, 1]
    y = [1, 1, 0, 1, 1]
    print(concordancia(x, y))

#c)** Elabore a função gera_ficha_votos` que recebe como parâmetros uma lista nomes
#(contendo os nomes dos congressistas) e o inteiro `num_votos` (o número de votos registrados para cada congressista). 
#Caso o comprimento da lista nomes seja superior a 1, a função deve retornar uma lista de tuplas nomeadas do tipo Ficha 
#(uma tupla para cada congressista), em que o campo votacao deve ser preenchido com um histórico de votos 
#gerado de forma aleatória (use a função `gera_votos`). Caso contrário, deve retornar uma única tupla nomeada,
# nas mesmas condições expostas acima. Exemplo de uso¹: