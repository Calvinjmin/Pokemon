# Python Imports
from tkinter import *


class CustomWindow:
    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Pokemon GUI")
        self.root.config(background="#AAAAAA")

        # Battle Frame
        self.battleFrame = Frame(self.root, width=450, heigh=200)
        self.battleFrame.grid(row=1, column=0, padx=10, pady=10)

        # Selection Frame
        self.selectFrame = Frame(self.root, width=450, heigh=150)
        self.selectFrame.grid(row=2, column=0, pady=10)

    def start(self):
        self.root.mainloop()
