#Se A = {1, 2} e B = {3, 4, 5}, determine A × B.
a = {1,2}
b = {3,4,5}

res = {(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)}

total = len(a) * len(b)

print(f"O resultado de AxB é {res} com {total} resultados possiveis")