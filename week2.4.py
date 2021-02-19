

word1= input("ilk kelimeyi giriniz: ").lower()
word2= input("ikinci kelimeyi giriniz:").lower()


a=''.join(sorted(set(word1).intersection(word2)))
b = ''.join(sorted(set(word1).difference(set(word2))))
c = ''.join(sorted(set(word2).difference(set(word1))))
print([a,b,c])

