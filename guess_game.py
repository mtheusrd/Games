import random


def play():

   """ The project is minigame where the playr need's guess the Secret Number. When he is wrong, lost points.
   In end, the script count all the lost points and print the final score."""

print("********************************")
print(" Welcome to the Guessing Game")
print("********************************")

# Variables
secret_number = random.randrange(1, 101)
attempts = 0
level = 0
points = 1000

# Levels
print("This game have 3 levels. Chose one!")
print("(1) Easy | (2) Medium | (3) Expert")

level = int(input("Type your chose: "))

if (level == 1):
    attempts = 20
elif (level == 2):
    attempts = 10
else:
    attempts = 5

# Rounds
for round in range(1, attempts + 1):
    print("Round {} of {}!".format(round, attempts))

    kick = input("Type a number from 1 to 100: ")
    result = int(kick)

    if (result > 100 or result < 1):
        print("You must type a number from 1 to 100. Try again: ")
        continue
        print("Você digitou: ", result, "!")

        # Conditions
        correct = result == secret_number
        above = result > secret_number
        below = result < secret_number

    if (correct):
        print("Congratulations! You're right!")
        print("You make {} points!".format(points))
        break
    else:
        if (above):
            print("You wrong. Your attempt was above than secret number!")
        elif (below):
            print("You wrong. Your attempt was below than secret number!")
lost_points = abs(secret_number - result)
points = points - lost_points

print("End of the Game!")

if(__name__ == "__main__"):
    play()