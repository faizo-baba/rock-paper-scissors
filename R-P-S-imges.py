print ("welcome to rock, paper, scissors")

import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choices = ["rock","paper","scissors"]
asci_imges = [rock,paper,scissors]

user_input = int(input("choose: 0 for rock,1 for paper,2 for scissor: "))
if user_input < 0 or user_input > 2:
    print ("invalid choice")
else :
    print (f"choose: \n{asci_imges[user_input]}")   

comp_choice = random.randint(0,2)
print (f"choose:\n{asci_imges[comp_choice]}")

if user_input == comp_choice :
    print ("it's a tie")
elif (user_input == 0 and comp_choice == 2) or \
    (user_input == 1 and comp_choice == 0) or \
    (user_input==2 and comp_choice==1):
    print("you won")
else :
    print ("you lose")