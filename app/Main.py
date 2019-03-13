from graphics.MainFrame import MainFrame
from tkinter import *
from repository.PatientRepository import PatientRepository

if __name__ == "__main__":
    root = Tk()
    root.configure(background='white')
    frame = MainFrame(root)

    frame.pack(padx=10, pady=10)

    patients = PatientRepository.get_instance().get_all()

    root.mainloop()
