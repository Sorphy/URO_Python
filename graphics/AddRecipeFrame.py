from tkinter import *
from repository.PatientRepository import PatientRepository
from tkinter import messagebox
from models.Recipe import Recipe


class AddRecipeFrame(Frame):
    def __init__(self, master, recipe_frame):
        Frame.__init__(self, master)

        self._master = master
        self._recipe_frame = recipe_frame

        self.configure(bg='white')

        self._inside_frame = Frame(self, bg='white')

        self._add_recipe_label = Label(self._inside_frame, text='Add recipe', font='Helvetica 12 bold', bg='white')

        self._type_label = Label(self._inside_frame, text='Type:', bg='white')
        self._code_label = Label(self._inside_frame, text='Code:', bg='white')
        self._name_label = Label(self._inside_frame, text='Name:', bg='white')
        self._dosage_label = Label(self._inside_frame, text='Dosage:', bg='white')
        self._from_label = Label(self._inside_frame, text='From:', bg='white')
        self._to_label = Label(self._inside_frame, text='To:', bg='white')

        self._type_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._code_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._name_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._dosage_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._from_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)
        self._to_entry = Entry(self._inside_frame, bg='#EEEEEE', relief=FLAT, width=25)

        self._button_frame = Frame(self, pady=5, bg='white')

        self._button_frame.columnconfigure(0, weight=1)
        self._button_frame.columnconfigure(1, weight=1)

        self._cancel_button = Button(self._button_frame, text='Cancel', font='Helvetica 12 bold', padx=20, pady=12,
                                     bg='#1E88E5', fg='white', relief=FLAT, command=self._close)
        self._save_button = Button(self._button_frame, text=' Save ', font='Helvetica 12 bold', padx=20, pady=12,
                                   bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC",
                                   command=self._save_patient)

        # Placing

        self._inside_frame.grid(row=0, column=0, sticky=W + S + E + N, padx=10, pady=10)

        self._add_recipe_label.grid(row=0, column=0, columnspan=2, sticky=W + S + E + N, pady=(0, 10))

        self._type_label.grid(row=1, column=0, sticky=W, pady=(0, 5))
        self._code_label.grid(row=2, column=0, sticky=W, pady=(0, 5))
        self._name_label.grid(row=3, column=0, sticky=W, pady=(0, 5))
        self._dosage_label.grid(row=4, column=0, sticky=W, pady=(0, 5))
        self._from_label.grid(row=5, column=0, sticky=W, pady=(0, 5))
        self._to_label.grid(row=6, column=0, sticky=W, pady=(0, 5))

        self._type_entry.grid(row=1, column=1, sticky=W, pady=(0, 5))
        self._code_entry.grid(row=2, column=1, sticky=W, pady=(0, 5))
        self._name_entry.grid(row=3, column=1, sticky=W, pady=(0, 5))
        self._dosage_entry.grid(row=4, column=1, sticky=W, pady=(0, 5))
        self._from_entry.grid(row=5, column=1, sticky=W, pady=(0, 5))
        self._to_entry.grid(row=6, column=1, sticky=W, pady=(0, 5))

        self._button_frame.grid(row=1, column=0, sticky=W + S + E + N, padx=10, pady=10)

        self._save_button.grid(row=0, column=0, padx=(0,10))
        self._cancel_button.grid(row=0, column=1)

    def _close(self):
        self._master.destroy()

    def _save_patient(self):
        type = self._type_entry.get()
        code = self._code_entry.get()
        name = self._name_entry.get()
        dosage = self._dosage_entry.get()
        from_date = self._from_entry.get()
        to_date = self._to_entry.get()

        recipe = Recipe(type, code, name, dosage, from_date, to_date)

        PatientRepository.get_instance().add_recipe(self._recipe_frame.selected_patient.data['pin'], recipe)

        messagebox.showinfo("Insert", "Recipe succesfully inserted")

        self._recipe_frame.fill_list(self._recipe_frame.selected_patient)

        self._master.destroy()
