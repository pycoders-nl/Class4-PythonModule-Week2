print("--------------------------------------------------------------------------")
print('------------------------------SHIFTING LIST---------------------------')
print("--------------------------------------------------------------------------")


n=int(input(""                                            # Kullanicidan 1 den kaca kadar liste olusturmasini
                                                          # girmesini istiyoruz ve n variable ina  atiyoruz.
"Do you want to make a list from 1 to what number?: "))

shifting_list=[i for i in range(1,n+1)]               # n e kadar olan sayilari liste seklinde shifting_liste koyuyoruz.
print("Your original list = {}".format(shifting_list))
shift=int(input(""                                    # kac birim ve ne tarafa kaydirmak istedigini 
"How many units do you want to shift?:"               # (- sola,+ saga) soruyoruz ve bu nu shift variable ina atiyoruz               
 " for right=> +  , for left=> - : "))
if shift < 0 :                                        # Girilen shift variable i 0 dan kucukse yani user sola kaydirmak
                                                      # istiyorsa if blogu calisir.
    for i in range(shift*-1):                         #i variable ina shift variable ina kadar calistiriyoruz.
                                                      #-2 girilirse 2 kez calisir.
        shifting_list.append(shifting_list.pop(0))    # pop metodu ile listenin ilk  elemanini (index=0 )silip
                                                      # append metodu ile de sildigimiz elemani listenin sonuna ekliyoruz.

    print("Your shifting list = {}".format(shifting_list)) # kaydirilmis olan listeyi print yapiyoruz.
else:
    for i in range(shift):
        shifting_list.insert(0,shifting_list.pop(-1))   # pop ile listenin son elemanini alip (index=-1)
                                                        # insert ile de sildigimiz elemani listeni basina (index=0) koyuyoruz.

    print("Your shifting list = {}".format(shifting_list))  # kaydirilmis olan listeyi print yapiyoruz.