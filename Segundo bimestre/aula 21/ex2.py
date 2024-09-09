#**Exercício 02 – Senha da biblioteca**
#Uma biblioteca distribui um cartão magnético para que os alunos possam frequentá-la.
# A senha inicial, enviada pelo correio, é gerada automaticamente a partir da data de nascimento 
#do aluno ('dd/mm/aaaa') do seguinte modo:
#mm'$'dd(invertido) + '#' + dd'!'mm(invertido) + '\'+aaaa`
#Assim, se a data de nascimento é 25/10/1995, a senha será:
#10$52#25!01\1995`
#Escreva um programa modular que solicite ao usuário a inserção da data de nascimento
#| no formato dd/mm/aaaa e retorne sua senha de acordo com as regras da biblioteca.

def gerar_senha(data_nascimento):
    # Separa a data de nascimento em dia, mês e ano
    dd, mm, aaaa = data_nascimento.split('/')
# Inverte o dia e o mês
    dd_invertido = dd[::-1]
    mm_invertido = mm[::-1]
# Gera a senha de acordo com as regras da biblioteca
    senha = f"{mm}$'{dd_invertido}#'{dd}!'{mm_invertido}\\{aaaa}"
    return senha
# Solicita ao usuário que insira a data de nascimento
data_nascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")
# Gera e imprime a senha
senha = gerar_senha(data_nascimento)
print(f"Sua senha é: {senha}")