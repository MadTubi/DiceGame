import random

numOfSides = int(input("How many sides are on the die you would like to play?"))



player1 = input("Enter your name player 1: ")
player1_pts = 0

player2 = input("Enter your name player 2:")
player2_pts = 0

numPlayed = 0
while True:
    die1 = random.randint(0,numOfSides)
    die2 = random.randint(0,numOfSides)

    die3 = random.randint(0,numOfSides)
    die4 = random.randint(0,numOfSides)

    print(f"\n{player1} rolls a {die1} and a {die2}.\nTotal points:  {die1 + die2}")
    player1_pts+=(die1 + die2) 
    print(F"{player1}'s total points: {player1_pts}")

    print(f"\n{player2} rolls a {die3} and a {die4}.\nTotal points:  {die3 + die4}")
    player2_pts+=(die3 + die4)
    print(F"{player2}'s total points: {player2_pts}")

    numPlayed = numPlayed + 1

    choice = input("\nWould you like to play again ? \nEnter Y for yes or N for no:").upper()

    if choice =='N':
        break

print("\n---------------")
print(f"Number of times played: {numPlayed}")
print(f"{player1}'s total points: {player1_pts}")
print(f"{player2}'s total points: {player2_pts}")

if player1_pts > player2_pts:
    print(f"\nWINNER: {player1}")
else:
     print(f"\nWINNER: {player2}")






