#fibonacci pattern  [0,1,1,2,3,5,8,13,21,34,55]
num = int(input("enter number: "))
n1=0
n2=1
for fab in range(0,num+1):
    nth=n1+n2
    n1=n2
    n2=nth
    
    print(nth)
    