#salary 5% bonus
service = int(input("enter your total services years : "))
salary = int(input("enter your annual salary ; "))
if service > 5:
    bonus = salary * 0.05
    print("your salary with bonus :", salary + bonus)
else:
    print("your salary without bonus ; ", salary)
