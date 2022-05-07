BACKGROUND='#ADD8E6'
import tkinter
import pandas as pd
import random

################################## Reading the data csv ###############################################
df=pd.read_csv('data/french_words.csv')
data_dict={}

#################################Converting the data into dictionary
for french, english in zip(df['French'], df['English']):
    data_dict[french]=english



############### Next_Card_Button_Action #############################################################################
def next_card():
    global choice, flip_timer
    window.after_cancel(flip_timer)
    choice=random.choice(list(data_dict.keys()))
    canvas.itemconfig(title,text=f'French',fill='black')
    canvas.itemconfig(word,text=choice,fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer=window.after(3000,func=flip_card)

############## Flip_Card after 3 sec #################################################################################
def flip_card():
    canvas.itemconfig(title,text=f'English',fill='white')
    canvas.itemconfig(word,text=data_dict[choice], fill='white')
    canvas.itemconfig(card_background, image=card_back)

############################# Creating GUI ############################################
window=tkinter.Tk()
window.title('Flash Card Game')
window.config(width=1000, height=1000, bg=BACKGROUND,padx=50,pady=50)

flip_timer=window.after(3000,func=flip_card)

canvas=tkinter.Canvas(width=800, height=526)
card_front=tkinter.PhotoImage(file='images/card_front.png')
card_background=canvas.create_image(400,263 , image=card_front)

card_back = tkinter.PhotoImage(file='images/card_back.png')

title=canvas.create_text(400,150,text='',font=("Courier",35, "bold"))
word=canvas.create_text(400,263,text='',font=("Courier",40, "bold"))
canvas.config(bg=BACKGROUND,highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

right_img=tkinter.PhotoImage(file='images/right.png')
wrong_img=tkinter.PhotoImage(file='images/wrong.png')

right_button=tkinter.Button(image=right_img, command=next_card)
right_button.grid(column=0, row=1)
right_button.config(highlightthickness=0)

wrong_button=tkinter.Button(image=wrong_img, command=next_card)
wrong_button.grid(column=1, row=1)
wrong_button.config(highlightthickness=0)

next_card()

window.mainloop()

