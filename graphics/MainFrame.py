from tkinter import *
from tkinter import ttk
from graphics.MainNotebook import MainNotebook

class MainFrame(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.mainNotebook = MainNotebook(self)

