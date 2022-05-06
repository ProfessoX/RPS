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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
else:
  print(scissors)

print("Computer chose:")

rps = int(len(["rock", "paper", "scissors"]))
comp_choice = random.randint(0, rps - 1)
print(comp_choice)

if comp_choice == 0:
  print(rock)
elif comp_choice == 1:
  print(paper)
else:
  print(scissors)

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and comp_choice == 2:
  print("You win!")
elif comp_choice == 0 and user_choice == 2:
  print("You lose")
elif comp_choice > user_choice:
  print("You lose")
elif user_choice > comp_choice:
  print("You win!")
elif comp_choice == user_choice:
  print("It's a draw")