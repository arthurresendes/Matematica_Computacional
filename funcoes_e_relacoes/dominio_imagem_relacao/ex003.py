# Dada R = {(x, y) | y = x², x ∈ {−2, −1, 0, 1, 2}}, encontre o domínio e a imagem.

r = {(-2,4),(-1,1),(0,0),(1,1), (2,4)}
primeiro_elemento: set = set()
segundo_elemento: set = set()
for v in r:
    primeiro_elemento.add(v[0])
    segundo_elemento.add(v[1])

print(primeiro_elemento)
print(segundo_elemento)