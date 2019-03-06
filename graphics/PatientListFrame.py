from tkinter import *
from tkinter import ttk
from tkinter import font

class PatientListFrame(ttk.Frame):

    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, **kwargs)

        big_font = font.Font(size=11)

        #Components declaration
        inside_frame = Frame(self, bg='white')

        self._patient_frame = Frame(inside_frame, bg='white')

        patient_list_scrool_bar = Scrollbar(self._patient_frame, width=20)
        patient_list = ttk.Treeview(self._patient_frame)
        patient_list["columns"] = ("PIN", "Name")

        patient_list.column('#0', width=50, anchor=CENTER)
        patient_list.heading('#1', text='PIN', anchor=CENTER)
        patient_list.column('#1', width=100, anchor=CENTER)
        patient_list.heading('#2', text='Name', anchor=CENTER)
        patient_list.column('#2', anchor=CENTER)

        #TODO: When user press some key, new entry is opened

        self.testEntry = Entry(self._patient_frame)

        patient_list.bind('<Key>', self.entry_test)


        patient_label = Label(self._patient_frame, text='Patients', bg='white')

        detail_label = Label(inside_frame, text='Detail:', bg='white')
        detail_frame = Frame(inside_frame, bg='white', relief=GROOVE, borderwidth=1, pady=10)

        pin_label = Label(detail_frame, text='PIN:', bg='white')
        fname_label = Label(detail_frame, text='Firstname:', bg='white')
        lname_label = Label(detail_frame, text='Lastname:', bg='white')
        birthday_label = Label(detail_frame, text='Birthday:', bg='white')
        phone_label = Label(detail_frame, text='Phone:', bg='white')
        email_label = Label(detail_frame, text='Email:', bg='white')
        insurance_number_label = Label(detail_frame, text='Insurance number:', bg='white')

        pin_entry = Entry(detail_frame, bg='white', state='disabled')
        fname_entry = Entry(detail_frame, bg='white', state='disabled')
        lname_entry = Entry(detail_frame, bg='white', state='disabled')
        birthday_entry = Entry(detail_frame, bg='white', state='disabled')
        phone_entry = Entry(detail_frame, bg='white', state='disabled')
        email_entry = Entry(detail_frame, bg='white', state='disabled')
        insurance_number_entry = Entry(detail_frame, bg='white', state='disabled')

        button_frame = Frame(inside_frame, pady=10, bg='white')

        add_button = Button(button_frame, text='  Add  ', font=big_font, padx=20, pady=12)
        update_button = Button(button_frame, text='Update', font=big_font, padx=20, pady=12)
        remove_button = Button(button_frame, text='Remove', font=big_font, padx=20, pady=12)

        #Set data
        patient_list.insert("", END, text='0',  values=('980429/5372', 'Szkandera Ondřej'))
        patient_list.insert("", END, text='0',  values=('980429/5372', 'Szkandera Ondřej'))
        patient_list.insert("", END, text='0',  values=('980429/5372', 'Szkandera Ondřej'))
        patient_list.insert("", END, text='0',  values=('980429/5372', 'Szkandera Ondřej'))

        #Placing
        inside_frame.pack(padx=10, pady=10)

        self._patient_frame.grid(row=0, column=0, sticky=W+E+S+N)

        patient_label.grid(row=0, column=0, sticky=W)
        patient_list.grid(row=1, column=0, sticky=W+E+S+N)
        patient_list_scrool_bar.grid(row=1, column=1, sticky=E+S+N)

        detail_label.grid(row=2, column=0, sticky=W, pady=(10, 0))
        detail_frame.grid(row=3, column=0, sticky=W+E+S+N)

        pin_label.grid(row=0, column=0, sticky=W, pady=(0, 5), padx=5)
        fname_label.grid(row=1, column=0, sticky=W, pady=(0, 5), padx=5)
        lname_label.grid(row=2, column=0, sticky=W, pady=(0, 5), padx=5)
        birthday_label.grid(row=3, column=0, sticky=W, pady=(0, 5), padx=5)
        phone_label.grid(row=0, column=2, sticky=W, pady=(0, 5), padx=5)
        email_label.grid(row=1, column=2, sticky=W, pady=(0, 5), padx=5)
        insurance_number_label.grid(row=2, column=2, sticky=W, pady=(0, 5), padx=5)

        pin_entry.grid(row=0, column=1, sticky=W, pady=(0, 5), padx=(0,5))
        fname_entry.grid(row=1, column=1, sticky=W, pady=(0, 5), padx=(0,5))
        lname_entry.grid(row=2, column=1, sticky=W, pady=(0, 5), padx=(0,5))
        birthday_entry.grid(row=3, column=1, sticky=W, pady=(0, 5), padx=(0,5))
        phone_entry.grid(row=0, column=3, sticky=W, pady=(0, 5), padx=(0,5))
        email_entry.grid(row=1, column=3, sticky=W, pady=(0, 5), padx=(0,5))
        insurance_number_entry.grid(row=2, column=3, sticky=W, pady=(0, 5), padx=(0,5))

        button_frame.grid(row=4, column=0, rowspan=2, sticky=W + E + S + N)


        add_button.grid(row=0, column=0, padx=(0, 10), pady=10, sticky=W + E + S + N)
        update_button.grid(row=0, column=1, padx=10, pady=10, sticky=W + E + S + N)
        remove_button.grid(row=0, column=2, padx=(10, 0), pady=10, sticky=W + E + S + N)

        #Configuration
        self.configure(bg="white")
        patient_list_scrool_bar.config(command=patient_list.yview)

        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)
        button_frame.grid_columnconfigure(2, weight=1)

        self._patient_frame.rowconfigure(1, weight=1)
        self._patient_frame.columnconfigure(0, weight=1)


    #Todo search entry
    def entry_test(self, event):
        if event.char == 'o':
            self.testEntry.grid(row=1, column=0, sticky=E + S, pady=(0, 2), padx=(0, 2))
            print('o')
        else:
            print('other')
            self.testEntry.grid_remove()