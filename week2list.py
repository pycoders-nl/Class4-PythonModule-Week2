n = 2
list_a = [1,2,3,4,5]
list_a[-n:]
list_a[:-n]

n = 2
list_a = [1,2,3,4,5]
a = list_a[-n:] + list_a[:-n]
a

n = -1
list_a = [1,2,3,4,5]
list_a[-n:]

def shiftinglist(list_a, n):
    print(list_a[-n:] + list_a[:-n])

shiftinglist([1,2,3,4,5], -2)

shiftinglist([1,2,3,4,5], 2)