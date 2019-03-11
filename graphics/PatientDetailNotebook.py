from tkinter import *
from tkinter import ttk
from graphics.RecipesFrame import RecipesFrame
from graphics.PatientDetailFrame import PatientDetailFrame

class PatientDetailNotebook(ttk.Notebook):
    def __init__(self, master):
        ttk.Notebook.__init__(self, master)

        self.notebook = ttk.Notebook(master)

        self._style = ttk.Style()
        self._style.configure('TNotebook', background='white')

        self.notebook.pack()

        self._patientDetailFrame = PatientDetailFrame(self.notebook)
        self._recipesFrame = RecipesFrame(self.notebook)

        self.notebook.add(self._patientDetailFrame, text="     Detail     ", padding=5)
        self.notebook.add(self._recipesFrame,       text="     Recipes    ", padding=5)


