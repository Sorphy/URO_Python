from tkinter import *
from repository.PatientRepository import PatientRepository
from utils.PatientBuilder import PatientBuilder
from tkinter import messagebox
from models.Address import Address

class AddPatientFrame(Frame):
    def __init__(self, master, card_frame):
        Frame.__init__(self, master)

        self._master = master
        self._card_frame = card_frame

        self.configure(bg='white')
        
        self._inside_frame = Frame(self, bg='white')

        self._add_patient_label = Label(self._inside_frame, text='Add patient', font='Helvetica 12 bold', bg='white')

        self._pin_label = Label(self._inside_frame, text='PIN:', bg='white')
        self._fname_label = Label(self._inside_frame, text='Firstname:', bg='white')
        self._lname_label = Label(self._inside_frame, text='Lastname:', bg='white')
        self._height_label = Label(self._inside_frame, text='Height:', bg='white')
        self._weight_label = Label(self._inside_frame, text='Weight:', bg='white')
        self._phone_label = Label(self._inside_frame, text='Phone:', bg='white')
        self._email_label = Label(self._inside_frame, text='Email:', bg='white')
        self._insurance_pin_label = Label(self._inside_frame, text='Ins PIN:', bg='white')
        self._insurance_number_label = Label(self._inside_frame, text='Ins Number:', bg='white')
        self._city_label = Label(self._inside_frame, text='City:', bg='white')
        self._street_label = Label(self._inside_frame, text='Street:', bg='white')

        self._zip_postal_code_label = Label(self._inside_frame, text='ZIP/Postal code:', bg='white')

        self._delimiter_label = Label(self._inside_frame, text='/', bg='white')
        self._pin_delimiter_label = Label(self._inside_frame, text='/', bg='white')

        self._alergies_label = Label(self._inside_frame, text='Alergies:', bg='white')

        self._pin_entry_1 = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=12)
        self._pin_entry_2 = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=9)
        self._fname_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._lname_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._height_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._weight_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._phone_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._email_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._insurance_pin_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._insurance_number_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._city_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._street_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)

        self._zip_code_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=12)
        self._postal_code_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=9)

        self._alergies_text = Text(self._inside_frame, width=19, height=3, bg='#EEEEEE',relief=FLAT)

        self._button_frame = Frame(self, pady=5, bg='white')

        self._button_frame.columnconfigure(0, weight=1)
        self._button_frame.columnconfigure(1, weight=1)

        self._cancel_button = Button(self._button_frame, text='Cancel', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, command=self._close)
        self._save_button = Button(self._button_frame, text=' Save ', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC", command=self._save_patient)



        #Placing

        self._inside_frame.grid(row=0, column=0, sticky=W+S+E+N, padx=10, pady=10)

        self._add_patient_label.grid(row=0, column=0, columnspan=4, sticky=W+S+E+N, pady=(0, 10))

        self._pin_label.grid(row=1, column=0, sticky=W, pady=(0, 5), padx=(0,4))
        self._pin_delimiter_label.grid(row=1, column=2, pady=(0, 5), padx=(0,5))
        self._fname_label.grid(row=2, column=0, sticky=W, pady=(0, 5))
        self._lname_label.grid(row=3, column=0, sticky=W, pady=(0, 5))
        self._height_label.grid(row=4, column=0, sticky=W, pady=(0, 5))
        self._weight_label.grid(row=5, column=0, sticky=W, pady=(0, 5))
        self._phone_label.grid(row=6, column=0, sticky=W, pady=(0, 5))
        self._email_label.grid(row=7, column=0, sticky=W, pady=(0, 5))
        self._insurance_pin_label.grid(row=8, column=0, sticky=W, pady=(0, 5))
        self._insurance_number_label.grid(row=9, column=0, sticky=W, pady=(0, 5))
        self._city_label.grid(row=10, column=0, sticky=W, pady=(0, 5))
        self._street_label.grid(row=11, column=0, sticky=W, pady=(0, 5))
        self._zip_postal_code_label.grid(row=12, column=0, sticky=W, pady=(0, 5))
        self._delimiter_label.grid(row=12, column=2, pady=(0, 5))
        self._alergies_label.grid(row=14, column=0, sticky=W)

        self._pin_entry_1.grid(row=1, column=1, sticky=W, pady=(0, 5))
        self._pin_entry_2.grid(row=1, column=3, sticky=W, pady=(0, 5))
        self._fname_entry.grid(row=2, column=1, sticky=W, pady=(0, 5), columnspan=3)
        self._lname_entry.grid(row=3, column=1, sticky=W, pady=(0, 5), columnspan=3)
        self._height_entry.grid(row=4, column=1, sticky=W, pady=(0, 5), columnspan=3)
        self._weight_entry.grid(row=5, column=1, sticky=W, pady=(0, 5), columnspan=3)
        self._phone_entry.grid(row=6, column=1, sticky=W, pady=(0, 5), columnspan=3)
        self._email_entry.grid(row=7, column=1, sticky=W, pady=(0, 5), columnspan=3)
        self._insurance_pin_entry.grid(row=8, column=1, sticky=W, pady=(0, 5), columnspan=3)
        self._insurance_number_entry.grid(row=9, column=1, sticky=W, pady=(0, 5), columnspan=3)
        self._city_entry.grid(row=10, column=1, sticky=W, pady=(0, 5), columnspan=3)
        self._street_entry.grid(row=11, column=1, sticky=W, pady=(0, 5), columnspan=3)

        self._zip_code_entry.grid(row=12, column=1, sticky=W, pady=(0, 5), padx=(0,5))
        self._postal_code_entry.grid(row=12, column=3, sticky=W, pady=(0, 5), padx=(0,5))

        self._alergies_text.grid(row=14, column=1, sticky=W, pady=(0, 5), columnspan=3)

        self._button_frame.grid(row=1, column=0, sticky=W+S+E+N, padx=10, pady=10)

        self._save_button.grid(row=0, column=0)
        self._cancel_button.grid(row=0, column=1)

    def _close(self):
        self._master.destroy()

    def _save_patient(self):
        fname = self._fname_entry.get()
        lname = self._lname_entry.get()
        height = self._height_entry.get()
        weight = self._weight_entry.get()
        phone = self._phone_entry.get()
        email = self._email_entry.get()
        city = self._city_entry.get()
        street = self._street_entry.get()
        zip_code = self._zip_code_entry.get()
        postal_code = self._postal_code_entry.get()
        insurance_pin = self._insurance_pin_entry.get()
        insurance_number = self._insurance_number_entry.get()
        pin = str(self._pin_entry_1.get()) + '/' + str(self._pin_entry_2.get())
        alergies_text = self._alergies_text.get('1.0', END)
        alergies = []

        for alergie in alergies_text.split(','):
            alergies.append(alergie)

        patient = PatientBuilder() \
            .set_pin(pin) \
            .set_fname(fname) \
            .set_lname(lname) \
            .set_height(height) \
            .set_weight(weight) \
            .set_insurance_pin(insurance_pin) \
            .set_insurance_number(insurance_number) \
            .set_phone(phone) \
            .set_email(email) \
            .set_address(Address(city, zip_code, postal_code, street)) \
            .set_alergies(alergies) \
            .build()

        PatientRepository.get_instance().insert(patient)

        messagebox.showinfo("Insert", "Pacient succesfully inserted")

        self._card_frame.fill_list()

        self._master.destroy()
