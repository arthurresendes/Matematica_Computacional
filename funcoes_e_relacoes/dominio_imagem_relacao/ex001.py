# Para R = {(1, 2), (1, 3), (2, 3), (3, 4)}, determine o domínio e a imagem.

r = {(1, 2), (1, 3), (2, 3), (3, 4)}
primeiro_elemento: set = set()
segundo_elemento: set = set()
for v in r:
    primeiro_elemento.add(v[0])
    segundo_elemento.add(v[1])

print(primeiro_elemento)
print(segundo_elemento)