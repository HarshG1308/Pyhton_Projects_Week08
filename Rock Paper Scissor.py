import random 

print('\n\n----------------------Welcome to Game of Rock Paper and Scissor----------------------\n\n')

a = 'Y'

while a == 'Y' or a == 'y':
    c1 = random.choice(['Rock','Paper','Scissor'])
    c2 = input('\nEnter your choice: ')
    if (c1 == 'Rock' and c2 == 'Scissor') or (c1 == 'Paper' and c2 == "Rock") or (c1 == 'Scissor' and c2 == 'Paper'):
        print('\n              Computer Wins... !!')
    elif c1 == c2:
        print("\n              It is a Tie Game...")
    else:
        print('\n              You Wins...')
    a = input("\nDo you want to continue(Y/N): ")
