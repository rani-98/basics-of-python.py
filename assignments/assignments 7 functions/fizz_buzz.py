def fizz_buzz():
    for x in range(1,101):
        if x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")
        elif (x % 3 == 0 and x % 5 == 0):
            print("fizzbuzz")
        else:
            print(x)
fizz_buzz()
print()