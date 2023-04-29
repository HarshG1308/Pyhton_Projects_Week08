import random 
import string

print('\n\n----------------------Welcome to Strong Password Generator----------------------\n')

up = string.ascii_uppercase
lo = string.ascii_lowercase
di = string.digits
pu = string.punctuation

pw = ''
n = int(input('\n How many characters you want in password (8/12):'))

if n == 8:
    up1 = random.choices(up,k=2)
    lo1 = random.choices(lo,k=2)
    di1 = random.choices(di,k=2)
    pu1 = random.choices(pu,k=2)
    pwl = up1 + lo1 + di1 + pu1
    for i in pwl:
        pw = pw + i
elif n==12:
    up1 = random.choices(up,k=3)
    lo1 = random.choices(lo,k=3)
    di1 = random.choices(di,k=3)
    pu1 = random.choices(pu,k=3)
    pwl = up1 + lo1 + di1 + pu1
    for i in pwl:
        pw = pw + i
else:
    print('Enter valid choice...')
    n = int(input('\n How many characters you want in password (8/12): '))

print('\n\t\t Generated password is: ',pw)
