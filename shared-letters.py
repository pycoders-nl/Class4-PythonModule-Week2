word1 = set(input('Enter first word : '))
word2 = set(input('Enter second word : '))

letters = [''.join(sorted(word1.intersection(word2))),
           ''.join(sorted(word1.difference(word2))),
           ''.join(sorted(word2.difference(word1)))]

print(letters)
