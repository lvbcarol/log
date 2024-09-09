#Função simples
def say_hello():
    print("hello")

say_hello()

#Função com parâmetro
def saudações(nome):
    print(f"Hello, {nome}")

saudações("José")

#return
def soma(num1, num2):
    return num1 + num2

print(soma(2, 2))

#lógica
def e_par(num):
    return num % 2 == 0

print(e_par(22))

#ou

def soma(n1, n2):
    resultado = n1 + n2
    return resultado

soma(2, 4)

def subtração(n1, n2):
    resultado = n1 - n2
    return resultado

subtração(6, 2)

resultado = soma(2, 4)
print("A soma é", soma(2,4))
resultado = subtração(6,2)
print("A subtração é", subtração(6,26))