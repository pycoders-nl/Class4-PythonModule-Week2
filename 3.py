"""
Kullanıcıdan bir cümle giren bir kod parçacığı yazın,
ardından her harfin geçtiği sayıları özetlemek için bir sözlük kullanın.
Büyük/küçük harfleri yoksayın, boşlukları yok sayın ve kullanıcının herhangi bir noktalama işareti girmediğini varsayın.
Harflerin iki sütunlu bir tablosunu ve sayılarını harflerle birlikte sıralı olarak görüntüleyin.

Ornegın:
Input >>> "This is a sample text with several words This is more sample text with some differentwords"
Output >>> [('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1),
            ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]
"""

cumle = str(input('Bir Cumle Giriniz....:')).replace(" ", "")
cumle = cumle.replace(" ", "").lower()    # cümleden boslukları kaldırıp buyuk harfler kucuk yapıldı
cumle1 = ''.join([x for x in cumle])
print('Cümle        :', cumle1)

from collections import Counter
tablo = Counter(cumle1)
print('Harf Tablosu :', tablo)
