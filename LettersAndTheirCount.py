print("---------------------------------------------------------------------------------")
print('------------------------------LETTERS AND THEIR COUNT---------------------------')
print("----------------------------------------------------------------------------------")


n=input("Enter the number of letters you wonder : ")   # input ile user dan hangi cumlenin harflerini
                                                       # saymasini istiyorsa o cumleyi aliyoruz. Buyuk harf bosluk yok
letters_numbers_dict={}                                #bir tane bos dictionary ve list olusturuyoruz.
letters_numbers_list=[]
x=0
while x < len(n):                                      # n in x ten buyuk oldugu mutdetce
                                                       # donen bir while loop u olusturuyoruz.
    letters_numbers_dict[n[x]]=n.count(n[x])           #bos dictionary nin icine n nin x inci indexini ve
                                                       # x indexindeki degerin n de kacdefa gectigini atiyoruz.
    letters_numbers_list.append(letters_numbers_dict.popitem())#bos diktionary e gonderilen key ve
                                                       # value yi popitem metodu ile listeye append metodu ile ekliyoruz
    x+=1
output_list=[]                                         # ekranda gosterilecek output listesini  olusturuyoruz.
for i in letters_numbers_list:                         #for ile icinde harflerin ve sayilarinin oldugu
                                                       # listeyi donguye sokuyoruz
    if i not in output_list:                           # bir harfin birden fazla yazmasini istemiyoruz. if kosulu ile
                                                       # bir harfin bir kere yazilmasini sagliyoruz.
        output_list.append(i)
print("LETTERS AND THEIR COUNT= \n {}".format(output_list))  # ve output u print ediyoruz.