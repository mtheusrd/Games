import random


def play():
    print_menu_message()
    secret_word = load_secret_word()

    right_letters= load_right_letters(secret_word)
    print(right_letters)

    hanged = False
    right = False
    mistake = 0

    while(not hanged and not right):

        kick = ask_kick()

        if(kick in secret_word):
            mark_right_kick(kick, right_letters, secret_word)
        else:
            mistake += 1
            draw_gibbet(mistake)

        hanged = mistake == 7
        acertou = "_" not in right_letters

        print(right_letters)

    if(right):
        print_win_message()
    else:
        print_loser_message(secret_word)


def draw_gibbet(mistake):
    print("  _______     ")
    print(" |/      |    ")

    if(mistake == 1):
        print (" |      (_)   ")
        print (" |            ")
        print (" |            ")
        print (" |            ")

    if(mistake == 2):
        print (" |      (_)   ")
        print (" |      \     ")
        print (" |            ")
        print (" |            ")

    if(mistake == 3):
        print (" |      (_)   ")
        print (" |      \|    ")
        print (" |            ")
        print (" |            ")

    if(mistake == 4):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |            ")
        print (" |            ")

    if(mistake == 5):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |            ")

    if(mistake == 6):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      /     ")

    if (mistake == 7):
        print (" |      (_)   ")
        print (" |      \|/   ")
        print (" |       |    ")
        print (" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()



def print_win_message():
    print("Congratulations! You win!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def print_loser_message(secret_word):
    print("Out... You were hanged !")
    print("The word was {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mark_right_kick(kick, right_letters, secret_word):
    index = 0
    for letter in secret_word:
        if (kick == letter):
            right_letters[index] = letter
        index += 1

def ask_kick():
    kick = input("Choose a letter! ")
    kick = kick.strip().upper()
    return kick

def load_right_letters(word):
    return ["_" for letter in word]

def print_menu_message():

    print("**********************************")
    print("** Welcome to the Hangman Game! **")
    print("**********************************")

def load_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


if(__name__ == "__main__"):
    play()
