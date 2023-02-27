import os
import sys
import tkinter as tk
from PIL import Image, ImageTk
from typing import Callable
from src.const import TILE_SIZE, WINDOW_SIZE, WINDOW_TITLE

def init_game_window(game_loop_callback: Callable):
    window: tk.Tk = tk.Tk()
    window.geometry(f"{WINDOW_SIZE[0]+TILE_SIZE[0]}x{WINDOW_SIZE[1]+TILE_SIZE[1]}")
    window.resizable(0,0)
    window_icon_img = ImageTk.PhotoImage(Image.open(os.path.join(sys.path[0], "assets/favicon.png")))
    window.wm_iconphoto(True, window_icon_img)
    frame: tk.Frame = tk.Frame(window)
    canvas: tk.Canvas = tk.Canvas(frame)
    canvas.configure(background="black", width=WINDOW_SIZE[0]+TILE_SIZE[0], height=WINDOW_SIZE[1]+TILE_SIZE[1])
    frame.pack()
    canvas.pack(expand=True, fill="both")

    game_loop_callback(window, canvas)

    window.mainloop()
    pass

__all__ = ["init_game_window"]