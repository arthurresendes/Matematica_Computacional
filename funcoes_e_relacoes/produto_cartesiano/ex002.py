#Se C = {a, b, c} e D = {1, 2}, quantos elementos tem C × D

c={'a','b','c'}
d = {1,2}

res = {('a',1),('a',2),('b',1),('b',2), ('c',1), ('c',2)}
total = len(c) * len(d)
print(f"O resultado de AxB é {res} com {total} resultados possiveis")