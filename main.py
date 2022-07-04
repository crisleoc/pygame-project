from tkinter import *
from tkinter import ttk
import Puzzle.main as puzzle_game
import Dona.main as dona_game
import TikTakToe.main as tiktaktoe_game
import Pescar.main as fishingGame


def run_puzzle():
    puzzle_game.main()


def run_dona():
    dona_game.main()


def run_tiktak():
    tiktaktoe_game.main()


def run_fishing():
    fishingGame.main()


WIDTH = 640
HEIGHT = 200


def main():
    root = Tk()
    root.geometry(f'{WIDTH}x{HEIGHT}')
    root.configure(bg='beige')
    root.title('Games')
    label = Label(root, text="Selecciona un juego")
    label.pack(anchor=CENTER, pady=10)
    label.config(fg="black", font=(None, 24))

    ttk.Button(root, text='Ejecutar puzzle',
               command=run_puzzle).place(x=120, y=HEIGHT/2.2)
    ttk.Button(root, text='Ejecutar Dona',
               command=run_dona).place(x=220, y=HEIGHT/2.2)
    ttk.Button(root, text='Ejecutar TikTakToe',
               command=run_tiktak).place(x=320, y=HEIGHT/2.2)
    ttk.Button(root, text='Ejecutar Fishing',
               command=run_fishing).place(x=440, y=HEIGHT/2.2)
    root.mainloop()


if __name__ == "__main__":
    main()
