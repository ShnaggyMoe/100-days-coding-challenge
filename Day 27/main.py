import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

#Label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=8)

# Button
def button_clicked():
    # print("I Got Clicked!")
    new_text = input.get()
    my_label["text"] = new_text


button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=0, row=4)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)




window.mainloop()