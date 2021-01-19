# Write a program that takes two inputs
# one of them is a list and the other is a number, and returns the list obtained by shifting the elements in the list n places to the right(left) when n is positive(negative). Use wrap-around: if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list. < br / > < br / >
# Example:
# ```
# Inputs >> > [1, 2, 3, 4, 5], 2
# Output >> > [4, 5, 1, 2, 3]
# Inputs >> > [1, 2, 3, 4, 5], -2
# Output >> > [3, 4, 5, 1, 2]

el = int(input("Enter a number that you want to create a list from 0 until : "))
shift = int(input('How many steps do you want to move your elements : '))


lst = list(range(0, el + 1))

print('Original list is : {}'.format(lst))

lst = lst[-shift:] + lst[:-shift]


print("\n")
print('Your new list is : {}'.format(lst))
