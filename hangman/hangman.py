import random

def hangman():
    word = random.choice(["Euope","tiger", "snow", "white", "hunt", "earth", "plumber"])
    validLetters = 'qwertzuiopasdfghjklyxcvbnm'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ""
        viewonly = ""
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
                viewonly = viewonly + " " + letter + " "
            else:
                main = main + " _ "
                viewonly = viewonly + " _ "
        if main == word:
            print(viewonly)
            print("You have won!")
            break

        print("Guess the word: ", viewonly)
        guess = input("- ")
        if guess in validLetters:
            guessmade = guessmade + guess
        else:
            print("Enter valid character")
            guess = input("- ")
        if guess not in word:
            turns = turns - 1
            print(str(turns) + " turns left")


name = input("Enter your name ")
print("welcome", name)
print("\t********")
print("try to gess less then 10 attempts")
hangman()
print()
