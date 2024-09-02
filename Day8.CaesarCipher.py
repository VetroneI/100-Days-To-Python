Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',\
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',\
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '#', '$', '%', '&', '(', ')', '*', '+', " "]

# Encrypt Message
def encrypt():
    encrypted = ""
    word = input("What do you want to encrypt\n")
    shift = int(input("By how much would you like to shift\n"))
    for a in word:
        if a in Letters:
            a = Letters[(Letters.index(a)+shift)%len(Letters)]
        encrypted += a
    print(f"Your encrypted message is \'{encrypted}\'.")
    if input("Would you like to go again?\nYes or No?\n").lower() == "yes":
        start()
    else:
        ("Have a good day!")

# Decrypt Message
def decrypt():
    decrypted = ""
    encrypted = input("What do you want to decrypt?\n")
    shift = int(input("What is the shift\n"))
    for a in encrypted:
        if a in Letters:
            a = Letters[(Letters.index(a)-shift)%len(Letters)]
        decrypted += a
    print(f"Your decrypted message is \'{decrypted}\'.")
    if input("Would you like to go again?\nYes or No?\n").lower() == "yes":
        start()
    else:
        ("Have a good day!")

# Start Program
def start():
    option = input("Would you like to encrypt or decrypt\n").lower()
    if option == "encrypt":
        encrypt()
    elif option == "decrypt":
        decrypt()
    else:
        print("That is not an option")
        start()

start()



