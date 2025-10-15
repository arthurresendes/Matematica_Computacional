'''
A = {a, b, c}, B = {b, c, d}, C = {c, d, e}
➜ Determine (A ∪ B) ∩ C.
'''

A = {'a', 'b', 'c'}
B = {'b', 'c', 'd'}
C = {'c', 'd', 'e'}

uniao = A.union(B)
result = uniao.intersection(C)
print(result)