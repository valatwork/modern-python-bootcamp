# print("...rock...")
# print("...paper...")
# print("...scissors...")

# player1 = input("(enter Player 1's choice): ")
# player2 = input("(enter Player 2's choice): ")

# print("SHOOT!")

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ")
player2 = input("Player 2, make your move: ")

if player1 == "rock" and player2 == "scissors":
    print("player1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins!")
elif player1 == player2:
    print("It's a tie")
else:
    print("something went wrong")