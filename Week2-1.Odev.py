liste=list(range(1,23))

print('orjinal liste=',liste)
j=2
k=1

for i in liste:

    del liste[k:23:j]
    print('liste {}='.format(k),liste)
    j+=1
    k+=1























