A=[1,2,3,4,5]
k=int(input("Lutfen elemanlari kaydirmak istediginiz degeri giriniz:"))

n=len(A)
C=[None] * n

for i in range(n):
    newIndex = (i + k) % n
    C[newIndex] = A[i]

print(C)













