import random

def game(score,name):
    cch = random.randint(1, 10)
    for i in range(5):
        choice = int(input("\t\tEnter a number between 1 and 10: "))
        if choice != cch:
            print("\n\t\t\tWrong! Try again...\n")
            score -= 50
        else:
            print(f"\n\t\tCongratulations{name}, you guessed it!\n")
            score += 100
    else:
        print("\nGame over. The correct answer was", cch)
        score = 0
    return score  

print('\n\n----------------------Welcome to Guess The Number----------------------\n\n')
print('Rule of the game: \n\t You have five chances to guess a number.\n\n')
name = input("Enter your name: ")
score = 200
score = game(score,name)
print("Final score:", score)
