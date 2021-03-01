import tkinter as tk
from random import choice
import time

root = tk.Tk()
root.title('BALL')
frame = tk.Frame(root)
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)

class Ball:
    def __init__(self, x=40, y=450):
        """ Конструктор класса Ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 3
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        canvas.move(self, self.x, self.y)

        # print(self.x, self.y)


ball = Ball()

def moving_ball():
   root.after(20, ball.move())

moving_ball()

tk.mainloop()