print("@@@Sansli sayilari bulma programina;Hosgeldiniz@@@")
x = int(input("Lutfen bir deger giriniz: x=> "))

main_list = list(range(1,x+1))

i = 2

while True:
    if i < len(main_list):
        del main_list[i-1:x:i]
        i += 1

    else:
        print(">>>Sizi gidi sanslilar :))) <<< {}".format(main_list))
        break