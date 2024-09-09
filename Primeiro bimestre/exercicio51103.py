penultima_medicao = float(input ("Qual foi o valor passado do medidor?"))
ultima_medicao = float(input ("Qual o valor atual do medidor?"))
unidades = (ultima_medicao - penultima_medicao)
if 0 <= unidades <= 100:
    print ("Sua conta deu o total de:", unidades * 0.5, "reais")
elif 101 <= unidades <= 200:
    print ("Sua conta deu o total de:", 50 + (1 * unidades), "reais")
elif 201 <= unidades <= 300:
    print ("Sua conta deu o total de:", 150 + (1.5 * unidades), "reais")
elif unidades >= 300:
    print ("Sua conta deu o total de:", 300 + (2 * unidades), "reais")