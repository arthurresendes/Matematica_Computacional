p =  input("Digite true ou false para p: ").lower()
if p == 'true':
    p = True
else:
    p = False

q =  input("Digite true ou false para q: ").lower()
if q == 'true':
    q = True
else:
    q = False

if p and q:
    print("True , p e q não são verdadeiros")
else:
    print('False , p e q são diferentes')

if p == True and q == False:
    print("Se p entao q é falso")
else:
    print("True, p e q são V no se entao")

if p == q:
    print("E bicondicional")
else:
    print("Não é bicondicional")

negacao_p = not p
print(f"Ngeacao de p: {negacao_p}")