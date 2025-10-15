"""
Dado U = {1,2,3,4,5,6,7,8,9,10}, A = {2,4,6,8,10}, B = {1,2,3,4,5}, calcule:
a) A′ (complementar de A)
b) (A′ ∩ B)
"""

U = {1,2,3,4,5,6,7,8,9,10}
A = {2,4,6,8,10}
B = {1,2,3,4,5}

letra_a = U-A
print(letra_a)  
letra_b = letra_a.intersection(B)
print(letra_b)