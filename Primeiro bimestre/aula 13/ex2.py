from math import log
ok = False
while not ok:
    x =float(input("Digite o valor de x:"))
    if x > 0:
        ok = True
    else:
        print("ERRO, X deve ser positivo!")
while ok:
    n =float(input("Digite o valor de n:"))
    if n > 0:
        ok = True
    else:
        print("ERRO, N deve ser positivo!")
if type(n) is float:
    n = int(n)

S = log(x)
for i in range(1, n+1):
    S += x**i/i

print(f"O valoe da série é {S:.3f}")
#esse .3f é para definir apenas três números depois 
#da primeira casa