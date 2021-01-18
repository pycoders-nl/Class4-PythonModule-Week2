#!/usr/bin/env python
# coding: utf-8

# # 1 Lucky Numbers
# Write a programme to generate the lucky numbers from the range(n). These are generated starting with the sequence s=[1,2,...,n]. At the first pass, we remove every second element fromthe sequence, resulting in s2. At the second pass, we remove every third element from the sequence s2, resulting in s3, and we proceed in this way until no elements can be removed. The resulting sequence are the numbers lucky enough to have survived elimination.
The following example describes the entire process for n=22:

Original sequence: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
Remove 2nd elements: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] 
Remove 3rd elements: [1, 3, 7, 9, 13, 15, 19, 21] 
Remove 4th elements: [1, 3, 7, 13, 15, 19] 
Remove 5th elements: [1, 3, 7, 13, 19]
We cannot remove every other 6th element as there is no 6th element.
Input>>> 22 
Output>>> Lucky numbers are [1, 3, 7, 13, 19]
# In[ ]:


n = int(input("n: "))
numbers = list(range(1,n+1))
i=2
while i < len(numbers):
 del numbers[i-1:n:i]
 i += 1
 n = max(numbers)
else:
 print("The lucky numbers are: {}".format(numbers))   


# # 2 Index kaydirma
Write a program that takes two inputs; one of them is a list and the other is a number, and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative). Use wrap-around: if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.

Example:

Inputs>>> [1, 2, 3, 4, 5], 2
Output>>> [4, 5, 1, 2, 3] 
Inputs>>> [1, 2, 3, 4, 5], -2 
Output>>> [3, 4, 5, 1, 2]
# In[ ]:


lst = list(input("Lutfen listenizin elemanlarini sade ve bitisik sekilde giriniz: "))

s = int(input("Lutfen listenin ogelerini kaydirmak istediginiz olcu miktarini giriniz: "))
y = len(lst)
x = y - s

if s > 0:
    lst2 = list(lst[x:y])
    print(lst2)
    del lst[x:y]
    lst3= lst2 + lst
    print(lst3)
elif s < 0:
    s = -1 * s
    lst2 = list(lst[0:s])
    print(lst2)
    del lst[0:s]
    lst3= lst + lst2
    print(lst3)
else:
    print("Lutfen baska bir sayi giriniz: ")
    
    


# # 3 Cumledeki harflerin sayisi
Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize the number of occurrences of each letter. Ignore case, ignore blanks and assume the user doesnot enter any punctuation. Display a two-column table of the letters and their counts with the letters in sorted order.

Example:

Input >>> "This is a sample text with several words This is more sample text with some differentwords" 
Output >>> [('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)] 
# In[6]:


b = str(input("Lutfen noktalam isareti kullanmadan bir cumle giriniz: "))

b = b.lower()

dicti={}

for i in b:
    x = {i:b.count(i)}
    dicti.update(x)
    
boslukat = dicti.pop(' ')

print("Cumledeki harflerin kullanim sayisi: ")

print(dicti)


# # 4 Unique letters
Write a program that takes in two words as input and returns a list containing three elements, in the following order:

Shared letters between two words.
Letters unique to word 1.
Letters unique to word 2.
Each element of the output should have unique letters, and should be alphabetically sorted. Useset operations. The strings will always be in lowercase and will not contain any punctuation.

Example:

Input1>>> "sharp" 
Input2>>> "soap" 
Output>>> ['aps', 'hr', 'o']
# In[ ]:


a = set(input("Lutfen bir kelime yaziniz: "))
b = set(input("Lutfen ikinci bir kelime yaziniz: "))

# sorted intersection

print("Birinci harf kumemiz: {}".format(a))
print("Ikinci harf kumemiz: {}".format(b))

c = list(a.intersection(b))
c.sort()
print("Shared letters between two words: {}".format(c))
x = ""
for k in c:
    x += str(k)
    x = x.lower()

# unique 1
d = list(a-b)
d.sort()
print("Letters unique to word 1: {}".format(d))
y = ""
for m in d:
    y += str(m)
    y = y.lower()
    
# unique 2
e = list(b-a)
e.sort()
print("Letters unique to word 2: {}".format(e))
z = ""
for n in e:
    z += str(n)
    z = z.lower()
    
print("-----Result-----: ")

print("['{}','{}','{}']".format(x,y,z))

