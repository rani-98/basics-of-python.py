#. Number Pattern Printing: Write a program using a `for` loop that prints a number pattern. For example, if the user enters 5, the program should print. Number Pattern Printing: Write a program using a `for` loop that prints a number pattern. For example, if the user enters 5, the program should pri
n=int(input("enter number: "))
pre = " "
for i in range(1,n):
  pre=pre+str(i)  # "1"+ "2"=12
  print(pre)

n=int(input("enter number: "))


for i in range(0, n):
	for j in range(0, i+1):
		print("*", end=" ")
	print()
