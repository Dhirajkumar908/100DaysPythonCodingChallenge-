from getpass import getpass as input

print("Let's play Rock, Paper, Scissors!")

user1_choise = input("User1: Enter 'rock', 'paper', or 'scissors': ")

user2_choise = input("User2: Enter 'rock', 'paper', or 'scissors': ")

if user1_choise == user2_choise:
    print("It's a tie!")
elif (user1_choise == "rock" and user2_choise == "scissors") or (
        user1_choise == "rock" and user2_choise == "paper") or (
            user1_choise == "paper"
            and user2_choise == "rocj ") or (user1_choise == "scissors"
                                             and user2_choise == "paper"):
    print("user 1 is Winner")

else:
    print("user 2 is Winner")

print("user 1 choise:", user1_choise)
print("user 2 choise:", user2_choise)
