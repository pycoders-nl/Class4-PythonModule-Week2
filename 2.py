# Best way to get an input, with columns and comas...
#Inputs>>> [1, 2, 3, 4, 5], 2
#Output>>> [4, 5, 1, 2, 3] 
#Inputs>>> [1, 2, 3, 4, 5], -2 
#Output>>> [3, 4, 5, 1, 2]

# Ill consider inputs would be without unnecessary items but numbers

# btw where is the lenght of the list, its totally a disaster

numbers = list(map(int, input().split()))
shift = numbers.pop()
n = len(numbers)
solution = [numbers[(x + shift) % n] for x in range(n)]
print(solution)
