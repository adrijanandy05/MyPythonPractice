import random

print("Snake, Water and Gun Game")
computer_point=0
player_point=0
no_of_guesses=0
lst = ["s", "w", "g"]
while no_of_guesses<10:
    n = input("Enter your input: ")
    r=random.choice(lst)
    if n==r:
        print(f"Your input was {n} and computer input was {r}")
        print("Tie so no point to anyone")
    elif r=="s" and n=="g":
        print(f"Your input was {n} and computer input was {r}")
        player_point=player_point+1
        print(f"Computer Score is {computer_point} and player score is {player_point}")
    elif r=="s" and n=="w":
        print(f"Your input was {n} and computer input was {r}")
        computer_point=computer_point+1
        print(f"Computer Score is {computer_point} and player score is {player_point}")
    elif r=="w" and n=="s":
        print(f"Your input was {n} and computer input was {r}")
        player_point=player_point+1
        print(f"Computer Score is {computer_point} and player score is {player_point}")
    elif r=="w" and n=="g":
        print(f"Your input was {n} and computer input was {r}")
        player_point=player_point+1
        print(f"Computer Score is {computer_point} and player score is {player_point}")
    elif r=="g" and n=="s":
        print(f"Your input was {n} and computer input was {r}")
        computer_point=computer_point+1
        print(f"Computer Score is {computer_point} and player score is {player_point}")
    elif r=="g" and n=="w":
        print(f"Your input was {n} and computer input was {r}")
        player_point=player_point+1
        print(f"Computer Score is {computer_point} and player score is {player_point}")
    else:
        print(f"Your input was {n} and computer input was {r}")
        print("Invalid input")
    no_of_guesses=no_of_guesses+1
    print(f"No. of guesses left : {10-no_of_guesses}")
if computer_point>player_point:
    print(f"Computer : {computer_point} and Player : {player_point}")
    print("Computer Wins")
elif computer_point==player_point:
    print(f"Computer : {computer_point} and Player : {player_point}")
    print("It's a tie")
else:
    print(f"Player : {player_point} and Computer : {computer_point}")
    print("Player Wins")