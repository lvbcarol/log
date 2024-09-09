#3. Escreva um programa Python para verificar se uma determinada chave já existe em um dicionário.

#A função 'chave_presente' recebe dois argumentos: i) um dicionário e ii) um valor para conferência. 
#A função deve dizer se a chave se encontra ou não no dicionário.

#Teste com o dicionário {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}. Verifique as chaves 5 e 9.

dicionario = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def chave_presente(d, x):
    if x in d:
        return f"Chave {x} está no dicionário."
    else:
        return f"Chave {x} não está no dicionário."
    
print(chave_presente(dicionario, 5))

print(chave_presente(dicionario, 9))