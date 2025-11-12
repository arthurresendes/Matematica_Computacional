def produto_cartesiano(a,b):
    lista_set = set()
    for i in a:
        for j in b:
            lista_set.add((i,j))
    return lista_set

A = [2,3,4]
B = [4,5]
print(produto_cartesiano(A,B))