from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.read_csv("data/words_to_learn,csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def next_card():
    global current_card, flip_timer
    heni.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas1.itemconfig(card_title, text="French", fill="Black")
    canvas1.itemconfig(card_word, text=current_card["French"], fill="Black")
    canvas1.itemconfig(card_background, image=front_image)
    heni.after(3000, func=flip_card)


def flip_card():
    canvas1.itemconfig(card_title, text="English", fill="white")
    canvas1.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas1.itemconfig(card_background, image=back_image)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn,csv",index=False)

    next_card()


# ---------------------------- UI SETUP ------------------------------- #
heni = Tk()
heni.title = "Flashy"
heni.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = heni.after(3000, func=flip_card)

canvas1 = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
card_background = canvas1.create_image(400, 263, image=front_image)
card_title = canvas1.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas1.create_text(400, 263, text="", font=("Ariel", 40, "bold"))
canvas1.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas1.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

next_card()

heni.mainloop()
