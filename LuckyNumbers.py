print("--------------------------------------------------------------------------")
print('------------------------------FIND LUCKY NUMBERS---------------------------')
print("--------------------------------------------------------------------------")

n=int(input('Please enter a number to view your lucky numbers?: '))   #kullanicidan bir sayi girmesini istiyoruz.
lucky_list=[i for i in range(1,n+1)]                                  # 1 den kullanicinin girdigi sayiya kadar olan
print(lucky_list)                                                     # sayilari lucky_list adinda listeye koyuyoruz.
x=2
while x < n:                        # while loop unu x in kullanicinin girdigi sayidan kucuk oldugu muddetce donduruyoruz.
    del lucky_list[x-1::x]          # her dondugunde lucky_list ten x-1 den n e kadar x adimla silerek gidiyoruz.
    x+=1                            # x i 1 arttiriyoruz.
    lengh=len(lucky_list)
    if x==lengh-1:                  # eger x listenin uzunlugundan bir azina esit olursa while loop unu sonlandiriyoruz.
        break                       #cunku esit olursa listede index disina cikilmis olur hata verir.
print('Your lucky numbers =  {}'.format(lucky_list))    #en son sansli numaralari yazdiriyoruz.




