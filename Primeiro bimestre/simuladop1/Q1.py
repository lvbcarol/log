P1 = float(input("Digite a nota de P1:"))
P2 = float(input("Digite a nota de P2:"))
T1 = float(input("Digite a nota de T1:"))
T2 = float(input("Digite a nota de T2:"))
T3 = float(input("Digite a nota de T3:"))

Mp = (P1 + P2)/2
Mt = (T1 * 0.4 + T2 * 0.4 + T3 * 0.2)
Mf = (Mp + Mt)/2

if Mf >= 6:
    print("aprovado")
else:
    print("reprovado")