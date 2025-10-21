'''
Seja A = {x ∈ ℕ | x < 6}, B = {x ∈ ℕ | x é par e x < 6}.
Liste os elementos e determine A – B.
'''

A = {0,1,2,3,4,5}
B = {2,4,6}

simetrica = (A-B).union(B-A)

print(simetrica)