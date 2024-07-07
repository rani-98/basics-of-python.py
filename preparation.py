# print 50 odd numbers
n=20
for x in range(1,n+1):
    if (x % 2 != 0):
      print(x)


# print 30 even numbers
n=20
for x in range(1,n+1):
    if (x % 2 == 0):
      print(x)

#revese the string
n="hello world"
reverse_str=""
for x in n:
  reverse_str = x + reverse_str

print(reverse_str)

#palindrom are not


n="raninar"
pali=""
for x in n:
   pali = x + pali
if(n == pali):
      print("yes")
else:
      print("no")





    



    