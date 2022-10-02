import guess_game
import hangman_game

def choose_game():
    print("*******************************")
    print("***** Matheus - Minigames *****")
    print("*******************************")

    print("Chose what a Minigame do you want play!")
    print("")
    print("(1) Guess Game (2) Hangman Game")

    choose = int(input("Type your chose: "))

    if (choose == 1):
        print("You chose the Guess Game!")
        guess_game.play()
    elif(choose == 2):
        print("You chose the Hangman Game")
        hangman_game.play()
    else:
        print("Invalid Option!")

if(__name__ == "__main__"):
    choose_game()