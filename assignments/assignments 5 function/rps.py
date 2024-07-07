import random

print('Start Rock , Paper , Scissor game ')
player_wins=0
computer_wins =0
tries=1
while tries<=3:
  player=input("choose one [rock,paper,scissor]: ")
  options=["rock","paper","scissor"]
  computer=random.choice(options)
  if player==computer:
    print("tie",player)
  elif player=="rock":
    if computer=="paper":
     print("paper cover rock you lose,computer choose ",computer)
     computer_wins+=1
    else:
      print("rock smashess scissor you win,computer choose ",computer)
      player_wins+=1
      
  elif player=="paper":
    if computer=="rock":
      print("paper covered rock you win,computer choose ",computer)
      player_wins+=1
    else:
      print("scissor cuts paper you lose,computer choose ",computer)
      computer_wins+=1
  elif player=="scissor":
   if computer=="rock":
    print("rock smashes scissor you lose,computer choose ",computer)
    computer_wins+=1
   else:
     print("scissors cuts paper you win ,computer choose ",computer)
     player_wins+=1
  tries = tries + 1
  print("your tries",4-tries,"only")
else:
    print("your tries is completed. game is over")





