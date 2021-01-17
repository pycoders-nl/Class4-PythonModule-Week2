# Write a program that takes two inputs; one of them is a list and the other is a number,
# returns the list obtained by shifting the elements in the list n places to the right (left)
# when n is positive (negative). Use wrap-around: if an element is shifted beyond the end of the list,
# then continue to shift starting at the beginning of the list.
i = 0
liste = list(input("Enter a list: "))           # Enter the sample list
number = int(input("Enter a number: "))         # Enter the number that the list will be shifted
if number > 0:
    listedepo = liste.copy()                    # Copy the original list not to loose the values

    for k in range(number):                     # Visit the numbers for the given times
        for i in range(len(liste)-1):           # Visit all elements of the list
            liste[i+1] = listedepo[i]           # Chane the values of copy list with original in descending order
        liste[0] = listedepo[i+1]               # Assign the last index value to the first index

        listedepo = liste.copy()                # Repeat the commands from the point list remained
    print(str(liste))                           # Print the shifted version

elif number < 0:                                # Same operations for negative value in ascending order
    listedepo = liste.copy()

    for j in range(abs(number)):
        for i in range((len(liste) - 1), 0, -1):
            liste[i - 1] = listedepo[i]
        liste[len(liste) - 1] = listedepo[0]

        listedepo = liste.copy()
    print(liste)

else:                                           # If the shifting number is ZERO, the list will not change
    print(liste)