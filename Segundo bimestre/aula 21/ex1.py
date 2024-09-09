#a)** Construa um programa em Python que troque todas as ocorrencias de uma letra L1
#pela letra L2 em uma *string*. A *string* e as letras L1 e L2 devem ser fornecidas pelo usuario.
string = input("Digite uma string:")
L1 = input("Digite uma das letras presentes na string:")
L2 = input("Digite a letra com que voce deseja substituir:")

newString = string.replace(L1, L2)

print(f"Sua string agira é: {newString}")