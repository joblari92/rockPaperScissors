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

choice = input('Rock, paper or scissors?').lower()

options = ['rock', 'paper', 'scissors']

position = random.randint(0,2)

if choice in options:

    print('Your choice:')

    if choice == 'rock':
        print(rock)
    elif choice == 'paper':
        print(paper)
    elif choice == 'scissors':
        print(scissors)

    print('Your oponent choice:')

    if options[position] == 'rock':
        print(rock)
    elif options[position] == 'paper':
        print(paper)
    elif options[position] == 'scissors':
        print(scissors)

    if choice == options[position]:
        print('Empate')
    elif choice == 'rock':
        if options[position] == 'paper':
            print('You lose')
        else:
            print('You win')
    elif choice == 'paper':
        if options[position] == 'scissor':
            print('You lose')
        else:
            print('You win')
    elif choice == 'scissor':
        if options[position] == 'rock':
            print('You lose')
        else:
            print('You win')

else:
    print('Introduce a valid input')