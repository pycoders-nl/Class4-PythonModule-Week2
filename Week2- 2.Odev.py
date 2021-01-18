list1=list(range(1,6))
print('liste=',list1)

print('Yukaridaki verilen listeye gore Degismesini istediginiz yerlerin baslangic'
      ' degerini giriniz...... ')

deger=int(input('Bir deger giriniz:'))


k=deger
if k>0:
    while k > 0:
        cikarilan=list1.pop()
        list1.insert(0, cikarilan)


        k -= 1
else:
    while k<0:
        cikarilan=list1.pop(0)
        list1.append(cikarilan)

        k +=1
print('Tebrikler Liste Tamamlandi Assagidaki Gibidir........')
print('Yeni Liste=',list1)



