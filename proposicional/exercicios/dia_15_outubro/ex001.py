'''
(p ∧ q) → ¬r
p: “Estudo lógica.”
q: “Faço exercícios.”
r: “Tiro notas ruins.”
➜ Monte a tabela verdade e diga se a proposição é tautologia, contradição ou contingência.

'''

print("p | q | r | p ∧ q | ¬r | (p ∧ q) → ¬r")
print("V | V | V | V     | F  | F")
print("V | V | F | V     | V  | V")
print("V | F | V | F     | F  | V")
print("V | F | F | F     | V  | V")
print("F | V | V | F     | F  | V")
print("F | V | F | F     | V  | V")
print("F | F | V | F     | F  | V")
print("F | F | F | F     | V  | V")

print("É uma contingencia")
