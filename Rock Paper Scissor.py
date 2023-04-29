import random 

print('\n\n----------------------Welcome to Game of Rock Paper and Scissor (Computer Vs Human)----------------------\n\n')

ch = 'Y'

while ch == 'Y' or ch == 'y':
    c1 = random.choice(['Rock','Paper','Scissor'])
    c2 = input('\nEnter your choice: ')
    if (c1 == 'Rock' and c2 == 'Scissor') or (c1 == 'Paper' and c2 == "Rock") or (c1 == 'Scissor' and c2 == 'Paper'):
        print('\n              Computer Wins !!')
    elif c1 == c2:
        print("\n              It's a Tie")
    else:
        print('\n              Congratulations !! You Win...')
    ch = input("\nDo you want to continue(Y/N): ")
