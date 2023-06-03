from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"

current_card = {}

#-------Data File -----#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/bangla_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


#-------Functions------#
def next_card():
    global current_card
    current_card = choice(to_learn)
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="Bangla", fill="black")
    canvas.itemconfig(card_word, text=current_card["Bangla"], fill="black")

def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    txt = canvas.itemcget(card_title, 'text')
    if txt == "Bangla":
        canvas.itemconfig(card_background, image=card_back_img)
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    else:
        canvas.itemconfig(card_background, image=card_front_img)
        canvas.itemconfig(card_title, text="Bangla", fill="black")
        canvas.itemconfig(card_word, text=current_card["Bangla"], fill="black")

def alphabet_window():
    alphabet_img = PhotoImage(file="images/bangla_alphabet.png")
    new_window = Toplevel()
    new_window.title("Bangla Letters")
    new_canvas = Canvas(new_window, width=390, height=580)
    new_canvas.create_image(0, 0, image=alphabet_img, anchor=NW)
    new_canvas.grid(column=0, row=0)
    new_canvas.alphabet_img = alphabet_img


#-------UI Setup ------#
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#flip_timer = window.after(TIMER, func=flip_card)

#canvas with Bangla word
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img=PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=4)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=(FONT, 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=(FONT, 60, "bold"))


#buttons
unknown_img = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_img, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

flip_button = Button(text="Flip Card", font=(FONT, 20, "bold"), bg=BACKGROUND_COLOR, command=flip_card)
flip_button.grid(column=1, row=1)
flip_button.config(padx=10, pady=10)

known_img = PhotoImage(file="images/right.png")
known_button = Button(image=known_img, highlightthickness=0, command=is_known)
known_button.grid(column=3, row=1)


alphabet_button = Button(text="Bangla\nLetters", font=(FONT, 20, "bold"), bg=BACKGROUND_COLOR, command=alphabet_window)
alphabet_button.grid(column=2, row=1)

next_card()


window.mainloop()
