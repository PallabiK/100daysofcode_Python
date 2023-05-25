import pandas

phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")
all_letters = {row.letter:row.code for (index, row) in phonetic.iterrows()}

def generate_phonetic():
    word = input("Please enter a word: ").upper()
    try:
        phonetic_word = [all_letters[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the English alphabet please.")
        generate_phonetic()
    else:
        print(f"The phonetic words are:\n{phonetic_word}")

generate_phonetic()

# input_is_not_word = True
#
# while input_is_not_word:
#     word = input("Please enter a word: ").upper()
#     try:
#         phonetic_word = [all_letters[letter] for letter in word]
#         print(f"The phonetic words are:\n{phonetic_word}")
#         input_is_not_word = False
#     except KeyError:
#         print("Sorry, only letters in the English alphabet please.")

