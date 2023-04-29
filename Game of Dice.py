import random 

print('\n\n----------------------Welcome to Game of Dice----------------------\n')
name = input('Enter your name: ')
print(f"\nHello! {name} Let's Roll !!..")
ch = 'Yes'
list = []
while ch == 'Yes' or ch == 'yes':
    print('\n1. Roll\n2. Exit')
    n = int(input('\nEnter Your Choice: '))
    out1= random.choice([1,2,3,4,5,6])
    out2= random.choice([1,2,3,4,5,6])
    if n == 1:
        print('\nNumber on the dices are: ',out1,out2)
        list.append([out1,out2])
    elif n == 2:
        print('\nTotal outcomes: ',list)
        print('\n\t\tThank You')
    else:
        print('\nEnter valid choice')
        n = int(input('\nEnter Your Choice: '))
    ch = input("\nDo you want to continue(Yes/No): ")
else:
    print('\nTotal outcomes: ',list)
    print('\n\t\t...Thank You for Playing...')