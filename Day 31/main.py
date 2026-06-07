import tkinter
import pandas as pd
import random
import os

timer = None
window = tkinter.Tk()
window.config(bg="#B1DDC6")
window.title("Flashy")
window.resizable(False, False)
window.config(padx=50, pady=20)

front_image = tkinter.PhotoImage(file="card_front.png")
back_image = tkinter.PhotoImage(file="card_back.png")
correct_image = tkinter.PhotoImage(file="right.png")
wrong_image = tkinter.PhotoImage(file="wrong.png")

def next_card():
    global random_word, timer
    if timer is not None:
        window.after_cancel(timer)
    random_word = random.choice(translations_dict)
    word = random_word["French"]
    canvas.itemconfig(language_text, text="French")
    canvas.itemconfig(word_text, text=word)
    timer = window.after(3000, flip_card)
    canvas.itemconfig(card_front_image, image=front_image)

def is_known():
    translations_dict.remove(random_word)
    pd.DataFrame(translations_dict).to_csv("words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_front_image, image=back_image)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=random_word["English"])





if os.path.exists("words_to_learn.csv"):
    translations = pd.read_csv("words_to_learn.csv")
else:
    translations = pd.read_csv("french_words.csv")



translations_dict = translations.to_dict(orient="records")

canvas = tkinter.Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
card_front_image = canvas.create_image(400, 258, image=front_image)
language_text = canvas.create_text(400, 150, text="French", font=("Arial", 30, "italic"))
word_text = canvas.create_text(400, 258, text="Bonjour", font=("Arial", 55, "bold"))

correct_button = tkinter.Button(image=correct_image, highlightthickness=0, bg="#B1DDC6", command=is_known)
correct_button.grid(row=1, column=0)

wrong_button = tkinter.Button(image=wrong_image, highlightthickness=0, bg="#B1DDC6", command=next_card)
wrong_button.grid(row=1, column=1)









canvas.grid(row=0, column=0, columnspan=2, pady=20)

next_card()
window.mainloop()