# generate a 6-digit OTP
import random
import string

print('\n\n----------------------OTP Generator----------------------\n\n')

otp = ""
for i in range(6):
    otp += str(random.randint(0, 9))

print("\t\tYour 6 digit OTP is:", otp)

# generate a 4-digit OTP
otp = ""
for i in range(4):
    otp += str(random.randint(0, 9))

print("\n\t\tYour 4 digit OTP is:", otp)

#generate a 6-digit alphanumeric OTP
otp = ""
d = string.digits
l = string.ascii_letters
d1 = random.choices(d,k=3)
l2 = random.choices(l,k=3)
f = d1 + l2
for i in f :
    otp += i
print("\n\t\tYour 6 digit alphanumeric OTP is:", otp)
