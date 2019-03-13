from tkinter import *
from tkinter import ttk
from models.Recipe import Recipe
from repository.PatientRepository import PatientRepository
from tkinter import messagebox
from graphics.AddRecipeFrame import AddRecipeFrame

class RecipesFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.configure(bg='white')

        self._selected_recipe = None
        self.selected_patient = None

        self._recipes_frame = Frame(self, bg='white')

        self._recipe_label = Label(self._recipes_frame, text='Recipes', bg='white')

        self._recipe_list = ttk.Treeview(self._recipes_frame, height=6)

        self._recipe_list_scrool_bar = Scrollbar(self._recipes_frame, width=20, command=self._recipe_list.yview)
        self._recipe_list_scrool_bar.configure(command=self._recipe_list.yview)
        self._recipe_list.configure(yscrollcommand=self._recipe_list_scrool_bar.set)

        self._recipe_list["columns"] = ("Name", "FROM", "TO")

        self._recipe_list.column('#0', width=70, anchor=CENTER)
        self._recipe_list.heading('#1', text='Name', anchor=CENTER)
        self._recipe_list.column('#1', anchor=CENTER, width=150)
        self._recipe_list.heading('#2', text='FROM', anchor=CENTER)
        self._recipe_list.column('#2', anchor=CENTER, width=93)
        self._recipe_list.heading('#3', text='TO', anchor=CENTER)
        self._recipe_list.column('#3', anchor=CENTER, width=93)

        self._recipe_detail_label = Label(self, bg='white', text='Detail')

        self._recipe_detail_frame = Frame(self, bg='white', relief=GROOVE, borderwidth=1, pady=10)

        self._type_label = Label(self._recipe_detail_frame, text='Type', bg='white')
        self._code_label = Label(self._recipe_detail_frame, bg='white', text='Code')
        self._name_label = Label(self._recipe_detail_frame, bg='white', text='Name')
        self._dosage_label = Label(self._recipe_detail_frame, bg='white', text='Dosage')
        self._from_label = Label(self._recipe_detail_frame, bg='white', text='From')
        self._to_label = Label(self._recipe_detail_frame, bg='white', text='To')

        self._type_var = StringVar()
        self._type_var.trace('w', self._on_entry_change_listener)
        self._name_var = StringVar()
        self._name_var.trace('w', self._on_entry_change_listener)
        self._dosage_var = StringVar()
        self._dosage_var.trace('w', self._on_entry_change_listener)
        self._from_var = StringVar()
        self._from_var.trace('w', self._on_entry_change_listener)
        self._to_var = StringVar()
        self._to_var.trace('w', self._on_entry_change_listener)
        self._code_var = StringVar()
        self._code_var.trace('w', self._on_entry_change_listener)

        self._type_entry = Entry(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center', textvariable=self._type_var)
        self._code_entry = Entry(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center', textvariable=self._code_var)
        self._name_entry = Entry(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center', textvariable=self._name_var)
        self._dosage_entry = Entry(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center', textvariable=self._dosage_var)
        self._from_entry = Entry(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center', textvariable=self._from_var)
        self._to_entry = Entry(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=20, justify='center', textvariable=self._to_var)

        self._button_frame = Frame(self, pady=10, bg='white')

        self._add_button = Button(self._button_frame, text='  Add  ', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, command=self._add_recipe)
        self._save_button = Button(self._button_frame, text='Save', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC", command=self._save_recipe)
        self._remove_button = Button(self._button_frame, text='Remove', font='Helvetica 12 bold', padx=20, pady=12, bg='#1E88E5', fg='white', relief=FLAT, disabledforeground="#CFD8DC", command=self._remove_recipe)

        self._save_button['state'] = 'disabled'
        self._remove_button['state'] = 'disabled'


        #Configuration
        self._recipe_list_scrool_bar.config(command=self._recipe_list.yview)


        #Placing
        self._recipes_frame.grid(row=0, column=0, padx=10)

        self._recipe_label.grid(row=0, column=0, columnspan=2, sticky=W, pady=(5,2))
        self._recipe_list.grid(row=1, column=0, sticky=W + E + S + N)
        self._recipe_list_scrool_bar.grid(row=1, column=2, sticky=E + S + N, padx=(1,0))

        self._recipe_detail_label.grid(row=1, column=0, sticky=W, padx=10, pady=(5,0))

        self._recipe_detail_frame.grid(row=2, column=0, sticky=W+E+S+N, padx=10)

        self._type_label.grid(row=0, column=0, sticky=W, pady=(5, 5), padx=(20, 10))
        self._code_label.grid(row=1, column=0, sticky=W, pady=(0, 5), padx=(15, 10))
        self._name_label.grid(row=2, column=0, sticky=W, pady=(0, 5), padx=(15, 10))
        self._dosage_label.grid(row=0, column=2, sticky=W, pady=(5, 5), padx=(35, 10))
        self._from_label.grid(row=1, column=2, sticky=W, pady=(0, 5), padx=(35, 10))
        self._to_label.grid(row=2, column=2, sticky=W, pady=(0, 5), padx=(35, 10))

        self._type_entry.grid(row=0, column=1, sticky=W, pady=(0, 5))
        self._code_entry.grid(row=1, column=1, sticky=W, pady=(0, 5))
        self._name_entry.grid(row=2, column=1, sticky=W, pady=(0, 5))
        self._dosage_entry.grid(row=0, column=3, sticky=W, pady=(0, 5))
        self._from_entry.grid(row=1, column=3, sticky=W, pady=(0, 5))
        self._to_entry.grid(row=2, column=3, sticky=W, pady=(0, 5))

        self._button_frame.grid(row=3, column=0)

        self._add_button.grid(row=0, column=0, padx=(3, 10), pady=(10, 0), sticky=W + E + S + N)
        self._save_button.grid(row=0, column=1, padx=20, pady=(10, 0), sticky=W + E + S + N)
        self._remove_button.grid(row=0, column=2, padx=(5, 0), pady=(10, 0), sticky=E + S + N)

        #Configuration
        self._recipe_list.bind("<ButtonRelease-1>", self._recipe_select_listener)

    def fill_list(self, patient):

        self.selected_patient = patient

        for i in self._recipe_list.get_children():
            self._recipe_list.delete(i)

        temp = 1

        for recipe in patient.data['recipes']:
            self._recipe_list.insert("", END, text=recipe.data['code'], values=(recipe.data['name'], recipe.data['from'], recipe.data['to']))
            temp += 1

    def _recipe_select_listener(self, event):
        cur_item = self._recipe_list.focus()
        selected = self._recipe_list.item(cur_item)

        code = selected['text']

        recipe = [x for x in self.selected_patient.data['recipes'] if x.data['code'] == code]

        self.clear_entries()

        self._type_entry['state'] = 'normal'
        self._code_entry['state'] = 'normal'
        self._name_entry['state'] = 'normal'
        self._dosage_entry['state'] = 'normal'
        self._from_entry['state'] = 'normal'
        self._to_entry['state'] = 'normal'

        try:
            self._type_entry.insert(END, recipe[0].data['type'])
            self._code_entry.insert(END, recipe[0].data['code'])
            self._name_entry.insert(END, recipe[0].data['name'])
            self._dosage_entry.insert(END, recipe[0].data['dosage'])
            self._from_entry.insert(END, recipe[0].data['from'])
            self._to_entry.insert(END, recipe[0].data['to'])
        except:
            pass

        self._selected_recipe = code

        self._remove_button['state'] = 'normal'

    def _on_entry_change_listener(self, *args):
        if self._selected_recipe != None:
            self._save_button['state'] = 'normal'

    def clear_entries(self):
        self._type_entry.delete(0, END)
        self._code_entry.delete(0, END)
        self._name_entry.delete(0, END)
        self._dosage_entry.delete(0, END)
        self._from_entry.delete(0, END)
        self._to_entry.delete(0, END)

    def disable_entries(self):
        self._type_entry['state'] = 'disabled'
        self._code_entry['state'] = 'disabled'
        self._name_entry['state'] = 'disabled'
        self._dosage_entry['state'] = 'disabled'
        self._from_entry['state'] = 'disabled'
        self._to_entry['state'] = 'disabled'

    def enable_entries(self):
        self._type_entry['state'] = 'normal'
        self._code_entry['state'] = 'normal'
        self._name_entry['state'] = 'normal'
        self._dosage_entry['state'] = 'normal'
        self._from_entry['state'] = 'normal'
        self._to_entry['state'] = 'normal'

    def _save_recipe(self):
        type = self._type_entry.get()
        code = self._code_entry.get()
        name = self._name_entry.get()
        dosage = self._dosage_entry.get()
        date_from = self._from_entry.get()
        date_to = self._to_entry.get()

        recipe = Recipe(type, code, name, dosage, date_from, date_to)

        PatientRepository.get_instance().remove_recipe(self.selected_patient.data['pin'], self._selected_recipe)
        PatientRepository.get_instance().add_recipe(self.selected_patient.data['pin'], recipe)

        messagebox.showinfo("Update", "Recipe succesfully updated")

    def _remove_recipe(self):
        PatientRepository.get_instance().remove_recipe(self.selected_patient.data['pin'], self._selected_recipe)
        self.fill_list(self.selected_patient)

        self._save_button['state'] = 'disabled'
        self._remove_button['state'] = 'disabled'

        self.clear_entries()
        self.disable_entries()

    def _add_recipe(self):
        new_recipe_window = Toplevel()
        new_recipe_window.configure(background='white')

        add_recipe_frame = AddRecipeFrame(new_recipe_window, self)

        add_recipe_frame.grid(row=0, column=0)

