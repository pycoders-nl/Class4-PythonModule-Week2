# 3.
# Write a code snippet that inputs a sentence from the user,
# then uses a dictionary to summarize the number of occurrences of each letter.
# Ignore case, ignore blanks and assume the user does not enter any punctuation.
# Display a two-column table of the letters and their counts with the letters in sorted order.
#
# Example:
#
# Input >>> "This is a sample text with several words This is more sample text with some different words"
# Output >>> [('a', 4), ('d', 3), ('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o', 4),
# ('p', 2), ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]

text = "This is a sample text with several words This is more sample text with some differentwords"
print("Input >>> ",text)

new_text = text.replace(" ", "").lower() # string deki bosluklari replace() ile ve buyukharfleri upper() ile yok ettim.

d = dict()                               # bos bir dict olusturdum.
for i in new_text:                       # string uzerinde dongu kullandim.
    if i not in d:                       # eger string item i dict de yoksa sarti ekledim
        d[i] = 1                         # string in item ini, dict in key i olarak, ve 1 i value olarak assign ettim.
    else:
        d[i] = d[i] + 1                  # string harfi(item) dict de zaten mevcut ise o key in value suna 1 arttirdim

t = list(d.items())                      # dict yi listeye convert ettim.
t.sort()                                 # listeyi siraladim
print("Output >>> ",t)
