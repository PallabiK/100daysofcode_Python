import random
from higher_lower_art import logo, vs
from higher_lower_game_data import data
from replit import clear

def get_random_account():
  """returns random account"""
  return random.choice(data)

def format_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  #print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}."

def comparison(followers_a, followers_b):
  """comparing followers of account a and b, returns the account with higher followers"""
  if followers_a > followers_b:
    return "a"
  else:
    return "b"

def game():
  winner = ""
  score = 0
  accounta = get_random_account()
  print(logo)
  game_over = False
  
  while not game_over:
    accountb = get_random_account()
    #making sure option1 and option2 are not the same
    while accounta == accountb:
      accountb = get_random_account()
  
    print(f"Compare A: {format_data(accounta)}.")
    print(vs)
    print(f"Against B: {format_data(accountb)}.")
    winner = comparison(accounta["follower_count"], accountb["follower_count"])
    guess = input("Who has more followers? Type'A' or 'B': ").lower()
    clear()
    print(logo)
    if guess == winner:
      score +=1
      print(f"You are right! Current Score: {score}.")
    else:
      print(f"Sorry, that's wrong. Final Score: {score}.")
      game_over = True
    accounta = accountb

game()
    