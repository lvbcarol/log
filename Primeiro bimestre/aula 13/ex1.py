#Elabore um programa Python que exiba todos os números pares entre zero e um número `N` fornecido pelo usuário.
#Requisito: Certifique-se de que o usuário tenha digitado um número positivo.
#while ok:
  #  numero = float(input("Digite um número positivo."))
  #  if numero > 0:
  # else:
  #     print("ERRO: o número deve ser positivo!")
#print(f"Números pares entre 0 e {numero}")
#number = 0
#while number <= numero:
   # print(number)
  #  number += 2

num_max = int(input("Digite um número positivo:"))
if num_max > 0:
    contador = 0
    while num_max > contador:
        print(contador)
        contador += 2
else:
        print("o número deve ser positivo.")
#vai sempre continuar sendo par, mesmo que oq vc digitar for ímpar pq tá adicionando 2 ao contador, e não ao número máximo, e contador começa como zero.
     