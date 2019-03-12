from tkinter import *
from utils.PatientBuilder import PatientBuilder
from repository.PatientRepository import PatientRepository
from models.Address import Address
from tkinter import messagebox

class PatientDetailFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.configure(bg="white")

        self._gender = StringVar()
        self._gender.set('M')

        self._general_frame = LabelFrame(self, bg='white', text='General information')

        self._pin_label = Label(self._general_frame, text='PIN', bg='white')
        self._firstname_label = Label(self._general_frame, text='Firstname', bg='white')
        self._lastname_label = Label(self._general_frame, text='Lastname', bg='white')
        self._birthday_label = Label(self._general_frame, text='Birthday', bg='white')
        self._gender_label = Label(self._general_frame, text='Gender', bg='white')
        self._height_label = Label(self._general_frame, text='Height', bg='white')
        self._weight_label = Label(self._general_frame, text='Weight', bg='white')

        self._pin_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=23, justify='center')
        self._firstname_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=23, justify='center')
        self._lastname_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=23, justify='center')
        self._birthday_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=23, justify='center')
        self._m_gender_radio = Radiobutton(self._general_frame, text="M", variable=self._gender, value='M', bg='white')
        self._f_gender_radio = Radiobutton(self._general_frame, text="F", variable=self._gender, value='F', bg='white')
        self._height_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=23, justify='center')
        self._weight_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=23, justify='center')

        self._contact_frame = LabelFrame(self, bg='white', text='Contact')

        self._phone_label = Label(self._contact_frame, text='Phone   ', bg='white')
        self._email_label = Label(self._contact_frame, text='Email', bg='white')

        self._phone_entry = Entry(self._contact_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=23, justify='center')
        self._email_entry = Entry(self._contact_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=23, justify='center')

        self._address_frame = LabelFrame(self, bg='white', text='Address')

        self._city_label = Label(self._address_frame, text='City     ', bg='white')
        self._street_label = Label(self._address_frame, text='Street', bg='white')
        self._zip_code_label = Label(self._address_frame, text='Zip code', bg='white')
        self._postal_code_label = Label(self._address_frame, text='Postal code', bg='white')

        self._city_entry = Entry(self._address_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center')
        self._street_entry= Entry(self._address_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center')
        self._zip_code_entry = Entry(self._address_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center')
        self._postal_code_entry = Entry(self._address_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center')

        self._insurance_frame = LabelFrame(self, bg='white', text='Insurance')

        self._insurance_pin_label = Label(self._insurance_frame, text='PIN      ', bg='white')
        self._insurance_number_label = Label(self._insurance_frame, text='Number     ', bg='white')

        self._insurance_pin_entry = Entry(self._insurance_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center')
        self._insurance_number_entry = Entry(self._insurance_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center')

        self._alergies_frame = LabelFrame(self, bg='white', text='Alergies')

        self._alergies_text = Text(self._alergies_frame, width=23, height=3, bg='#EEEEEE', state='disabled', relief=FLAT)

        self._button_frame = Frame(self, pady=5, bg='white')

        self._button_frame.columnconfigure(0, weight=1)
        self._button_frame.columnconfigure(1, weight=1)

        self._export_button = Button(self._button_frame, text='Export', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT)
        self._save_button = Button(self._button_frame, text=' Save ', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC", command=self._save_patient)


        self._entries = (
            self._firstname_entry,
            self._lastname_entry,
            self._birthday_entry,
            self._height_entry,
            self._weight_entry,
            self._phone_entry,
            self._email_entry,
            self._city_entry,
            self._street_entry,
            self._zip_code_entry,
            self._postal_code_entry,
            self._insurance_pin_entry,
            self._insurance_number_entry,
            self._pin_entry
        )

        #Placing
        self._pin_label.grid(row=0, column=0, sticky=W, padx=(3, 3), pady=(5, 0))
        self._firstname_label.grid(row=1, column=0, sticky=W, padx=(3, 3))
        self._lastname_label.grid(row=2, column=0, sticky=W, padx=(3, 3))
        self._birthday_label.grid(row=3, column=0, sticky=W, padx=(3, 3))
        self._gender_label.grid(row=4, column=0, sticky=W, padx=(3, 3))
        self._height_label.grid(row=5, column=0, sticky=W, padx=(3, 3))
        self._weight_label.grid(row=6, column=0, sticky=W, padx=(3, 3))

        self._pin_entry.grid(row=0, column=1, sticky=W, columnspan=2, pady=(8, 6))
        self._firstname_entry.grid(row=1, column=1, sticky=W, columnspan=2, pady=(3, 3))
        self._lastname_entry.grid(row=2, column=1, sticky=W, columnspan=2, pady=(3, 3))
        self._birthday_entry.grid(row=3, column=1, sticky=W, columnspan=2, pady=(3, 3))
        self._m_gender_radio.grid(row=4, column=1, sticky=W, pady=(3, 3))
        self._f_gender_radio.grid(row=4, column=2, sticky=W, pady=(3, 3))
        self._height_entry.grid(row=5, column=1, sticky=W, columnspan=2, pady=(3, 3))
        self._weight_entry.grid(row=6, column=1, sticky=W, columnspan=2, pady=(3, 0))

        self._general_frame.grid(row=0, column=0, rowspan=2, pady=(10,0), ipadx=5, ipady=5, padx=7, sticky=W+E+S+N)

        self._phone_label.grid(row=0, column=0, sticky=W, padx=(5, 5), pady=(5, 0))
        self._email_label.grid(row=1, column=0, sticky=W, padx=(5, 5), pady=(0, 5))

        self._phone_entry.grid(row=0, column=1, sticky=W, pady=(8, 3))
        self._email_entry.grid(row=1, column=1, sticky=W, pady=(3, 0))

        self._contact_frame.grid(row=2, column=0, pady=2, ipadx=0, ipady=5, padx=7, sticky=W+E+S+N)

        self._city_label.grid(row=0, column=0, sticky=W, padx=(5, 5), pady=(0, 0))
        self._street_label.grid(row=1, column=0, sticky=W, padx=(5, 5))
        self._postal_code_label.grid(row=2, column=0, sticky=W, padx=(5, 5))
        self._zip_code_label.grid(row=3, column=0, sticky=W, padx=(5, 5))

        self._city_entry.grid(row=0, column=1, sticky=W, pady=(3, 6))
        self._street_entry.grid(row=1, column=1, sticky=W, pady=(3, 3))
        self._postal_code_entry.grid(row=2, column=1, sticky=W, pady=(3, 3))
        self._zip_code_entry.grid(row=3, column=1, sticky=W, pady=(3, 0))

        self._address_frame.grid(row=0, column=1, pady=(10,0), ipadx=5, padx=7, sticky=W+E+S+N)

        self._insurance_number_label.grid(row=0, column=0, sticky=W, padx=(5, 5), pady=(5, 0))
        self._insurance_pin_label.grid(row=1, column=0, sticky=W, padx=(5, 5))

        self._insurance_pin_entry.grid(row=0, column=1, sticky=W, pady=(8, 6))
        self._insurance_number_entry.grid(row=1, column=1, sticky=W, pady=(3, 0))

        self._insurance_frame.grid(row=1, column=1, ipadx=5, padx=7, sticky=W+E+S+N)

        self._alergies_text.grid(row=0, column=0, pady=(5, 10), padx=(10,10))

        self._alergies_frame.grid(row=2, column=1)

        self._button_frame.grid(row=3, column=0, ipadx=5, columnspan=2, sticky=W + E + S + N)

        self._export_button.grid(row=0, column=0, sticky=W, pady=(8, 6), padx=(40,0))
        self._save_button.grid(row=0, column=1, sticky=W, pady=(3, 0), padx=(50,0))

    def fill_entries(self, patient):
        self._enable_entries()

        for x in self._entries:
            x.delete(0, END)

        self._alergies_text.delete('1.0', END)

        self._firstname_entry.insert(0, patient.data['fname'])
        self._lastname_entry.insert(0, patient.data['lname'])
        self._birthday_entry.insert(0, patient.data['birthday'])
        self._height_entry.insert(0, patient.data['height'])
        self._weight_entry.insert(0, patient.data['weight'])
        self._phone_entry.insert(0, patient.data['phone'])
        self._email_entry.insert(0, patient.data['email'])
        self._city_entry.insert(0, patient.data['address'].city)
        self._street_entry.insert(0, patient.data['address'].street)
        self._zip_code_entry.insert(0, patient.data['address'].zip_code)
        self._postal_code_entry.insert(0, patient.data['address'].postal_code)
        self._insurance_pin_entry.insert(0, patient.data['insurance_pin'])
        self._insurance_number_entry.insert(0, patient.data['insurance_number'])
        self._pin_entry.insert(0, patient.data['pin'])

        self._gender.set(patient.data['gender'])

        alergies = ', '

        for a in patient.data['alergies']:
            alergies += a  + ', '

        self._alergies_text['state'] = 'normal'
        self._alergies_text.insert(END, alergies[2: len(alergies) - 2])

    def _enable_entries(self):
        for entry in self._entries:
            entry['state'] = 'normal'

    def _save_patient(self):
        fname = self._firstname_entry.get()
        lname = self._lastname_entry.get()
        birthday = self._birthday_entry.get()
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
        pin = self._pin_entry.get()
        gender = self._gender.get()
        alergies_text = self._alergies_text.get('1.0', END)
        alergies = []

        for alergie in alergies_text.split(','):
            alergies.append(alergie)

        patient = PatientBuilder()\
            .set_pin(pin)\
            .set_fname(fname)\
            .set_lname(lname)\
            .set_height(height)\
            .set_weight(weight)\
            .set_insurance_pin(insurance_pin)\
            .set_insurance_number(insurance_number)\
            .set_phone(phone)\
            .set_email(email)\
            .set_gender(gender)\
            .set_address(Address(city, zip_code, postal_code, street))\
            .set_alergies(alergies)\
            .build()

        PatientRepository.get_instance().update(patient)

        messagebox.showinfo("Update", "Pacient succesfully updated")


