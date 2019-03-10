from tkinter import *
from tkinter import ttk
from graphics.PatientCardFrame import PatientCardFrame
from graphics.PatientListFrame import PatientListFrame


class MainNotebook(ttk.Notebook):
    def __init__(self, master):
        ttk.Notebook.__init__(self, master)

        self.notebook = ttk.Notebook(master)

        self.notebook.pack()

        self.patientListFrame = PatientListFrame(self.notebook)
        self.patientCardFrame = PatientCardFrame(self.notebook)

        self.notebook.add(self.patientListFrame, text="     List     ", padding=5)
        self.notebook.add(self.patientCardFrame, text="     Card     ")


