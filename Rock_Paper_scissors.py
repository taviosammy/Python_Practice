

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

answers = ['scissors', 'rock', 'paper']
cont = 'y' 

while cont.lower() == 'y' : 
  pick = input("\nRock, Paper or Scissors? ")

  cpu = random.choice(answers)
  if cpu == pick.lower():
    print('\nDRAW !!!!')
  
  #Outcome if the user picks Rock
  if pick.lower() == "rock" :
    print(f"You: {rock} \n\n")
    if cpu == "paper":
      print(f"CPU: {paper}\n")
      print('Paper wins!!!')
    elif cpu == "scissors":
      print(f"CPU: {scissors}\n")
      print('Rock wins!!!')
  #Outcome if the user picks Paper
  elif pick.lower() == "paper":
    print(f"You: {paper} \n\n")
    if cpu == "rock":
      print(f"CPU: {rock}\n")
      print('Paper wins!!!')
    elif cpu == "scissors":
      print(f"CPU: {scissors}\n")
      print('Scissors wins!!!\n') 
  #Outcome if the user picks scissors
  elif pick.lower() == "scissors":
    print(f"You: {scissors} \n\n")
    if cpu == "rock":
      print(f"CPU: {rock}\n")
      print('Rock wins!!!')
    elif cpu == "paper":
      print(f"CPU: {paper}\n")
      print('Paper wins!!!\n') 

  cont = input("Do you want to continue? Y or N? \n")