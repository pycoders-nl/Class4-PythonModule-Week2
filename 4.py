n = input()
m = input()

ortak = ""
nde = ""
mde = ""

for i in n:
    if i in m:
        ortak += i

for i in n:
    if i not in m:
        nde += i

for i in m:
    if i not in n:
        mde += i

print("".join(sorted(ortak)))
print("".join(sorted(nde)))
print("".join(sorted(mde)))
