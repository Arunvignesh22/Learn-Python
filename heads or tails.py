import random

Flip_1 = input("Do you want to flip the coin?")
Flip = Flip_1.title()
if Flip == "Yes":
    random_flip = random.randint(0, 1)
    if random_flip == 0:
        print("Tails")
    else:
        print("Heads")
else:
    print("You haven't flipped the coin")
