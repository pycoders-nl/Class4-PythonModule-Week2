"""
Write a program that takes two inputs;
one of them is a list and the other is a number,
and returns the list obtained by shifting the elements in the list n places
to the right (left) when n is positive (negative).
Use wrap-around: if an element is shifted beyond the end of the list,
then continue to shift starting at the beginning of the list.

Example:

Inputs>>> [1, 2, 3, 4, 5], 2
Output>>> [4, 5, 1, 2, 3]
Inputs>>> [1, 2, 3, 4, 5], -2
Output>>> [3, 4, 5, 1, 2]
"""
print("***************************************************************\n"
      "*** Oluşturulan listeyi istenilen kadar saga sola kaydırma  ***\n"
      "***************************************************************")
x = int(input('1 den başlayarak oluşturulacak liste uzunlugunu giriniz:'))

liste = list(range(1, x+1))
print('Oluşturulan liste kacıncı elemandan sonra kaydırılsın?')
k = int(input('sağa kaydırma için "+" , sola kaydırma için "-" sayı yazınız :'))
print('Olusturulan ilk liste            :', liste)

if k > 0:                           # kaydırma degeri pozitifse
    while k > 0:
        kes = liste.pop()           # listenin son elemanını kesip alınır
        liste.insert(0, kes)        # kesilip alınan eleman listenin başına eklenir
        k -= 1
else:
    while k < 0:                    # kaydırma degeri negatifse
        kes = liste.pop(0)          # listenin ilk elemanını kesip alınır
        liste.append(kes)           # kesilip alınan eleman listenin sonuna eklenir

        k += 1

print('Kadırma sonucu olusan Yeni Liste :', liste)
