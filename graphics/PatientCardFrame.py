from tkinter import *

class PatientCardFrame(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.configure(bg="white")

        self.b = Button(self, text='LLLLLLLLLLLL')
        self.b.grid(row=0, column=0)
