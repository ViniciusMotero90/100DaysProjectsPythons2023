from tkinter import *

window  = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="click me", command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()



window.mainloop()