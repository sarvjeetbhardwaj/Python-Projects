import tkinter
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password=''

    for l in range(1,9):
        password += random.choice(letters)
    for n in range(1,5):
        password +=random.choice(numbers)
    for s in range(1,5):
        password += random.choice(symbols)

    password_input.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website_address=website_input.get()
    email=email_input.get()
    password=password_input.get()
    json_data={
        website_address:{
        'email': email,
        'password':password
    }
    }

    if len(website_address) == 0 or len(password) == 0:
        messagebox.showerror(title='Mandatory fields empty', message='website_address or email cannot be empty')

    else:
        try:
            with open('data.json', 'r') as f:
                #reading the data
                data = json.load(f)
                #updating the new data
                data.update(json_data)
        except:
            with open('data.json', 'w') as f:
                json.dump(json_data, f, indent=4)
        else:
        #writing the data
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)

        website_input.delete(0, tkinter.END)
        password_input.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window=tkinter.Tk()
window.title('Password Manager')
window.config(padx=100, pady=50)

canvas=tkinter.Canvas(width=200,height=189)
pass_image=tkinter.PhotoImage(file='logo.png')
canvas.create_image(100,94, image=pass_image)
canvas.grid(column=1, row=0)

website_label=tkinter.Label(text='Website')
website_label.grid(column=0, row=1)


email_label=tkinter.Label(text='Email/Username')
email_label.grid(column=0, row=2)

password_label=tkinter.Label(text='Password')
password_label.grid(column=0, row=3)

website_input=tkinter.Entry(width=35)
website_input.grid(column=1, row=1 , columnspan=2)
website_input.focus()


email_input=tkinter.Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0,'sjitbh121993@gmail.com')

password_input=tkinter.Entry(width=21)
password_input.grid(column=1, row=3)

generate_password=tkinter.Button(text='Generate Password',command=password_generator)
generate_password.grid(column=2, row=3)


add_values=tkinter.Button(text='Add', width=36, command=save_data)
add_values.grid(column=1, row=4, columnspan=2)




window.mainloop()


