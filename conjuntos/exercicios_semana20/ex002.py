'''
Seja A = {x | x é número par menor que 10}, B = {x | x é múltiplo de 3 menor que 10}.
Determine A ∩ B e A ∪ B.
'''

A = {2,4,6,8}
B = {3,6,9}

uniao = A.union(B)
intersec = A.intersection(B)
print(uniao)
print(intersec)