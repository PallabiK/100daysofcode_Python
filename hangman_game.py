import random
from hangman_words import word_list
from hangman_art import logo, stages
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)

display = []
for _ in range(word_length):
    display += "_"
print(f'There are {word_length} letters in the word.')
print(f"{' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print (f"You have already guessed {guess}")
    if guess not in chosen_word:
      lives-=1
      print(f"You guessed '{guess}' which is not in the word. You lose a life.")
      print(stages[lives])
      if lives == 0:
        end_of_game = True
        print("You lose.")
        print(f"Your word was {chosen_word}.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
  
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win.")