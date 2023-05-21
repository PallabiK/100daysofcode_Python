import pandas

phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
all_letters = {row.letter:row.code for (index, row) in phonetic.iterrows()}

word = input("Please enter a word: ").upper()
phonetic_word = [all_letters[letter] for letter in word]

print(f"The phonetic words are:\n{phonetic_word}")