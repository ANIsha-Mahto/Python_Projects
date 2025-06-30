import random
def roll_dice():
    return random.randint(1,6)
print("dice rollinf simulator🎲")
while True:
    roll=input("Roll the dice?(yes/no):").lower()
    if roll=="yes":
        print("you rolled:",roll_dice())
    elif roll=="no":
        print("thnks for playing!")
        break
    else:
        print("please type 'yes' or 'no'")