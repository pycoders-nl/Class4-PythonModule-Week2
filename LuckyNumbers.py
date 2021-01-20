
n= (input('Bir sayi giriniz:'))
n= int(n)
list1= list(range(1,n+1))
print(list1)

for i in range(1,n):
    if len(list1) > i:
        del list1[i::i+1]   #kumulatif ayiklama yapiyoruz, her seferinde 'del' ile, 2,3,4ncu...sayilari secerek eleme yapiyor,
                             # del ile listemiz otomatik eksiltilerek her stepte guncellenmis oluyor
        print (list1)

if len(list1) < i+1:        # bu asamada atlayacagi sayi, listedeki toplam sayiyi astigi icin eleme duruyor, sansli sayilara ulasmis oluyoruz
        print("Lucky Numbers are", list1)
        print("Total Number of Lucky Numbers :",len(list1))