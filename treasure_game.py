print("Welcome. Your objective is to find the treaure. Wish you luck on your adventure.")

direction = input("You are at a crossroads. Which direction do you want to go? Type 'Left' or 'Right'\n")
if direction.lower() == "left":
  way = input("You are infront of a mountain. Do you want to climb it to get across or dig a tunnel? Type 'Climb' or 'Dig'\n")
  if way.lower() == "climb":
    act = input ("You climb to the top of the mountain and find a bush of berries. You can eat the berries or continue on your way down. Type 'Eat' or 'Down'\n")
    if act.lower() == "down":
      mode = input ("You get to the bottom of the mountain and find a horse. Do you take the horse or keep walking? Type 'Walk' or 'Horse'\n")
      if mode.lower() == "horse":
        print("You let the horse lead the way and ended up at a shack filled with treasure. You took the treasure back to your village and lived happily ever after.")
      elif mode.lower() == "walk":
        print ("You got attacked by a murder of crows. Game Over")
      else:
        print("You woke up from your dream and never found the treasure. Game Over")
    elif act.lower() == "eat":
      print("You died from eating the berries. Game Over.")
    else:
      print("You fell off the mountain doing that. Game Over")
  elif way.lower() =="dig":
    print("You die of exhaustion while digging. Game Over.")
  else:
    print("You get picked up by a giant bird. Game Over.")
elif direction.lower() == "right":
  print ("You get lost in the Forest. Game Over.")
else:
  print("You are shot by an arrow. Game Over")

print("\nAnd that's a wrap.")