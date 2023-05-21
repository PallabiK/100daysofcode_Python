from tkinter import *

def miles_to_km():
    km = round(float(miles_input.get())*1.60934, 3)
    km_result.config(text=km)

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)

#Entry
miles_input = Entry(width=7)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)


#Label
miles = Label(text="Miles")
miles.grid(column=2, row=0)

equal = Label(text="is equal to")
equal.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()