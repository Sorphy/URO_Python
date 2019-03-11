from graphics.MainFrame import MainFrame
from tkinter import *

if __name__ == "__main__":
    root = Tk()
    root.configure(background='white')
    frame = MainFrame(root)

    frame.pack(padx=10, pady=10)


    root.mainloop()
