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
        if number < 4:
            number = input("Password must be at least 4 characters. Try again: ")
            continue
    except ValueError:
        number = input("Please enter an integer digit only: ")
        continue
    break


part1 = number // 4
part2 = number // 4
part3 = number // 4
part4 = number - part1 - part2 - part3

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


print("Your generated password is:", High_security_password)
