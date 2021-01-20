
cumle=str(input('Bir Cumle Giriniz....:')).replace(" ", "")

valid_characters = 'abcdefghijklmnopqrstuvwxyz1234567890'
cumle1 = ''.join([ x for x in cumle if x.lower() in valid_characters ])
liste= list(cumle1.lower())
from collections import Counter
print(liste)


print('Liste....:',Counter(liste))
print('3.Odev Bitmistir..........')















