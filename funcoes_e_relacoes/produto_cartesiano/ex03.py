# Escreva os elementos de A × B, onde A = {x | x < 3, x ∈ ℕ} e B = {a, b}

a = {0,1,2}
b = {'a','b'}

res = {(0,'a'), (0,'b'),(1,'a'),(1,'b'),(2,'a'),(2,'b')}
total = len(a) * len(b)
print(f"O resultado de AxB é {res} com {total} resultados possiveis")