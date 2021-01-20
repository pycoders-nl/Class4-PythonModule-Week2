
kelime_1=str(input('Lutfen Ilk Kelimeyi Giriniz.......:').replace(" ", ""))
kelime_2=str(input('Lutfen Ikinci Kelimeyi Giriniz....:').replace(" ", ""))

valid_characters = 'abcdefghijklmnopqrstuvwxyz1234567890'
kelime1 = ''.join([ x for x in kelime_1 if x.lower() in valid_characters ])

ilkkelime= set(kelime1.lower())


valid_characters = 'abcdefghijklmnopqrstuvwxyz1234567890'
kelime2 = ''.join([ x for x in kelime_2 if x.lower() in valid_characters ])
ikincikelime= set(kelime2.lower())






from collections import Counter
print('Girilen Ilk Kelimenin Harfleri.............:',sorted(ilkkelime))
print('Girilen Ikinci Kelimenin Harfleri..........:',sorted(ikincikelime))
print('Ilk Girilen Kumenin Ikinci Girilenden Farki:',ilkkelime.difference(ikincikelime))
print('Ikinci Girilen Kumenin Ilk Girilenden Farki:',ikincikelime.difference(ilkkelime))
print('Ilk ile Ikinci Kumenin Kesisimi............:',ilkkelime.intersection(ikincikelime))










