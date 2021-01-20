# 4.
# Write a program that takes in two words as input and returns a list containing three elements, in the following order:
# Shared letters between two words.
# Letters unique to word 1.
# Letters unique to word 2.
# Each element of the output should have unique letters, and should be alphabetically sorted.
# Use set operations. The strings will always be in lowercase and will not contain any punctuation.
# Example:
# Input1>>> "sharp"
# Input2>>> "soap"
# Output>>> ['aps', 'hr', 'o']

word1=input("enter a 1.word: ")
word2=input("enter a 2.word: ")
s1 = set(word1)             # 1.kelimeyi set e convert ettim.
s2 = set(word2)             # 2.kelimeyi set e convert ettim.

k = s1.intersection(s2)     # Shared letters between two words. | print(s1&s2)
klist = list(k)             # kesisim set ini list e convert ettim.
klist.sort()                # listeyi sort ettim.
str1 = ''.join(klist)       # listenin item lerini str e convert ettim.

f1 = s1.difference(s2)      # s1 fark s2. | print(s1-s2)
flist1 = list(f1)           # f1 set ini list e convert ettim.
flist1.sort()               # listeyi sort ettim.
str2 = ''.join(flist1)      # listenin item lerini str e convert ettim.

f2 = s2.difference(s1)      # s2 fark s1. | print(s2-s1)
flist2 = list(f2)           # f2 set ini list e convert ettim.
flist2.sort()               # listeyi sort ettim.
str3 = ''.join(flist2)      # listenin item lerini str e convert ettim.

result_list = [str1, str2, str3]    # olusan resultlari bir listede topladim.
print(result_list)