x =[1,2,3,4]
y = [3,5,7,9]
r = set()
for i in x:
    for j in y:
        r.add((i,j))
r_ordenado = sorted(r)

dominio = set()
imagem = set()
for k in r:
    dominio.add(k[0])
    imagem.add(k[1])

print(f"Resultado X x Y: {r_ordenado}\nOnde o y é 2x + 1")
print(f"Dominio: {dominio}")
print(f"Imagem: {imagem}")
