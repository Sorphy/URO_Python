from tkinter import *
from tkinter import ttk
from tkinter import font
from repository.PatientRepository import PatientRepository

class PatientListFrame(ttk.Frame):

    def __init__(self, master, **kwargs):
        Frame.__init__(self, master)

        self._selected_patient = None

        self._patient_card = kwargs['card']

        self._master = master

        self._patient_repository = PatientRepository.get_instance()

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
        self._insurance_number_label = Label(self._detail_frame, text='Ins PIN:', bg='white')

        self._pin_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20)
        self._fname_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20)
        self._lname_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20)
        self._birthday_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20)
        self._phone_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20)
        self._email_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20)
        self._insurance_number_entry = Label(self._detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20)

        self._entries = (self._pin_entry,
                         self._fname_entry,
                         self._lname_entry,
                         self._birthday_entry,
                         self._phone_entry,
                         self._email_entry,
                         self._insurance_number_entry)



        self._button_frame = Frame(self._inside_frame, pady=10, bg='white')

        self._add_button = Button(self._button_frame, text='  Add  ', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT)
        self._update_button = Button(self._button_frame, text='Update', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC")
        self._remove_button = Button(self._button_frame, text='Remove', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC", command=self._remove_patient)

        self._update_button['state'] = 'disabled'
        self._remove_button['state'] = 'disabled'

        self._fill_list()

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

        #Bind click listener to tree view
        self._patient_list.bind("<ButtonRelease-1>", self._patient_select_listener)
        self._patient_list.bind('<Double-Button-1>', self._show_detail)

        self._button_frame.grid_rowconfigure(0, weight=1)
        self._button_frame.grid_columnconfigure(0, weight=1)
        self._button_frame.grid_columnconfigure(1, weight=1)
        self._button_frame.grid_columnconfigure(2, weight=1)

        self._patient_frame.rowconfigure(1, weight=1)
        self._patient_frame.columnconfigure(0, weight=1)

    def _fill_list(self):
        for i in self._patient_list.get_children():
            self._patient_list.delete(i)

        temp = 1
        for patient in self._patient_repository.get_all():
            self._patient_list.insert("", END, text=str(temp), values=(patient.data['pin'], patient.data['fname'] + " " + patient.data['lname']), tags=('clickable'))
            temp += 1

    def _patient_select_listener(self, event):
        cur_item = self._patient_list.focus()
        selected = self._patient_list.item(cur_item)

        pin = selected['values'][0]

        self._selected_patient = pin

        patient = self._patient_repository.get_by_pin(pin)

        self._pin_entry['text'] = patient.data['pin']
        self._fname_entry['text'] = patient.data['fname']
        self._lname_entry['text'] = patient.data['lname']
        self._birthday_entry['text'] = patient.data['birthday']

        self._phone_entry['text'] = patient.data['phone']
        self._email_entry['text'] = patient.data['email']
        self._insurance_number_entry['text'] = patient.data['insurance_number']

        self._update_button['state'] = 'normal'
        self._remove_button['state'] = 'normal'

    def _remove_patient(self):
        self._patient_repository.remove(self._selected_patient)

        self._fill_list()

        for entry in self._entries:
            entry['text'] = ''

        self._update_button['state'] = 'disabled'
        self._remove_button['state'] = 'disabled'

    def _show_detail(self, event):
        self._master.select(1)
        self._patient_card.say_hello()




