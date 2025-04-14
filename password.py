# password.py - takes in user input length, and generates random password of that length

import random 
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+{}:" # random password will contain following characters 
length_password = int(input("Enter the length of the password: ")) # length is input length
a = "".join(random.sample(password, length_password)) # randomly takes characters from password and joins together in length of length_password
print(f"Your password is {a}")
