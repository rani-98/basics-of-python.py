

import random

a= random.randint(1,10)

tries = 1
while tries <=3: # true
   u=int(input("guess the number:"))

   if u == a:
      print("guess was correct")
      break
   elif u > a:
      print("your guess is large")
   elif u < a:
      print("your guess is small")

   tries = tries + 1
 
   print("your tries",4-tries,"only")
else:
   print("your tries finished better luck next time.")