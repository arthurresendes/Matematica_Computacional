p = True
q = False
r = True
s = True
# ((p ∧ q) V ¬r) <-> s

if ((p and not q) or not r) == s:
    print(True)
else:
    print(False)