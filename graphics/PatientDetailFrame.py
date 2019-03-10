from tkinter import *

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

        self._pin_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._firstname_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._lastname_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._birthday_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._m_gender_radio = Radiobutton(self._general_frame, text="M", variable=self._gender, value='M', bg='white')
        self._f_gender_radio = Radiobutton(self._general_frame, text="F", variable=self._gender, value='F', bg='white')
        self._height_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._weight_entry = Entry(self._general_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)

        self._contact_frame = LabelFrame(self, bg='white', text='Contact')

        self._phone_label = Label(self._contact_frame, text='Phone   ', bg='white')
        self._email_label = Label(self._contact_frame, text='Email', bg='white')

        self._phone_entry = Entry(self._contact_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._email_entry = Entry(self._contact_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)

        self._address_frame = LabelFrame(self, bg='white', text='Address')

        self._city_label = Label(self._address_frame, text='City     ', bg='white')
        self._street_label = Label(self._address_frame, text='Street', bg='white')
        self._zip_code_label = Label(self._address_frame, text='Zip code', bg='white')
        self._postal_code_label = Label(self._address_frame, text='Postal code', bg='white')

        self._city_entry = Entry(self._address_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._street_entry= Entry(self._address_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._zip_code_entry = Entry(self._address_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._postal_code_entry = Entry(self._address_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)

        self._insurance_frame = LabelFrame(self, bg='white', text='Insurance')

        self._insurance_pin_label = Label(self._insurance_frame, text='PIN      ', bg='white')
        self._insurance_number_label = Label(self._insurance_frame, text='Number     ', bg='white')

        self._insurance_pin_entry = Entry(self._insurance_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)
        self._insurance_number_entry = Entry(self._insurance_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=16)

        self._alergies_frame = LabelFrame(self, bg='white', text='Alergies')

        self._alergies_text = Text(self._alergies_frame, width=20, height=3, bg='#EEEEEE', state='disabled', relief=FLAT)

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

        self._alergies_text.grid(row=0, column=0, pady=(10, 10), padx=(10,10))

        self._alergies_frame.grid(row=2, column=1)