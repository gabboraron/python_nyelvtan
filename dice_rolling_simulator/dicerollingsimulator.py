import random

#x = random.random()
#print(int(x*10))

def roll():
    number = random.randint(1,6)
    if number == 1:
        print("----------")
        print("|        |")
        print("|   1    |")
        print("|        |")
        print("----------")

    if number == 2:
        print("----------")
        print("| 2      |")
        print("|        |")
        print("|      2 |")
        print("----------")

    if number == 3:
        print("----------")
        print("| 3       |")
        print("|    3    |")
        print("|       3 |")
        print("----------")

    if number == 4:
        print("----------")
        print("| 4     4 |")
        print("|         |")
        print("| 4     4 |")
        print("----------")

    if number == 5:
        print("----------")
        print("| 5      5 |")
        print("|    5     |")
        print("| 5      5 |")
        print("----------")

    if number == 6:
        print("----------")
        print("| 6      6 |")
        print("| 6      6 |")
        print("| 6      6 |")
        print("------------")

y = x = "y"
while y == x :
    roll()
    x = input("Do you want to roll it again? (y/n)  ")
