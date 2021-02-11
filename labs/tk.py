import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text='Full name')
resultContents = tk.StringVar()
label['textvariable'] = resultContents
resultContents.set('New value to display')
label.pack()
# Or button

button = tk.Button(
    text="Click me!",
    width=25,
    background='black',
    foreground='white'
)

button.pack()
# Entry
entry = tk.Entry(foreground='yellow', background='blue', width=50)
entry.pack()
# textBox = tk.TextBox()
textBox = tk.Text()
textBox.pack()


frame = tk.Frame(window, width=100, height=100)
frame['borderwidth'] = 2
frame['relief'] = 'sunken'
frame.pack()

window.mainloop()
