import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog


def main():
    def bloquear():
        for i in range(0, 9):
            Botones[i].config(state="disable")
            Botones[i].config(bg="lightgray")
            Botones[i].config(text=(""))

    def iniciar_juegos():
        for i in range(0, 9):
            Botones[i].config(state="normal")
            Botones[i].config(bg="white")
            Botones[i].config(text=(""))
            X_O.append(i)
            global n_turnos
            n_turnos = 0
        global nj1, nj2
        nj1 = simpledialog.askstring("Nombre Jugadores", "Jugador 1:")
        nj2 = simpledialog.askstring("Nombre Jugadores", "Jugador 2:")
        etiqueta.set("Turno de: " + nj1)

    def cambia(n):
        global turno
        global n_turnos
        if turno == 0:
            Botones[n].config(text=("X"))
            turno = turno+1
            X_O[n] = "X"
            etiqueta.set("Turno de: "+nj2)
        else:
            Botones[n].config(text=("O"))
            turno = turno-1
            X_O.append("O")
            X_O[n] = "O"
            etiqueta.set("Turno de: "+nj1)
        gano()
        n_turnos = n_turnos+1
        if n_turnos == 9 and gano() == False:
            bloquear()
            messagebox.showinfo("Game over", "empate")
            etiqueta.set("Nuevo juego para volver a jugar")
            X_O.clear()
            n_turnos = 0
            turno = 0

    def gano():
        global turno
        if (X_O[0] == X_O[1] == X_O[2] or X_O[3] == X_O[4] == X_O[5]
            or X_O[6] == X_O[7] == X_O[8] or X_O[0] == X_O[3] == X_O[6]
            or X_O[1] == X_O[4] == X_O[7] or X_O[2] == X_O[5] == X_O[8] or
            X_O[0] == X_O[4] == X_O[8]
                or X_O[2] == X_O[4] == X_O[6]) and turno == 0:
            bloquear()
            messagebox.showinfo("Game over", "el ganador es "+nj2)
            etiqueta.set("Nuevo juego para volver a jugar")
            X_O.clear()
            global n_turnos
            n_turnos = 0
            return True
        elif (X_O[0] == X_O[1] == X_O[2] or X_O[3] == X_O[4] == X_O[5]
              or X_O[6] == X_O[7] == X_O[8] or X_O[0] == X_O[3] == X_O[6]
              or X_O[1] == X_O[4] == X_O[7] or X_O[2] == X_O[5] == X_O[8] or
              X_O[0] == X_O[4] == X_O[8]
              or X_O[2] == X_O[4] == X_O[6]) and turno == 1:
            n_turnos = 0
            bloquear()
            messagebox.showinfo("Game Over", "el ganador es "+nj1)
            etiqueta.set("Nuevo juego para volver a jugar")
            X_O.clear()
            turno = 0
            return True
        else:
            return False

    ventana = Tk()
    ventana.geometry("400x500")
    ventana.title("Tres en raya")
    n_turnos = 0
    nj1 = " "
    nj2 = " "
    etiqueta = StringVar()
    global turno
    turno = 0
    Botones = []
    X_O = []
    Boton0 = Button(ventana, width=9, height=3, command=lambda: cambia(0))
    Boton0.place(x=50, y=50)
    Botones.append(Boton0)
    Boton1 = Button(ventana, width=9, height=3, command=lambda: cambia(1))
    Boton1.place(x=150, y=50)
    Botones.append(Boton1)
    Boton2 = Button(ventana, width=9, height=3, command=lambda: cambia(2))
    Boton2.place(x=250, y=50)
    Botones.append(Boton2)
    Boton3 = Button(ventana, width=9, height=3, command=lambda: cambia(3))
    Boton3.place(x=50, y=150)
    Botones.append(Boton3)
    Boton4 = Button(ventana, width=9, height=3, command=lambda: cambia(4))
    Boton4.place(x=150, y=150)
    Botones.append(Boton4)
    Boton5 = Button(ventana, width=9, height=3, command=lambda: cambia(5))
    Boton5.place(x=250, y=150)
    Botones.append(Boton5)
    Boton6 = Button(ventana, width=9, height=3, command=lambda: cambia(6))
    Boton6.place(x=50, y=250)
    Botones.append(Boton6)
    Boton7 = Button(ventana, width=9, height=3, command=lambda: cambia(7))
    Boton7.place(x=150, y=250)
    Botones.append(Boton7)
    Boton8 = Button(ventana, width=9, height=3, command=lambda: cambia(8))
    Boton8.place(x=250, y=250)
    Botones.append(Boton8)
    iniciar = Button(ventana, bg='#29B7C5', fg='black',
                     text="Nuevo Juego", width=13, height=3, command=iniciar_juegos)
    iniciar.place(x=130, y=350)
    etiquetaV = Label(ventana, textvariable=etiqueta)
    etiquetaV.place(x=50, y=30)
    bloquear()
    ventana.mainloop()
