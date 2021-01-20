cumle = str(input(" Please enter a sentence without using punctuation marks: "))

cumle = cumle.lower()
dictionary = {}
for i in range(97, 123):
    dictionary[chr(i)] = 0

for i in cumle:

    dictionary[i] = cumle.count(i)

if dictionary.__contains__(" "):
    ignoreblanks = dictionary.pop(" ")

print("The number of each a letters in the sentence: ")

print(dictionary)
