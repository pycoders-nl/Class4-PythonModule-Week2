# 2.
# Write a program that takes two inputs; one of them is a list and the other is a number,
# and returns the list obtained by shifting the elements in the list n places to the right (left)
# when n is positive (negative). Use wrap-around: if an element is shifted beyond the end of the list,
# then continue to shift starting at the beginning of the list.
# Example:
# Inputs>>> [1, 2, 3, 4, 5], 2
# Output>>> [4, 5, 1, 2, 3]
# Inputs>>> [1, 2, 3, 4, 5], -2
# Output>>> [3, 4, 5, 1, 2]

n = int(input("Enter a number to create a list: ")) # liste icin ilk input u aldim ve integer yaptim.
aList = [i for i in range(1, n + 1)]                # liste olusurdum.
print("Inputs>>> ",aList, end="")                   # istenen formatta ekrana yazdirdim.
n2 = int(input(" enter the other number: "))        # ikinci inputu aldim ve integer yaptim
newList1 = []                           # listeleri concatenate ile birlestirmek icin 3 yeni bos liste assign ettim.
newList2 = []
result=[]
if n2>0:                                # ikinci input sifirdan buyukse bu if bloguna girsin.
    newList1 = aList[-n2::]             # ikinci input ile alinan sayiyi kullanarak liste sonuna kadar slice yaptim.
    newList2 = aList[:-n2]              # bastan ikinci input ile alinan sayiya kadar slice yaptim.
    result=newList1+newList2            # iki listeyi concatenate ile birlestirdim.
    print("Output>>> ",result)
else:                                   # ikinci input sifirdan buyuk degilse (kucukse) bu bloga girsin
    newList1 = aList[:-n2]              # bastan ikinci input ile alinan sayiya kadar slice yaptim.
    newList2 = aList[-n2:]              # ikinci input ile alinan sayiyi kullanarak liste sonuna kadar slice yaptim.
    result = newList2 + newList1        # iki listeyi concatenate ile birlestirdim.
    print("Output>>> ",result)          # istenen sonucu ekrana yazdirdim.



