print(input("Welcome to Treasure Island.\
            \nWould you like to enter for a chance at treasure?\
            \nWARNING! Your life will be at risk\
            \nEnter or Leave?"))

if input("Are you sure? Yes or No?\n").lower() != "yes":
    print("Bye...")
elif input("You enter the island, there are two paths\
           \nleft or right\n").lower() != "left":
    print("A giant spider traps and eats you!\nGame Over!")
elif input("You go left\
           \n There is a giant lake, do you choose to \"go around\" or \"take a boat\"\n").lower() != "take a boat":
    print("On your way around the lake a giant bear attacks you!\nGame Over!")
elif input("You make it across the lake, on the dock there is a home with 3 doors.\
           \nYellow\
           \nBlue\
           \nRed\
           \nWhich do you choose to enter?\n").lower() != "blue":
    print("The door sucks you in and slams behind you. \nYour vision goes black\nGame Over!")
else:
    print("You have found a giant pile of gold!")
