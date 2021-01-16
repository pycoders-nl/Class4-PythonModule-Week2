i=0
newlist = []
sayi = int(input("Enter a number:"))
for x in range(1, sayi+1):                  # Creating the desired list
    newlist.append(x)
print("Original source     : ", newlist)    # Printing original list

for x in newlist :                          # All the elements of newlist will be visited
    del newlist[i+1:sayi:i+2]           # Target indexes will be deleted
    if len(newlist) >= i+2 :            # There is more number to be erased
        print("Remove the", i+2, "elemets: ", newlist)      # Remained numbers will be printed
        i=i+1
print("We cannot remove every other", i + 2, "th element as there is no", i + 2, ". element.")


