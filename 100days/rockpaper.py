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

new1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

ch_list = [rock, paper, scissors]
new2 = random.randint(0, 2)

if new1 >= 3 or new1 < 0 :
  print("Invalid nr! You lose!")
else:
  print(ch_list[new1])

if new1 == 0 and new2 == 2:
  print("You win!")

elif new2 > new1:
  print("you lose!")

elif new2 == new1:
  print("draw")