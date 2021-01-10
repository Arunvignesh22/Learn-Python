import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

bill_payer_1 = len(names)
bill_payer_2 = random.randint(0, bill_payer_1)
bill_payer = names[bill_payer_2 - 1]

print(f"{bill_payer} is going to pay the bill today")