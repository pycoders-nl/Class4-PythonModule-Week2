
listem = list(input("Lutfen listenizin elemanlarini bitisik sekilde giriniz: "))

o = int(input("Lutfen listeyi ne kadar oteleyecigimizi giriniz: "))
b = len(listem)
a = b - o

if o > 0:
    lst2 = list(listem[a:b])
    print(lst2)
    del listem[a:b]
    lst3= lst2 + listem
    print(lst3)
elif o < 0:
    o = -1 * o
    lst2 = list(listem[0:o])
    print(lst2)
    del listem[0:o]
    lst3= listem + lst2
    print(lst3)
else:
    print("Lutfen baska bir sayi giriniz: ")