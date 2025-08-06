#adventure game 
name = input("Type you name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road you have to choose a path right/left to move ahead. ").lower()

if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across, choose between swim/walk. ")
    if answer == "swim":
        print("you swam across and were eaten by a crocodile. ")
        print("you lose.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game. ")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You have arrvide at amazom rainforest, where you can move ona path full of snakes or stay there and leave next morning with a new path, choose between (stay/move)")
    if answer == "move":
        print("you were halway of reaching the final stage but snake had bitten you on your leg.")
        print("You lose")
    elif answer == "stay":
        print("you woke up in the morning and went onto the right direction where it helped you reach to your final destination, You Win")
else: 
    print("Not a valid option you lose.")
print(f'Thank you for trying {name} :)')
    
