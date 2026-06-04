import tkinter
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    my_letter = [random.choice(letters) for letter in range(nr_letters)]
    my_number = [random.choice(numbers) for number in range(nr_numbers)]
    my_symbol = [random.choice(symbols) for symbol in range(nr_symbols)]
    password_list = my_letter + my_number + my_symbol
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    user_website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()

    if not user_website or not user_password:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=user_website, message=f"These are the details entered: \nu{user_email} \n{user_password} \n It it ok to save?")
        if is_ok:
            with open("data.txt", mode='a') as data_file:
                data_file.write(f"{user_website} | {user_email} | {user_password}\n")
            website_entry.delete(0, tkinter.END)
            email_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
# window.minsize(width=300, height=300)
window.config(padx=40, pady=40)
logo_image = tkinter.PhotoImage(file="logo.png")

canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = tkinter.Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = tkinter.Entry(width=35)
email_entry.insert(0, "thebronjame@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

generate_password_button = tkinter.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()