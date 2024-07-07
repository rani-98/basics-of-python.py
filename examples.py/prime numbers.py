#prime number b/w 1-100    ----1,2,3,7,11,13,17,19,23.....
n=range(1,20)
def prime(n):
    for x in range(2,n):
        if (n%x)==0:
          return False
    return True
pri=list(filter(prime,n))
print(pri)
        
