def produto_cartesiano(a,b):
    lista_set = set()
    for i in a:
        for j in b:
            lista_set.add((i,j))
    ordenada = sorted(lista_set)
    return ordenada

A = [0,2,4,6]
B = [1,3,5]
print(produto_cartesiano(A,B))