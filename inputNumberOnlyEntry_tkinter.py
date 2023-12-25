from tkinter import *
from tkinter import ttk
from tools import *

form = Tk()
form.geometry("700x500")
tkcenter(form)
def number_only(text):
    if str.isdigit(text):
        return True
    else:
        return False

reg_fun =form.register(number_only)
txt=ttk.Entry(form,validate="key",validatecommand=(reg_fun,"%P"))
txt.pack(pady=10)
fontall(form,"None 20")
form.mainloop()

