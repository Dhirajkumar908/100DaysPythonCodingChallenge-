"""
Day 17 Challenge
Go find your Rock, Paper, Scissors game from Day 14 and add the code here before you start. We are going to build upon this game.

Use a loop to repeat the game multiple rounds.
Keep score of player 1 and player 2.
End the game when a player wins three rounds using break and exit.
Use continue to restart the round until one player wins three rounds.
Your last bit of code should be the results of which player won.
"""
from getpass import getpass as input

print("Let's play Rock, Paper, Scissors!\n")
print("Select your move (R,P or S)\n")

player1_score=0
player2_score=0

while True:
  player1 = input("Player1 move:")
  player2 = input("player2 move:")

  if player1=="R":
    if player2=="R":
      print('You both chosed rock, it is a tie!')
    elif player2=="S":
      print('Rock beats scissors, player1 wins!')
      player1_score+=1
    elif player2=="P":
      print("Paper beats rock, player2 wins! ")
      player2_score +=1
      
  elif player1 == "P":
    if player2 =="R":
      print( "Paper beats rock, player1 wins!")
      player1_score +=1
    elif player2 == "s":
      print("Scissors beats paper, player2 wins!")
      player2_score +=1
    elif player2=="P":
      print("You both chose paper, it is a tie!")
      
  elif player1 =="S":
    if player2 =="R":
      print("Rock beats scissors, player2 wins!")
      player2_score +=1
    elif player2== "S":
      print("You both chose scissors, it is a tie!")
    elif player2 =="P":
      print( "Scissors beats paper, player1 wins!")
      player1_score +=1

  print("Player1 score:", player1_score)
  print("Player2 score:", player2_score)
  if player1_score==3 or player2_score==3:
    print("thank you for playing!")
    break
    exit()
  else:
    continue
    
    
    
    
