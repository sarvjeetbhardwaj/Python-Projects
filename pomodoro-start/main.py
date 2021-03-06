import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK="✓"
reps=0
time=None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer_text,text='00:00')

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN *60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps % 8 == 0 :
        count_down(long_break_sec)
        timer.config(text='start', fg=RED)
    elif reps % 2 ==0 :
        count_down(short_break_sec)
        timer.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        timer.config(text='Break', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_mins = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_mins}:{count_sec}')
    if count > 0:
        global time
        time=window.after(1000, count_down, count-1 )
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title('POMODORA')
window.config(padx=100, pady=50, bg=YELLOW)

canvas=tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img=tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100,112 ,image=tomato_img)
timer_text=canvas.create_text(100, 112, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer=tkinter.Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, 'bold'))
timer.grid(column=1, row=0)

check_mark=tkinter.Label(text=CHECK_MARK, bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

start=tkinter.Button(text='Start',command=start_timer)
start.grid(column=0, row=2)

reset=tkinter.Button(text='Reset', command=reset_timer)
reset.grid(column=2, row=2)



window.mainloop()