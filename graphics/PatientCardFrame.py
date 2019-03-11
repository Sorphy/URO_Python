from tkinter import *
from graphics.PatientDetailNotebook import PatientDetailNotebook

class PatientCardFrame(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)

        self.configure(bg="white")

        #Components
        self._inside_frame = Frame(self, bg='white')

        #Patient info
        self._patient_info_frame = Frame(self._inside_frame, bg='white', borderwidth=1, pady=10, padx=10, highlightbackground="#9E9E9E", highlightcolor="grey", highlightthickness=1)
        self._patient_label = Label(self._patient_info_frame, text='Patient', bg='white')
        self._patient_pin_label = Entry(self._patient_info_frame, bg='#EEEEEE', relief=FLAT, width=14, state=DISABLED)
        self._patient_name_label = Entry(self._patient_info_frame, bg='#EEEEEE', relief=FLAT, width=40, state=DISABLED)

        #self._button_frame = Frame(self, pady=5, bg='white')

        #self._export_button = Button(self._button_frame, text='Export', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT)
        #self._save_button = Button(self._button_frame, text=' Save ', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC")

        #Placig
        self._inside_frame.pack(padx=3, pady=10)

        self._patient_info_frame.grid(row=0, column=0, sticky=W, pady=(10,5))

        self._patient_label.grid(row=0, column=0, padx=(0, 5))
        self._patient_pin_label.grid(row=0, column=1)
        self._patient_name_label.grid(row=0, column=2, padx=(5,0))

        self._patient_detail_notebook = PatientDetailNotebook(self)

        #self._button_frame.pack()

        #self._export_button.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky=W + E + S + N)
        #self._save_button.grid(row=0, column=1, padx=10, pady=(10, 0), sticky=W + E + S + N)


    def say_hello(self):
        print('Hello')