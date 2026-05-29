from tkinter import *
import random


number = random.randint(1, 10)


def check():

    guess = int(entry.get())

    if guess == number:
        result.config(text="Correct ✅")

    elif guess < number:
        result.config(text="Too Small")

    else:
        result.config(text="Too Large")



root = Tk()

root.title("Guess Game")
root.geometry("300x200")


label = Label(
    root,
    text="Guess Number 1 to 10"
)

label.pack()


entry = Entry(root)
entry.pack()


button = Button(
    root,
    text="Check",
    command=check
)

button.pack()


result = Label(root, text="")
result.pack()


root.mainloop()
