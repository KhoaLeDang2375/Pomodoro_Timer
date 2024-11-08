from tkinter import *
import time
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
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

def Reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label_Timer.config(text="Timer")
    label_Check_mark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    label_Timer.config(text="Breaking",fg=RED)
    if(reps%2!=0):
        count_down(work_sec)
        label_Timer.config(text="Working",fg=GREEN)
    if(reps%8==0):
         count_down(long_break_sec)

    if(reps%2==0):
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if(count_min<10):
        count_min=f"0{count_min}"
    if(count_sec<10):
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if(count>0):
        global timer
        timer=window.after(1000,count_down,count-1)
    if(count==0):
        start_timer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks+="✓"
        label_Check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
btn_Start=Button(text="Start",bg="white",highlightthickness=0,command=start_timer)
btn_reset=Button(text="Reset",bg="white",highlightthickness=0,command=Reset_timer)
label_Timer=Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
label_Check_mark=Label(fg=GREEN,bg=YELLOW)
label_Timer.grid(row=0,column=1)
label_Check_mark.grid(row=3,column=1)
btn_Start.grid(row=2,column=0)
btn_reset.grid(row=2,column=2)
canvas=Canvas(width="200",height="224",bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.grid(column=1,row=1)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))













window.mainloop()