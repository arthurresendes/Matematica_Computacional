'''
Se U = {a, b, c, d, e, f}, A = {a, c, e}, B = {b, c, d}, determine:
(A’ ∩ B) ∪ (A ∩ B’).
'''

U = {'a', 'b', 'c', 'd', 'e', 'f'}
A = {'a', 'c', 'e'}
B = {'b', 'c', 'd'}

U_semA = U - A
U_semB = U-B

resultado = (U_semA.intersection(B)).union(U_semB.intersection(A))

print(resultado)