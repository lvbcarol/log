import math

v0 = 5
g = 9.81
y = 0.2

#a diferença deste para o anterior é que é importado o math e tem comandos especiais  
t1 = (v0 - math.sqrt(v0**2 - 2*g*y)) / g
t2 = (v0 + math.sqrt(v0**2 - 2*g*y)) / g

print(f'tempo na subida: {t1}, tempo na descida: {t2}')


