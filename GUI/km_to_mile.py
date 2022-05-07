import tkinter

#window creation
window=tkinter.Tk()
window.title('Mile to km Converter')

#input box
input=tkinter.Entry()
input.grid(column=1, row=0)

#label_creation
is_equal_to_label=tkinter.Label(text='is equal to')
is_equal_to_label.grid(column=0, row=1)

miles_label=tkinter.Label(text='Miles')
miles_label.grid(column=2, row=0)

km_label=tkinter.Label(text='Km')
km_label.grid(column=2, row=1)

calculate_button=tkinter.Button(text='Calculate')
calculate_button.grid(column=1,row=2)

final_value_label=tkinter.Label(text='0')
final_value_label.grid(column=1, row=1)

def button_clicked():
    final_value_label.config(text=str(round(float(input.get())*1.6,1)))

calculate_button=tkinter.Button(text='Calculate',command=button_clicked)
calculate_button.grid(column=1,row=2)

window.mainloop()