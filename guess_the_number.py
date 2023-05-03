import random
from replit import clear

logo = '''
  ________                                __  .__                                 ___.                 
 /  _____/ __ __   ____   ______ ______ _/  |_|  |__   ____     ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \   __\  |  \_/ __ \   /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   |  | |   Y  \  ___/  |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >  |__| |___|  /\___  > |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/             \/     \/       \/            \/    \/     \/       
        '''


def guess_number (level):
  """Guesses the number"""
  number = random.randint(1,100)
  game_over = False
  while not game_over:
    if level >0:
      print (f"You have {level} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      if guess > number:
        print("Too High.")
      elif guess < number:
        print("Too Low.")
      elif guess == number:
        print(f"You got it. The answer is {number}.")
        game_over = True
      level-=1
    else:
      print ("You have run out of attempts.")
      game_over = True
    

def play_game():
  """ Play game """
  print (logo)
  print("Welcome to the Number Guessing Game!")
  print("I am thinking of a number between 1 and 100.")
  diff_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if diff_level == "easy":
    guess_number(10)
  elif diff_level == "hard":
    guess_number(5)
  else:
    print("Invalid Entry.")

while input("Do you want to guess the number? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
