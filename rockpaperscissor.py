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

import random

x= int(input("Welcome to rock, paper and scissors game. What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

if x==0:
  print(rock)
elif x==1:
  print(paper)
elif x==2:
  print(scissors)
else:
  print("Enter a valid number")

print("\n")
print("Computer chose:")
print("\n")

c= random.randint(0,2)
if c==0:
  print(rock)
elif c==1:
  print(paper)
else:
  print(scissors)

if x==c:
  print("Its a draw.")
elif x==0 and c==2:
  print("You win")
elif x==2 and c==0:
  print("You lose")
elif x<c:
  print("You lose")
else:
  print("You win")

