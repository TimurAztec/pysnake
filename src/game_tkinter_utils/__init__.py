import tkinter as tk
from typing import Callable
from src.const import WINDOW_SIZE, WINDOW_TITLE

def init_game_window(game_loop_callback: Callable):
    window: tk.Tk = tk.Tk()
    window.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")
    window.resizable(0,0)
    window.iconbitmap("assets/snake.ico")
    frame: tk.Frame = tk.Frame(window)
    canvas: tk.Canvas = tk.Canvas(frame)
    canvas.configure(background="black", width=WINDOW_SIZE[0], height=WINDOW_SIZE[1])
    frame.pack()
    canvas.pack(expand=True, fill="both")

    game_loop_callback(window, canvas)

    window.mainloop()
    pass

__all__ = ["init_game_window"]