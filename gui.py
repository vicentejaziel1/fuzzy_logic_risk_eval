from tkinter import *


# tab rm
from tkinter.ttk import Treeview


def create_tab(key, tablayout):
    tab = Frame(tablayout)
    tab.pack()
    create_trv(tab, key)

    tablayout.add(tab, text=key['name'])


def create_trv(frame,key):
    trv = Treeview(frame, columns=(1, 2), show='headings', height='6')
    trv.pack(padx = 20, pady = 20, fill="both")
    trv.heading(1, text="Atributo")
    trv.heading(2, text="Peso")

    for value in key['subrisks']:
        trv.insert('', END, values=(value['name'], value['weight']))
