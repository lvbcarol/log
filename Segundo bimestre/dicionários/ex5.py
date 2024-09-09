#5. Mescle dois dicionários.
#Por exemplo, a partir dos dicionários d1 = {'a': 100, 'b': 200} e
#d2 = {'x': 300, 'y': 200}, crie um dicionário d3 = {'a': 100, 'b': 200, 'x': 300, 'y': 200}

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

d1.update(d2)
#este update é para unir os dois dicionários

print(d1)
#não precisa criar outra varíavel chamada d3, pq agora este já é o novo valor de d1.