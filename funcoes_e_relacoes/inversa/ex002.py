def inverte(r):
    lista_inversa = set()
    dominio = ()
    imagem = ()
    for i in r:
        dominio = i[0]
        imagem = i[1]
        lista_inversa.add((imagem,dominio))
    return lista_inversa

R={(1,2),(2,3),(3,4)}
inverso = inverte(R)
print(inverso)