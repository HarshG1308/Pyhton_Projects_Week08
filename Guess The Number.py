import random

def fun(sc):
    a = random.randint(1, 10)
    for i in range(5):
        ch = int(input("\t\tEnter a number between 1 and 10: "))
        if ch != a:
            print("\n\t\t\tWrong! Try again...\n")
            sc -= 50
        else:
            print("\n\t\tCongratulations, you guessed it!\n")
            sc += 100
            break
    else:
        print("\nGame over. The correct answer was", a)
        sc = 0
    return sc 

print('\n\n----------------------Welcome to Guess The Number----------------------\n\n')
print('Rule of the game: \n\t You have five chances to guess a number.\n\n')
sc = 200
sc = fun(sc)
print("Final score:", sc)
