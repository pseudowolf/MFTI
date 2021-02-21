import tkinter as tk
from tkinter import ttk



class MainView(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.name = tk.StringVar()
        self.helloString = tk.StringVar()
        self.helloString.set('Hello, world!')

        nameLabel = ttk.Label(self, text='Name:')
        nameEntry = ttk.Entry(self, textvariable=self.name)
        chButton = ttk.Button(self, text='Change', command=self.on_change)
        helloLabel = ttk.Label(self,
                               textvariable=self.helloString,
                               font=('TkDefaultFont', 64),
                               wraplength=600)

        nameLabel.grid(row=0, column=0, sticky=tk.W)
        nameEntry.grid(row=0, column=1, sticky=tk.W + tk.E)
        chButton.grid(row=0, column=2, sticky=tk.E)
        helloLabel.grid(row=1, column=0, columnspan=3)

        self.columnconfigure(1, weight=1)

    def on_change(self):
        if self.name.get().strip():
            self.helloString.set('Hello ' + self.name.get() + '!')
        else:
            self.helloString.set('Hello, world!')


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Hello Tkinter')
        self.geometry('800x600')
        self.resizable(width=False, height=False)

        MainView(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()

