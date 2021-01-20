
ham= (input('Bir cumle giriniz:'))
cumle= ham.lower()               #Farkli hesaplamayi onlemek icin, buyuk harfleri kucuk harfe ceviriyoruz
print ('Cumleniz :', cumle)
freq = {}
for char in cumle:
   if char ==' ' or char=='?' or char=="'"or char=='"':   # istemedigimiz karakterleri hesaplama 'if'ine sokmuyoruz, ayiriyoruz
       continue
   if char in freq:
      freq[char] += 1
   else:
      freq[char] = 1

# Sonuc Gosterme,
print ('{}' "  cumlesindeki karakter frekanslari :\n {}".format(cumle, str(freq)))

