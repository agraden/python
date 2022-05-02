import random
import string

password_length = int(input("How long do you want your password to be? "))
password = ""

print(range(password_length))

for position in range(password_length):
    password = password + random.choice(string.ascii_letters)
    print(password)