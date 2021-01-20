#Soruda defaatle yanlis komutlar var, ornek de dogru degil.

import math

n = int(input())
s = [x+1 for x in range(n)]

for x in range(0,int(math.ceil(len(s)/2))):
    del s[x+1]
    print(x+1)
    
print(s)
