#entrada 
v0 = 5
g = 9.81
y = 0.2

#processamento
t1 = (v0 - (v0**2 - 2*g*y)**0.5) / g
t2 = (v0 + (v0**2 - 2*g*y)**0.5) / g

#saída 
print(f'tempo na subida: {t1}, tempo na descida: {t2}')