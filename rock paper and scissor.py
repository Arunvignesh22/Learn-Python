import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_decision = input("What do you choose? Type 0 for Rock, Type 1 for Paper and 2 for Scissors.")

options = [rock, paper, scissors]
computer_decision = random.choice(options)

if user_decision == "0" and computer_decision == rock:
    print(f"you chose {rock}\ncomputer chose{rock}\nMatch drawn")
elif user_decision == "0" and computer_decision == paper:
    print(f"you chose {rock}\n computer chose{paper}\n You've lost")
elif user_decision == "0" and computer_decision == scissors:
    print(f"you chose {rock}\n computer chose{scissors}\n you won")
elif user_decision == "1" and computer_decision == rock:
    print(f"you chose {paper}\n computer chose{rock}\n You've won")
elif user_decision == "1" and computer_decision == paper:
    print(f"you chose {paper}\n computer chose{paper}\n Match drawn")
elif user_decision == "1" and computer_decision == scissors:
    print(f"you chose {paper}\n computer chose{scissors}\n You've lost")
elif user_decision == "2" and computer_decision == rock:
    print(f"you chose {scissors}\n computer chose{rock}\n you 've lost'")
elif user_decision == "2" and computer_decision == paper:
    print(f"you chose {scissors}\n computer chose{paper}\n you won")
else:
    print(f"you chose {scissors}\n computer chose{scissors}\n Match drawn")