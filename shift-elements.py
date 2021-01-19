el = int(input("Enter a number that you want to create a list from 0 until : "))
shift = int(input('How many steps do you want to move your elements : '))


lst = list(range(0, el + 1))

print('Original list is : {}'.format(lst))

lst = lst[-shift:] + lst[:-shift]


print("\n")
print('Your new list is : {}'.format(lst))
