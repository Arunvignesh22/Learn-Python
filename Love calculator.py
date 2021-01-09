print("Welcome to the Love Calculator!")
name_male = input("What is your name? \n")
name_female = input("What is their name? \n")

name1 = name_male.upper()
name2 = name_female.upper()

T = name1.count("T") + name2.count("T")
R = name1.count("R") + name2.count("R")
U = name1.count("U") + name2.count("U")
E = name1.count("E") + name2.count("E")

L = name1.count("L") + name2.count("L")
O = name1.count("O") + name2.count("O")
V = name1.count("V") + name2.count("V")
E = name1.count("E") + name2.count("E")

TRUE = (T + R + U + E)
LOVE = (L + O + V + E)

Final = int(' %d%d ' % (TRUE, LOVE))

if 10 >= Final >= 90:
    print(f"Your score is {Final}, You go together like coke and mentos")
elif 40 <= Final <= 50:
    print(f"Your score is {Final}, You are alright together")
else:
    print(f"Your score is {Final}")
