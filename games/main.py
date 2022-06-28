from tkinter import *
from tkinter import ttk
import Puzzle.main as puzzle_game
import Dona.main as dona_game
import TikTakToe.main as tiktaktoe_game


def run_puzzle():
    puzzle_game.main()


def run_dona():
    dona_game.main()


def run_tiktak():
    tiktaktoe_game.main()


def main():
    root = Tk()
    root.geometry('640x640')
    root.configure(bg='beige')
    root.title('Games')
    ttk.Button(root, text='Ejecutar puzzle',
               command=run_puzzle).place(x=100, y=300)
    ttk.Button(root, text='Ejecutar Dona',
               command=run_dona).place(x=200, y=300)
    ttk.Button(root, text='Ejecutar TikTakToe',
               command=run_tiktak).place(x=300, y=300)
    root.mainloop()


if __name__ == "__main__":
    main()
