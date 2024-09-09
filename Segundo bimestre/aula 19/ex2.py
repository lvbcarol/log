##**Exercício 02 - Validação de senha**

#Continuando seu trabalho no Departamento de TI da universidade, sua nova tarefa é a criação
# de um programa que valide a escolha de senha de cada estudante para o acesso à rede de computadores.
# Quando da criação da senha, o estudante foi comunicado de que a senha escolhida devia:

# Ser formada por, no mínimo, sete caracteres;
# Conter ao menos uma letra maiúscula;
# Conter ao menos uma letra minúscula;
# Conter ao menos um dígito numérico.

#Para a criação do programa, modularize seu código:

#*a)** Crie uma função *valida_senha* que recebe como parâmetro a senha do usuário 
#e retorna *True* se a senha é válida ou *False*, caso contrário.
def valida_senha(senha):
    COMP_SENHA = 7
    maiuscula_ok = False
    minuscula_ok = False
    if len(senha) >= COMP_SENHA:
        for caractere in senha:
            if caractere.isupper():
                maiuscula_ok = True
            if caractere.islower():
                minuscula_ok = True
            if caractere.isdigit():
                numero_ok = True
        return maiuscula_ok and minuscula_ok and numero_ok
    else:
        return False 
    
#b)** Elabore um programa que solicite a digitação da senha. 
#Caso se trate de uma senha válida, o programa deve exibir a mensagem “Senha validada”.
# Caso seja inválida, o processo de entrada deve se repetir até que uma senha válida seja informada.
senha = input("Digite sua senha:")
while not valida_senha(senha):
    print("ERRO: SEnha inválida!")
    senha = input("Digite sua senha:")
print("SEnha validada!")