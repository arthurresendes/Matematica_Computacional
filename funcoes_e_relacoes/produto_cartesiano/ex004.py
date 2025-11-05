# Determine A × B e B × A para A = {1, 2} e B = {x, y}. São iguais?

a = {1,2}
b = {'x', 'y'}

resAB = {(1,'x'),(1,'y'), (2,'x'),(2,'y')}
resBA = {('x',1),('x',2), ('y',1),('y',2)}

if resAB == resBA:
    print("São iguais")
else:
    print("Não são iguais")

#  Nao sao pq o valor de x e y tem que ser iguais e nesse caso os valores se invertes