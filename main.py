from tkinter import *

# Miles to Km Function
def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
# my_label.config(padx=50, pady=50)

# Label 2
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# Label 3
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

# Label 4
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
