#Project2
#Rock_Paper Scissors


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

get_img =[rock,paper,scissors]

user_choice=int(input("What do you want to choose? \n Type: \n 0 Rock \n 1 Paper \n 2 Scissors"))
print(get_img[user_choice])

import random
computer_choice=random.randint(0,2)
print(get_img[computer_choice])
# print(f"Computer chose {computer_choice}")

def rock(b,a=0):
    if b==1:
        print("You Loose :(")
    elif b==2 :
        print("You Win :)")
    else:
        print("Try Again")

def paper(b,a=1):
    if a==1 and b==2:
        print("You Loose :(")
    elif a==1 and b==0 :
        print("You Win :)")
    else:
        print("Try Again")

def scissors(b,a=2):
    if b==2:
        print("Try Again!")
    elif b==0 :
        print("You Loose :(")
    else:
        print("You Win :)")

if user_choice==0:
    rock(computer_choice)
elif user_choice==1:
    paper(computer_choice)
elif user_choice==2:
    scissors(computer_choice)
else:
    print(f"\n\nYou Entered an Invalid Number {user_choice}, You Lose! :(")
    print("Try Again with \n 0 Rock \n 1 Paper \n 2 Scissors")



