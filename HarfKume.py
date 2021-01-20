
print ('2 kelime giriniz...')
kelime1 = input ('kelime1=' )
kelime2 = input ('kelime2=' )

isim=kelime1.lower()
isim2=kelime2.lower()


harfler=set(isim)
harfler1=set(isim2)
harfler2= sorted(list(harfler & harfler1))
harfler3= sorted(list(harfler - harfler1 ))
harfler4= sorted(list(harfler1 - harfler))
harfler5= (''.join(harfler2))
harfler6= (''.join(harfler3))
harfler7= (''.join(harfler4))
print (harfler)
print (harfler1)
print (harfler2)
print (harfler3)
print (harfler4)
print (''.join(harfler2))
print (''.join(harfler3))
print (''.join(harfler4))
Final=[harfler5, harfler6, harfler7]
print (Final)

