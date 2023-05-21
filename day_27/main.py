from tkinter import *

def button_clicked():
    my_label.config(text=input.get())

window = Tk()
window.title("Here's a GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)


#Label
my_label = Label(text="Label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.pack()
# my_label.place(x=200, y=130)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#Button
button = Button(text="Click", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button =Button(text="Clickster", command=button_clicked)
new_button.grid(column=3, row=0)

#Entry
input = Entry(width = 10)
# input.pack()
input.grid(column=4, row=2)








window.mainloop()

