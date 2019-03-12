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
        self._patient_pin_label = Entry(self._patient_info_frame, bg='#EEEEEE', relief=FLAT, width=20, state=DISABLED, justify='center')
        self._patient_name_label = Entry(self._patient_info_frame, bg='#EEEEEE', relief=FLAT, width=45, state=DISABLED, justify='center')

        #Placig
        self._inside_frame.pack(padx=3, pady=10)

        self._patient_info_frame.grid(row=0, column=0, sticky=W, pady=(10,5))

        self._patient_label.grid(row=0, column=0, padx=(0, 5))
        self._patient_pin_label.grid(row=0, column=1)
        self._patient_name_label.grid(row=0, column=2, padx=(5,0))

        self._patient_detail_notebook = PatientDetailNotebook(self)


    def fill_patient_detail_entries(self, data):
        self._patient_detail_notebook.get_patient_detail_frame().fill_entries(data)

        #Fill list in recipe frame
        self._patient_detail_notebook.get_recipe_frame().fill_list(data)

    def fill_patient_info(self, patient):
        self._patient_pin_label['state'] = 'normal'
        self._patient_name_label['state'] = 'normal'
        self._patient_name_label.delete(0, END)
        self._patient_pin_label.delete(0, END)
        self._patient_pin_label.insert(0, patient.data['pin'])
        self._patient_name_label.insert(0, patient.data['fname'] + ' ' + patient.data['lname'])
        self._patient_pin_label['state'] = 'disabled'
        self._patient_name_label['state'] = 'disabled'

