import random 
import string

print('\n\n----------------------Welcome to Strong Password Generator----------------------\n')

u = string.ascii_uppercase
l = string.ascii_lowercase
d = string.digits
p = string.punctuation

pw = ''
a = int(input('\n How many characters you want in password (8/12):'))

if a == 8:
    u1 = random.choices(u,k=2)
    l1 = random.choices(l,k=2)
    d1 = random.choices(d,k=2)
    p1 = random.choices(p,k=2)
    pwl = u1 + l1 + d1 + p1
    for i in pwl:
        pw = pw + i
elif a==12:
    u1 = random.choices(u,k=3)
    l1 = random.choices(l,k=3)
    d1 = random.choices(d,k=3)
    p1 = random.choices(p,k=3)
    pwl = u1 + l1 + d1 + p1
    for i in pwl:
        pw = pw + i
else:
    print('Enter valid choice...')
    a = int(input('\n How many characters you want in password (8/12): '))

print('\n\t\t Generated password is: ',pw)