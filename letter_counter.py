import string

sentence = input("type a sentence: ").replace(" ", "").lower()
dic = {}

for letter in sentence:
    if letter not in string.punctuation:
        dic[letter] = sentence.count(letter)

dic_items = sorted(dic.items())

print(dic_items)