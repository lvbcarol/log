#Exercício 02 – Média e Conceito**
#Escreva um programa que:
#Solicita ao usuário a entrada de 5 notas relativas a avaliações (números inteiros entre 0 e 100);
#Calcula a média associada;
#Determina o respectivo conceito final na disciplina, segundo a tabela abaixo.
#Média    Conceito
#90 100 a
#80 89 b
#70 79 c
#60 69 d
#< 60 = f

#a)** Elabore a função `entrada` que deve retornar uma lista com as cinco notas obtidas na disciplina.
#Lembre-se de validar os dados de entrada
def entrada():
    notas = []
    while True:
        try:
            nota = int(input("Digite a nota (entre 0 e 100):"))
            if 0 <= nota <= 100:
                notas.append(nota)
                break
            else:
                print("Insira um número entre 0 e 100.")
        except ValueError:
            print("Insira um número inteiro")
    return notas

#b)** Elabore a função `media` que recebe a lista de notas e retorna a média (numérica) alcançada
def media(notas):
    return sum(notas) / len(notas)

#c)** Elabore a função `conceito` que recebe a média das notas e retorna o conceito a ela associado.
def conceito(media):
    if 90 <= media <=100:
        return "A"
    if 80 <= media <=89:
        return "B"
    if 70 <= media <=79:
        return "C"
    if 60 <= media <=69:
        return "D"
    elif media < 60:
        return "F"
    
#d)Use as funções dos itens anteriores e escreva o programa.
notas = entrada()
media_notas = media(notas)
conceito_final = conceito(media_notas)
print(f"Média das notas: {media_notas:.2f}")
print(f"Conceito final: {conceito_final}")

