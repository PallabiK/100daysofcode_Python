from replit import clear
import art

print (art.logo)
print("Welcome to the secret auction!")

def find_bid_winner(dict):
  highest_bid = 0
  bid_winner = ""
  for bidder in dict:
    if dict[bidder]> highest_bid:
      highest_bid = dict[bidder]
      bid_winner = bidder
  print(f"The winner is {bid_winner} who bid ${highest_bid}.")

bid_dict = {}
should_continue = True

while should_continue:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bid_dict[name] = bid
  continue_on = input("Is there any other bidder? Type 'yes' or 'no'. ").lower()
  if continue_on == 'no':
    should_continue = False
    find_bid_winner(bid_dict)
  else:
     clear()