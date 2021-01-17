# Write a programme to generate the lucky numbers from the range(n).
# These are generated starting with the sequence s=[1,2,...,n].
# At the first pass, we remove every second element from the sequence, resulting in s2.
# At the second pass, we remove every third element from the sequence s2, resulting in s3,
# we proceed in this way until no elements can be removed.
# The resulting sequence are the numbers lucky enough to have survived elimination.

i = 0
newlist = []                                # Creating an empty list
sayi = int(input("Enter a number:"))
for x in range(1, sayi + 1):                # Visit the number from 1 to end
    newlist.append(x)                       # Adding elements to the list
print("Original source     : ", newlist)    # Printing original list

for x in newlist:                           # All the elements of newlist will be visited
    del newlist[i + 1: sayi: i + 2]         # Target indexes will be deleted
    if len(newlist) >= i + 2:               # Cheking if there is more number to be erased
        print("Remove the", i + 2, "elemets: ", newlist)    # Remained numbers will be printed
        i = i + 1
print("We cannot remove every other", i + 2, "th element as there is no", i + 2, ". element.")
