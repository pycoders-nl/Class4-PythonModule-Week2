
sayilar_list = []
n = int(input("n:"))
for i in range(1, n+1):
    sayilar_list.append(i)
print(sayilar_list)
i = 2
while i < len(sayilar_list):
    del sayilar_list[i-1:n:i]
    print("Remove the", i, "elements: ", sayilar_list)
    i += 1
else:
    print("Lucky numbers are: {}".format(sayilar_list))
