metin=input("Lutfen bir cumle yaziniz:")

metin2={}

for i in metin:
    letter={i:metin.count(i)}
    metin2.update(letter)

bosluksil = metin2.pop(' ')

liste = list()

for i in metin2:
 tuple = (str(i), metin2[i])
 liste.append(tuple)

print(liste)
