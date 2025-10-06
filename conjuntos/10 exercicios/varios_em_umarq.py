A = {1,2,3,4,5,6}
B = {5,6,7,8,9,10}
print(f"União: {A.union(B)}\nIntersecção: {A.intersection(B)}\nA e não em B: {A-B}")

A = {6,7,8}
if A.issubset(B):
    print("A é subconjunto de B")
else:
    print("A não é subconjunto de B")

A = {1,2,3,4,5,6}
B = {5,6,7,8,9,10}
U =  A.union(B)
print(U)
complementar = U - A
print(complementar)

intersec = A.intersection(B)
A = A - intersec
B = B - intersec
print(A,B)
U = A.union(B)


print(f"Qtd elementos em A: {len(A)}\nQtd elementos em B: {len(B)}\nQtd elementos em U: {len(U)}")

A = {1,2,3,4}
B = {3,4,5,6}
C = {4,6,8}

U1 = A.union(B)
U2 = B.union(C)
UT = U1.union(U2)
print(UT)

intersec = A.intersection(B)
print(intersec)
print(intersec-C)