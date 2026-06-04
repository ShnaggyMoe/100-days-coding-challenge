import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    my_label["text"] = 'Timer'
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        my_label["text"] = "Work"
        my_label["fg"] = PINK
        count_down(work_sec)
        reps += 1
    elif reps == 2 or reps == 4 or reps == 6:
        my_label["text"] = "Break"
        my_label["fg"] = RED
        count_down(short_break_sec)
        reps += 1
    elif reps == 8:
        my_label["text"] = "Break"
        my_label["fg"] = GREEN
        count_down(long_break_sec)
        reps = 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 1:
            check_mark["text"] += '✔'


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


my_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=("Times New Roman", 30))
my_label.grid(column=2, row=0)

start_button = tkinter.Button(text="Start", font=("Arial", 10), command=start_timer)
start_button.grid(column=1, row=3)

reset_button = tkinter.Button(text="Reset", font=("Arial", 10), command=reset_timer)
reset_button.grid(column=3, row=3)

check_mark = tkinter.Label(text="", fg=GREEN, bg=YELLOW)
check_mark.grid(column=2, row=3)



window.mainloop()