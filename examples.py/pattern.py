
n=6
for x in range(n,0,-1):
  print(x*' * ' )


rows=6
for x in range(rows,0,-1):
  r=(x*" *").rjust(rows*2)
  print(r)


n=5
for i in range(0, n):
  for j in range(0, i+1):
    print("*",end=" ")
  print()

n=7
for x in range(1,n+1):
  print("$ "*n)


# in complete
n=6
p=""
for x in range(1,n-1):
  p = p + "  *  "
  print(p.center(n+(n+1)))


rows=5
for x in range(rows,0,-1):
    spaces=" "*(rows-x)
    stars=" *"*x
    print(spaces+stars)

rows=5
for x in range(rows,0,-1):
    spaces=" "*(rows-x)
    stars="*"*x
    print(spaces+stars)
    








