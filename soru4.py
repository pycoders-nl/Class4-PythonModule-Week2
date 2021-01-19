# Write a program that takes in two words as input and returns a list containing three elements,
# Shared letters between two words.
# Letters unique to word 1.
# Letters unique to word 2.
# Each element of the output should have unique letters, and should be alphabetically sorted.
# Use set operations. The strings will always be in lowercase and will not contain any punctuation.

first_word = input("enter first word :").lower()                        # Getting the first string
second_word = input("enter second word:").lower()                       # Getting the second string
if (first_word.isalpha()) == False or (second_word.isalpha()) == False: # If any forbidden character is entered
    print("Please enter only letters")                                  # Program will be terminated with a messsage

else:
    a = sorted(set(first_word) & set(second_word))      # Convert to set type and intersection opeartion
    a = "".join(a)                                      # Convert to string back for the desired output
    b = sorted(set(first_word) - set(second_word))      # Convert to set type and set difference opeartion
    b = "".join(b)                                      # Convert to string back for the desired output
    c = sorted(set(second_word) - set(first_word))      # Convert to set type and set difference opeartion
    c = "".join(c)                                      # Convert to string back for the desired output
    print(a.split() + b.split() + c.split())            # Output as it is asked in the question

