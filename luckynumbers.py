
n=int(input("Input a Number: "))
x,y=list(range(1,n+1)),2
while(y<=len(x)):
    x = [x[i] for i in range(0, len(x)) if (i == 0) or ((i + 1) % y) > 0]
    y += 1
print("lucky numbers are ",x)

