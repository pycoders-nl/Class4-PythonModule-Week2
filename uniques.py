word1 = input("enter the first word: ")
word2 = input("enter the second word: ")

word1_set = set((word1.lower()).replace(" ", ""))
word2_set = set((word2.lower()).replace(" ", ""))

shared = ''.join(sorted(word1_set.intersection(word2_set)))
dif_word1 = ''.join(sorted(word1_set.difference(word2_set)))
dif_word2 = ''.join(sorted(word2_set.difference(word1_set)))

groupping = [shared, dif_word1, dif_word2]

print(groupping)