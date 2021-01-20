number = input("type a number. press enter to end: ")
number_list = []
while number != "":
    number_list.append(int(number))
    number = input("type a number: ")
    
shifter = int(input("type a shifter number: "))

shifter *= -1
leftFirst = number_list[0: shifter]
leftSecond = number_list[shifter:]
print(leftSecond + leftFirst)
