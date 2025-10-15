'''
Se A ⊂ B e B ⊂ C, o que se pode afirmar sobre A e C?

Que A pertence a C
'''

A = {1,2}
B = {1,2,3}
C = {1,2,3,4,5}
a_subset_b = "A é subconjunto de B" if A.issubset(B) else "Não é"
b_subset_c = "B é subconjunto de C" if B.issubset(C) else "Não é"
a_subset_c = "A é subconjunto de C" if A.issubset(C) else "Não é"
print(a_subset_b)
print(b_subset_c)
print(a_subset_c)