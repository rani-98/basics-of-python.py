
rows=6
for i in range(rows):
    print(i*"1 ")

rows=5
for i in range(rows):
    for j in range(i):
        print(i,end=' ')
    print(' ')


rows=7
b=0
for i in range(rows,0,-1):
    b +=1
    for j in range(1,i+1):
        print(b, end=' ')
    print(' ')

     
# multiplication table pattern
rows=10
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i*j, end='  ')
    print('')
    


