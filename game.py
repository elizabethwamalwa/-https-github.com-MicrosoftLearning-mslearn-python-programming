import random

# Display the game title
print("Rock, Paper, Scissors!")
print("-" *23   )
# Get and display the player's choice
player=input("Enter your choice (rock, paper, scissors): ").lower()
print(f"You chose {player}.")

# Check if the player's choice is invalid
if player !="rock" and player !="paper" and player !="scissors"  :
  # Display an invalid input message
  print("Invalid choice Please choose rock paper or scissors")
# Play the game if the player's choice is valid
else:
    # Generate the computer's choice
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"computer chose:{computer}")
    # Determine the winner
if player == computer:
    print("It's a tie!")
elif player =="rock" and computer =="scissors":
    print("You win! Rock crushes scissors")
elif player =="paper" and computer =="rock":
    print("You win! Paper covers rock")
elif player =="scissors" and computer =="paper":
    print("You win! Scissors cuts paper")
else:
    print(f"Computer wins! {computer.capitalize()} beats {player}.")