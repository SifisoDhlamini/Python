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

#Write your code below this line 👇

rps = [rock, paper, scissors]

num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors: "))

user_choice = rps[num]
computer_choice = random.choice(rps)

print(user_choice)
print("Computer chose:")
print(computer_choice)

winner = "computer"
if user_choice == rock:
  if computer_choice == scissors:
    winner = "user"
  elif computer_choice == rock:
    winner == "draw"
if user_choice == paper:
  if computer_choice == rock:
    winner = "user"
  elif computer_choice == paper:
    winner = "draw"
if user_choice == scissors:
  if computer_choice == paper:
    winner = "user"
  elif computer_choice == scissors:
    winner == "draw"

if winner == "draw":
  print("It is a draw")
elif winner == "user":
  print("You win")
else:
  print("You lose")
