#Elabore um fuxograma e um programa Python que leia três valores (x, y e z) e um código de condição.
 #Se o código for “c” os valores devem ser escritos em ordem crescente.
 #Se o código for “d”, deve-se escrevê-los em ordem decrescente.


x = float (input ("Qual o valor de x?"))
y = float (input ("Qual o valor de y?"))
z = float (input ("Qual o valor de z?"))
letra = (input ("Qual é o código?"))
if letra == "c":
    if x > y > z:
        print (x, y, z)
    elif y > z > x:
        print (y, z, x)
    elif z > y > x:
        print (z, y, x)
    elif x > z > y:
        print (x, z, y)
    elif (y > x > z):
        print (y, x, z)
    elif (z > x > y):
        print (z, x, y) 
elif letra == "d": 
    if x < y < z:
        print (x, y, z)
    elif y < z < x:
        print (y, z, x)
    elif z < y < x:
        print (z, y, x)
    elif x < z < y:
        print (x, z, y)
    elif (y < x < z):
        print (y, x, z)
    elif (z < x < y):
        print (z, x, y) 