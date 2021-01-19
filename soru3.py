# Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize
# the number of occurrences of each letter. Ignore case, ignore blanks and assume the user does not enter
# any punctuation. # Display a two-column table of the letters and their counts with the letters in sorted order.

d = {}                                  # Creating an empty set
sentence = input("Enter a sentence: ")  # Receiving user's input
lower = sentence.lower()                # Convert to the lowercase if not
print(sentence)                         # Print the original sentence

for i in lower:                         # Visit all the members
    if i == " ":                        # Omit the spaces
        continue
    d[i] = lower.count(i)               # Count the each different character
print(sorted(d.items()))                # Print key and value couples in alphabetical order