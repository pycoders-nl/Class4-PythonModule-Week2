print("---------------------------------------------------------------------------------")
print('------------------------------SHARED LETTERS-------------------------------------')
print("----------------------------------------------------------------------------------")


n=input("Enter first word : ")         # user dan birinci kelimeyi istiyoruz.
x=input("Enter second word : ")        # user dan ikinci kelimeyi istiyoruz.
output_list=[]
n_set=set(n)                           # userdan alinan string ifadeyi set metodu ile set e ceviriyoruz
x_set=set(x)
a,b,c="","",""                         #set lerin kesisim ve farklarini eklemek icin 3 tane bos string olusturuyoruz.

for i in sorted(n_set.intersection(x_set)): # iki set in kesimini sirlayip a stringine toplayarak goderiyoruz.
    a+=str(i)
for i in sorted(n_set.difference(x_set)):   # n-x  i siralayip b stringine toplayarak gonderiyoruz.
    b+=str(i)
for i in sorted(x_set.difference(n_set)):   # x-n  i siralayip b stringine toplayarak gonderiyoruz.
    c+=str(i)

output_list.append(a)                       # en son hazir olan stringleri outout_liste append ediyoruz.
output_list.append(b)
output_list.append(c)                       # ve output_list i print ediyoruz.
print("1. word & 2. word , 1.word difference 2.word , 2.word difference 1.word =>>\n {}".format(output_list))
