import tkinter

window = tkinter.Tk()
window.minsize(width=400, height=200)
window.title("Mile to Km Converter")

def conversion():
    value = user_input.get()
    integer = int(value)
    miles_converted = integer * 1.6
    conversion_label["text"] = miles_converted

label_1 = tkinter.Label(text="Miles", font=("Arial", 14,))
label_1.grid(column=2, row=0, padx=25, pady=25)

label_2 = tkinter.Label(text="is equal to", font=("Arial", 14))
label_2.grid(column=0, row=1, padx=25, pady=25)

label_3 = tkinter.Label(text="Km", font=("Arial", 14))
label_3.grid(column=2, row=1, padx=25, pady=25)

user_input = tkinter.Entry()
user_input.grid(column=1 , row=0)

button = tkinter.Button(text="Calculate", font=("Arial", 15), command=conversion)
button.grid(column=1, row=2)

conversion_label = tkinter.Label(text="0", font=("Arial", 15))
conversion_label.grid(column=1, row=1)





window.mainloop()