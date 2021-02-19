kelime = input('Bir kelime giriniz: ')
kelime = kelime.lower()
list = 'abcçdefgğhıijklmnoöpqrsştuüvwxyz0123456789'
a = {}
for i in kelime:
    if i in list:
        a[i] = kelime.count(i)
               

print ('{}' ": {}".format(kelime, str(a)))