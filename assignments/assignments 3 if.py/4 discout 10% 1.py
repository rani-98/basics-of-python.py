amount = int(input("enter your purcase amount"))
if amount >1000:
   discount = amount * 0.10
   print ("discount amount", discount)
elif amount <= 1000:
   print ("invalid amount")    
