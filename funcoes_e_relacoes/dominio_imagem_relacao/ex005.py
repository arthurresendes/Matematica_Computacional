def ordena(exemplo):
    ordenado = sorted(exemplo)
    return ordenado

x = [1,2,3,4]
y = [1,4,9,16]
r = set()
for i in x:
    for j in y:
        r.add((i,j))

dominio = set()
imagem = set()
for k in r:
    dominio.add(k[0])
    imagem.add(k[1])

dominio = tuple(ordena(dominio))
imagem = tuple(ordena(imagem))

print(f"Resultado X x Y: {r}\nOnde o y é x ao quadrado")
print(f"Dominio: {dominio}")
print(f"Imagem: {imagem}")
