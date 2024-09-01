import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nrLetters = int(input("How many letters would you like in your password?\n")) 
nrSymbols = int(input(f"How many symbols would you like?\n"))
nrNumbers = int(input(f"How many numbers would you like?\n"))

password = []


# Password Grab Module

def grab(type, amount):
    global password
    for x in range(amount):
        random.shuffle(type)
        password.extend(type[1])
   
grab(letters, nrLetters)
grab(symbols, nrSymbols)
grab(numbers, nrNumbers)


# Password Gen 

random.shuffle(password)

print("Password: " + "".join(password)) 
