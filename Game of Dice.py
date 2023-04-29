import random 

print('\n\n----------------------Welcome to Game of Dice----------------------\n')
name = input('Enter your name: ')
print(f"\nHello! {name} Let's Start !!..")
ch = 'Y'
l = []
while ch == 'Y' or ch == 'y':
    print('\n1. Roll\n2. Exit')
    a = int(input('\nEnter Your Choice: '))
    c1= random.choice([1,2,3,4,5,6])
    c2= random.choice([1,2,3,4,5,6])
    if a == 1:
        print('\nNumber on the dices are: ',c1,c2)
        l.append([c1,c2])
    elif a == 2:
        print('\nTotal outcomes: ',l)
        print('\n\t\tThank You')
    else:
        print('\nEnter valid choice')
        a = int(input('\nEnter Your Choice: '))
    ch = input("\nDo you want to continue(Y/N): ")
else:
    print('\nTotal outcomes: ',l)
    print('\n\t\t...Thank You for Playing...')
