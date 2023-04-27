import random
print("Let's Play Rock-Paper-Scissor")
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

options = [rock, paper, scissors]

opponent = int(input("Make your choice. Type 0 for rock, 1 for paper, 2 for scissors\n"))
if opponent<0 or opponent>=3:
  print("You typed an invalid number, you lose. :/")
else:
  print(f"Your choice:\n {options[opponent]}")
  computer = random.randint(0,2)
  print(f"Computer chose:\n {options[computer]}")
  if opponent<0 or opponent>=3:
    print("You typed an invalid number, you lose. :/")
  elif opponent == computer:
    print("It's a draw.")
  elif opponent == 2 and computer == 0:
    print("You lose.:/")
  elif opponent == 0 and computer == 2:
    print("You win! :D")
  elif computer> opponent:
    print("You lose.:/")
  elif computer<opponent:
    print("You win! :D")
