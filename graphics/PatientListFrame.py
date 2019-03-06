from tkinter import *
from tkinter import ttk
from tkinter import font

class PatientListFrame(ttk.Frame):

    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, **kwargs)

        big_font = font.Font(size=11)

        #Components declaration
        self._inside_frame = Frame(self, bg='white')

        self._patient_frame = Frame(self._inside_frame, bg='white')

        self._patient_label = Label(self._patient_frame, text='Patients', bg='white')

        self._patient_list_scrool_bar = Scrollbar(self._patient_frame, width=20)
        self._patient_list = ttk.Treeview(self._patient_frame)
        self._patient_list["columns"] = ("PIN", "Name")

        self._patient_list.column('#0', width=50, anchor=CENTER)
        self._patient_list.heading('#1', text='PIN', anchor=CENTER)
        self._patient_list.column('#1', width=100, anchor=CENTER)
        self._patient_list.heading('#2', text='Name', anchor=CENTER)
        self._patient_list.column('#2', anchor=CENTER)

        self._detail_label = Label(self._inside_frame, text='Detail:', bg='white')
        self._detail_frame = Frame(self._inside_frame, bg='white', relief=GROOVE, borderwidth=1, pady=10)

        self._pin_label = Label(self._detail_frame, text='PIN:', bg='white')
        self._fname_label = Label(self._detail_frame, text='Firstname:', bg='white')
        self._lname_label = Label(self._detail_frame, text='Lastname:', bg='white')
        self._birthday_label = Label(self._detail_frame, text='Birthday:', bg='white')
        self._phone_label = Label(self._detail_frame, text='Phone:', bg='white')
        self._email_label = Label(self._detail_frame, text='Email:', bg='white')
        self._insurance_number_label = Label(self._detail_frame, text='Insurance number:', bg='white')

        self._pin_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._fname_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._lname_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._birthday_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._phone_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._email_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._insurance_number_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)



        self._button_frame = Frame(self._inside_frame, pady=10, bg='white')

        self._add_button = Button(self._button_frame, text='  Add  ', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT)
        self._update_button = Button(self._button_frame, text='Update', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC")
        self._remove_button = Button(self._button_frame, text='Remove', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC")

        self._update_button['state'] = 'disabled'
        self._remove_button['state'] = 'disabled'

        #Set data
        self._patient_list.insert("", END, text='0',  values=('980429/5372', 'Szkandera Ondřej'))
        self._patient_list.insert("", END, text='0',  values=('980429/5372', 'Szkandera Ondřej'))
        self._patient_list.insert("", END, text='0',  values=('980429/5372', 'Szkandera Ondřej'))
        self._patient_list.insert("", END, text='0',  values=('980429/5372', 'Szkandera Ondřej'))

        #Placing
        self._inside_frame.pack(padx=10, pady=10)


        self._patient_frame.grid(row=0, column=0, sticky=W+E+S+N)

        self._patient_label.grid(row=0, column=0, sticky=W)
        self._patient_list.grid(row=1, column=0, columnspan=2, sticky=W+E+S+N)
        self._patient_list_scrool_bar.grid(row=1, column=2, sticky=E+S+N)

        self._detail_label.grid(row=1, column=0, sticky=W, pady=(10, 0))
        self._detail_frame.grid(row=2, column=0, sticky=W+E+S+N)

        self._pin_label.grid(row=0, column=0, sticky=W, pady=(0, 5), padx=5)
        self._fname_label.grid(row=1, column=0, sticky=W, pady=(0, 5), padx=5)
        self._lname_label.grid(row=2, column=0, sticky=W, pady=(0, 5), padx=5)
        self._birthday_label.grid(row=3, column=0, sticky=W, pady=(0, 5), padx=5)
        self._phone_label.grid(row=0, column=2, sticky=W, pady=(0, 5), padx=5)
        self._email_label.grid(row=1, column=2, sticky=W, pady=(0, 5), padx=5)
        self._insurance_number_label.grid(row=2, column=2, sticky=W, pady=(0, 5), padx=5)

        self._pin_entry.grid(row=0, column=1, sticky=W+E+S+N, pady=(0, 5), padx=(0,5))
        self._fname_entry.grid(row=1, column=1, sticky=W+E+S+N, pady=(0, 5), padx=(0,5))
        self._lname_entry.grid(row=2, column=1, sticky=W+E+S+N, pady=(0, 5), padx=(0,5))
        self._birthday_entry.grid(row=3, column=1, sticky=W+E+S+N, pady=(0, 5), padx=(0,5))
        self._phone_entry.grid(row=0, column=3, sticky=W+E+S+N, pady=(0, 5), padx=(0,5))
        self._email_entry.grid(row=1, column=3, sticky=W+E+S+N, pady=(0, 5), padx=(0,5))
        self._insurance_number_entry.grid(row=2, column=3, sticky=W+E+S+N, pady=(0, 5), padx=(0,5))

        self._button_frame.grid(row=3, column=0, rowspan=2, sticky=W + E + S + N)


        self._add_button.grid(row=0, column=0, padx=(0, 10), pady=(10, 0), sticky=W + E + S + N)
        self._update_button.grid(row=0, column=1, padx=10, pady=(10, 0), sticky=W + E + S + N)
        self._remove_button.grid(row=0, column=2, padx=(10, 0), pady=(10, 0), sticky=W + E + S + N)

        #Configuration
        self.configure(bg="white")
        self._patient_list_scrool_bar.config(command=self._patient_list.yview)

        self._button_frame.grid_rowconfigure(0, weight=1)
        self._button_frame.grid_columnconfigure(0, weight=1)
        self._button_frame.grid_columnconfigure(1, weight=1)
        self._button_frame.grid_columnconfigure(2, weight=1)

        self._patient_frame.rowconfigure(1, weight=1)
        self._patient_frame.columnconfigure(0, weight=1)
