import tkinter as tk
import random
from tkinter import messagebox


def mover_numero(fila, columna):
    global posicion_vacia
    fila_vacia, col_vacia = posicion_vacia
    if (abs(fila - fila_vacia) + abs(columna - col_vacia)) == 1:
        tablero[fila][columna], tablero[fila_vacia][col_vacia] = tablero[fila_vacia][col_vacia], tablero[fila][columna]
        posicion_vacia = (fila, columna)
        actualizar_tablero()
        verificar_ganador()


def actualizar_tablero():
    for i in range(4):
        for j in range(4):
            if tablero[i][j] == 0:
                botones[i][j].config(text='', state='disabled', bg='lightgrey')
            else:
                botones[i][j].config(text=str(tablero[i][j]), state='normal', bg='sky blue')


def verificar_ganador():
    esperado = list(range(1, 16)) + [0]
    actual = [tablero[i][j] for i in range(4) for j in range(4)]
    if actual == esperado:
        for i in range(4):
            for j in range(4):
                botones[i][j].config(state='disabled')
        messagebox.showinfo("**GANASTE**")


numeros = list(range(1, 16)) + [0]
random.shuffle(numeros)
tablero = [numeros[i * 4:(i + 1) * 4] for i in range(4)]
posicion_vacia = [(i, j) for i in range(4) for j in range(4) if tablero[i][j] == 0][0]


ventana = tk.Tk()
ventana.title("VISCA BARCA")



botones = [[None for _ in range(4)] for a in range(4)]
for i in range(4):
    for j in range(4):
        boton = tk.Button(ventana, text='', font=('Helvetica', 24), width=4, height=2,
                        command=lambda i=i, j=j: mover_numero(i, j))
        boton.grid(row=i, column=j)
        botones[i][j] = boton


actualizar_tablero()

ventana.mainloop()