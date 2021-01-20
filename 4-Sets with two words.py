kelime1 = "teacher"
kelime2 = "student"

kelime1_karakter_kumesi = set()
kelime2_karakter_kumesi = set()

for karakter in kelime1:
    kelime1_karakter_kumesi.add(karakter)
for karakter in kelime2:
    kelime2_karakter_kumesi.add(karakter)

kelime1_kelime2_kesisim = kelime1_karakter_kumesi & kelime2_karakter_kumesi
kelime1_fark_kelime2 = kelime1_karakter_kumesi - kelime2_karakter_kumesi
kelime2_fark_kelime1 = kelime2_karakter_kumesi - kelime1_karakter_kumesi


print(kelime1_karakter_kumesi)
print(kelime2_karakter_kumesi)
print(kelime1_kelime2_kesisim)
print(kelime1_fark_kelime2)
print(kelime2_fark_kelime1)


#print(sorted(set({"a","p","p","l","e"})))