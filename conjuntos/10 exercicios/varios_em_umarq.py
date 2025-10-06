A = {1,2,3,4,5,6}
B = {5,6,7,8,9,10}
print(f"União: {A.union(B)}\nIntersecção: {A.intersection(B)}\nA e não em B: {A-B}")

A = {6,7,8}
if A.issubset(B):
    print("A é subconjunto de B")
else:
    print("A não é subconjunto de B")