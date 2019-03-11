from tkinter import *
from tkinter import ttk

class RecipesFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.configure(bg='white')

        self._recipes_frame = Frame(self, bg='white')

        self._recipe_label = Label(self._recipes_frame, text='Recipes', bg='white')

        self._recipe_list_scrool_bar = Scrollbar(self._recipes_frame, width=20)

        self._recipe_list = ttk.Treeview(self._recipes_frame, height=7)
        self._recipe_list["columns"] = ("Name", "FROM", "TO")

        self._recipe_list.column('#0', width=40, anchor=CENTER)
        self._recipe_list.heading('#1', text='Name', anchor=CENTER)
        self._recipe_list.column('#1', anchor=CENTER, width=120)
        self._recipe_list.heading('#2', text='FROM', anchor=CENTER)
        self._recipe_list.column('#2', anchor=CENTER, width=100)
        self._recipe_list.heading('#3', text='TO', anchor=CENTER)
        self._recipe_list.column('#3', anchor=CENTER, width=100)
        
        self._recipe_list.insert("", END, text='0',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='0',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='0',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='0',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='0',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='0',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='1',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='2',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='3',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='4',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))
        self._recipe_list.insert("", END, text='5',  values=('Prestance 5/5mg', '12/05/2018', '23/12/2019'))


        self._recipe_detail_frame = Frame(self, bg='white', relief=GROOVE, borderwidth=1, pady=10)

        self._type_label = Label(self._recipe_detail_frame, text='Type', bg='white')
        self._code_label = Label(self._recipe_detail_frame, bg='white', text='Code')
        self._name_label = Label(self._recipe_detail_frame, bg='white', text='Name')
        self._dosage_label = Label(self._recipe_detail_frame, bg='white', text='Dosage')
        self._from_label = Label(self._recipe_detail_frame, bg='white', text='From')
        self._to_label = Label(self._recipe_detail_frame, bg='white', text='To')

        self._type_entry = Label(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._code_entry = Label(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._name_entry = Label(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._dosage_entry = Label(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._from_entry = Label(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)
        self._to_entry = Label(self._recipe_detail_frame, bg='#EEEEEE', state='disabled', relief=FLAT, width=14)


        #Configuration
        self._recipe_list_scrool_bar.config(command=self._recipe_list.yview)


        #Placing
        self._recipes_frame.pack(fill=X, padx=10)

        self._recipe_label.grid(row=0, column=0, columnspan=2, sticky=W, pady=(5,2))
        self._recipe_list.grid(row=1, column=0, sticky=W + E+S+N)
        self._recipe_list_scrool_bar.grid(row=1, column=2, sticky=E + S + N)

        self._recipe_detail_frame.pack(fill=X, pady=10, padx=10)

        self._type_label.grid(row=0, column=0, sticky=W, pady=(5, 5), padx=(10, 5))
        self._code_label.grid(row=1, column=0, sticky=W, pady=(0, 5), padx=(10, 5))
        self._name_label.grid(row=2, column=0, sticky=W, pady=(0, 5), padx=(10, 5))
        self._dosage_label.grid(row=0, column=2, sticky=W, pady=(0, 5), padx=(10, 5))
        self._from_label.grid(row=1, column=2, sticky=W, pady=(0, 5), padx=(10, 5))
        self._to_label.grid(row=2, column=2, sticky=W, pady=(0, 5), padx=(10, 5))

        self._type_entry.grid(row=0, column=1, sticky=W, pady=(0, 5))
        self._code_entry.grid(row=1, column=1, sticky=W, pady=(0, 5))
        self._name_entry.grid(row=2, column=1, sticky=W, pady=(0, 5))
        self._dosage_entry.grid(row=0, column=3, sticky=W, pady=(0, 5))
        self._from_entry.grid(row=1, column=3, sticky=W, pady=(0, 5))
        self._to_entry.grid(row=2, column=3, sticky=W, pady=(0, 5))
