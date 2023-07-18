print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
move = input("left or right ?").lower()
if move == "left":
    move_2= input("swim or wait? ").lower()
    if move_2=="wait":
        door=input("Which door?").lower()
        if door=="yellow":
            print("You Win!")
        elif door=="blue":
            print("Eaten by beasts.\n Game Over.")
        elif door=="red":
            print("Burned by fire.\n Game Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.\nGame Over.")
else:
    print("Fall into a hole.\nGame Over.")
