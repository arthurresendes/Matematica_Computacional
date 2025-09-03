A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
uniao = A.union(B)
print(uniao)
intersecao = A.intersection(B)
print("Diferença A - B:", A - B)
print("Diferença B - A:", B - A)
print(intersecao)
print("Diferença Simétrica:", A ^ B)


x = int(input("Digite um valor: "))
if x in A and B:
    print(f"{x} esta no conjunto {A} | {B} A e B")
elif x in A:
    print(f"{x} esta no conjunto {B} A")
elif x in B:
    print(f"{x} esta no conjunto {B} B")
else:
    print(f"X não esta em nenhum conjunto")