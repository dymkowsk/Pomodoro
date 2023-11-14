import tkinter as TK

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
SECONDS_IN_MIN = 60
ONE_SECOND = 1000  # in milliseconds
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = (FONT_NAME, 35, "bold")
FONT_TITLE = (FONT_NAME, 50, "bold")
FONT_BUTTON = (FONT_NAME, 24, "bold")
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    count = start_timer.counter
    if count == 8:
        title.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif count % 2 == 0:
        title.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        title.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

    start_timer.counter = count + 1


def reset_timer():
    window.after_cancel(count_down.timer)
    start_timer.counter = 1
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    seconds = count % SECONDS_IN_MIN
    time_left = "{:02d}".format(count // SECONDS_IN_MIN) + ":" + "{:02d}".format(seconds)

    canvas.itemconfig(timer_text, text=time_left)

    if count > 0:
        count_down.timer = window.after(ONE_SECOND, count_down, count - 1)
    if count == 0:
        start_timer()
        break_counter.config(text="✔" * (start_timer.counter // 2))


# ---------------------------- UI SETUP ------------------------------- #

# static function variable
start_timer.counter = 1
count_down.timer = None


window = TK.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = TK.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = TK.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT)
canvas.grid(row=1, column=1)

title = TK.Label()
title.config(text="Timer", fg=GREEN, font=FONT_TITLE, bg=YELLOW)
title.grid(row=0, column=1)

start = TK.Button()
start.config(text="Start", font=FONT_BUTTON, highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)


reset = TK.Button()
reset.config(text="Reset", font=FONT_BUTTON, highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

break_counter = TK.Label()
break_counter.config(fg=GREEN, bg=YELLOW, font=FONT)
break_counter.grid(row=3, column=1)

window.mainloop()
