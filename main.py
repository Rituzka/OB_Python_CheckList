import tkinter
from tkinter import Listbox, ttk

window = tkinter.Tk()
window.geometry("250x250")

title = ttk.Label(window, text="Selecciona categorias favoritas:")
title.grid(column=0, row=0, sticky=tkinter.W)

categories = ['Acción', 'Ciencia Ficción', 'Fantasía', 'Comedia', 'Romántica', 'Terror', 'Bélica', 'Biografica', 'De época']
cat_items = tkinter.StringVar(value=categories)
option = Listbox(window, selectmode="multiple", listvariable=cat_items)

option.grid(column=0, row=1, sticky=tkinter.W)

window.mainloop()
