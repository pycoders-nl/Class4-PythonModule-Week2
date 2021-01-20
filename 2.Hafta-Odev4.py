strA = str(input("Kelime_1:"))
strA = strA.lower()

strB = input("Kelime_2:")
strB = strB.lower()

punctuation = "!@#$%^&*()_+<>?:.,;"

for c in strA:
    if c in punctuation:
        strA = strA.replace(c, "")

for c in strB:
    if c in punctuation:
        strB = strB.replace(c, "")

A = set(strA)
B = set(strB)

A_KES_B = list(A.intersection(B))
sorted(A_KES_B)
print("A ve B'de ortak bulunan harfler:")
print([''.join(A_KES_B)])

A_FARK_B = list(A - B)

sorted(A_FARK_B)
print("A'da olup B'de olmayan harfler:")
print([''.join(A_FARK_B)])

B_FARK_A = list(B - A)
print("B'da olup A'de olmayan harfler:")
print([''.join(B_FARK_A)])

print([''.join(A_KES_B)], [''.join(A_FARK_B)], [''.join(B_FARK_A)])








