# Write a program that takes in two words as input and returns a list containing three elements, in the following order: < br / >
# - Shared letters between two words.
# - Letters unique to word 1.
# - Letters unique to word 2. < br / >

# Each element of the output should have unique letters, and should be alphabetically sorted. Useset operations. The strings will always be in lowercase and will not contain any punctuation. < br / > < br / >
# Example:
# ```
# Input1 >> > "sharp"
# Input2 >> > "soap"
# Output >> > ['aps', 'hr', 'o']
# ```

word1 = set(input('Enter first word : '))
word2 = set(input('Enter second word : '))

letters = [''.join(sorted(word1.intersection(word2))),
           ''.join(sorted(word1.difference(word2))),
           ''.join(sorted(word2.difference(word1)))]

print(letters)
