from tkinter import *
from tkinter.ttk import Notebook, Treeview
import numpy as np

import initials as init
import generic_functions as gp
import weight_calc as wc
import gui


def asign_weights(key, matrix):
    wt = wc.weights(matrix)
    nw = gp.normalize(wt)

    for i in range(len(key['subrisks'])):
        key['subrisks'][i - 1]['weight'] = nw[i - 1]


def calculate_risk(attr, level):
    res = [0, 0, 0]
    for i, val in enumerate(attr['subrisks']):
        res = np.array(res) + (np.array(level[i]) * val['weight'])
    return np.around(res, decimals=2)


# importa json vacio
risks = init.risks

# array de matrices de subriesgos
subrisk_matrix = [init.eo_m, init.rm_m, init.pm_m, init.rp_m, init.ps_m, init.t_m]

# calcula peso de riesgos
asign_weights(risks, init.goal_matrix)

# calcula peso de subriesgos
for i in range(len(subrisk_matrix)):
    asign_weights(risks['subrisks'][i - 1], subrisk_matrix[i - 1])

# array de pesos de nivel de riesgo de cada subriesgo
levels = [init.eo_w, init.rm_w, init.pm_w, init.rp_w, init.ps_w, init.t_w]


def run_risk_calculation():
    main_levels = []
    for i, val in enumerate(risks['subrisks']):
        main_levels.append(calculate_risk(val, levels[i]))

    risk_levels = calculate_risk(risks, main_levels)
    trv = Treeview(root, columns=(1, 2), show='headings', height='6')

    trv.heading(1, text="Nivel")
    trv.heading(2, text="Peso")

    trv.insert('', END, values=('Riesgo Alto', risk_levels[0]))
    trv.insert('', END, values=('Riesgo Medio', risk_levels[1]))
    trv.insert('', END, values=('Riesgo Bajo', risk_levels[2]))

    trv.pack(padx=20, pady=20)


# Interfaz
root = Tk()
root.geometry("1200x680")

frame1 = LabelFrame(root, text="Evaluacion de riesgo para un proyecto TI")
frame1.pack(fill="both", padx=10, pady=10)

frame2 = Frame(root)
frame2.pack(fill="both", padx=10, pady=10)

gui.create_trv(frame1, risks)

tablayout = Notebook(frame2)

for i in range(len(risks['subrisks'])):
    gui.create_tab(risks['subrisks'][i], tablayout)

tablayout.pack(fill="both")

btn = Button(root, text='Generar estimación', command=lambda: run_risk_calculation())

btn.pack()

root.mainloop()

# print(json.dumps(risks, indent=4, sort_keys=True))
