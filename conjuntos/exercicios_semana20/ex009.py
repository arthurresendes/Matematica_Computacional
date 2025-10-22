U = {1,2,3,4,5,6,7,8,9,10}
A = {1,2,3,4,5,6}
B = {4,5,6,7,8,9}
print(U-A)
print(U-B)
simetrica = (A-B).union(B-A)
print(simetrica)