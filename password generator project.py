import random
import string

low = list(string.ascii_lowercase)
up = list(string.ascii_uppercase)
digits = list(string.digits)
specials = list("!@#$%^&*-_=+;:,.?/")

number = input("Enter the number of characters for the password: ")

while True:
    try:
        number = int(number)
    except:
        number = input("Please enter a integer digit only: ")
        continue
    break
random.shuffle(low)
random.shuffle(up)
random.shuffle(digits)
random.shuffle(specials)

part1 = round(number * 0.25)
part2 = round(number * 0.25)
part3 = round(number * 0.25)
part4 = round(number * 0.25)

password = []

for i in range(part1):
    password.append(random.choice(low))

for i in range(part2):
    password.append(random.choice(up))

for i in range(part3):
    password.append(random.choice(digits))

for i in range(part4):
    password.append(random.choice(specials))

random.shuffle(password)

High_security_password = "".join(password)
print("Your generated password is: ", High_security_password)
