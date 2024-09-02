import os
auctioners = {

}

def auction():
    global auctioners
    global amount
    os.system("cls")
    print('Welcome to the auction!')
    name = str((input('What is your name?\n')))
    amount = 0
    def amountVerify():
        global amount
        amount = int((input(f'Welcome {name} How much would you like to bid\n$')))
        if input(f'You entered ${amount}, is this correct?\n').lower() == 'no':
            amountVerify()
    amountVerify()
    auctioners = {name: amount}
    if input('Are there more auctioneers?\n').lower() == 'yes':
        auction()
    else:
        os.system("cls")
        maxbidder = max(auctioners)
        print(f'{maxbidder} has won with a bet of ${str(auctioners[maxbidder])}!')
        
    

    
auction()
