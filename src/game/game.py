import tkinter as tk
from playsound import playsound
from typing import Dict
from src.const import WINDOW_TITLE
from src.game.food import Food
from src.game.snake import Snake
from src.utils.input import get_last_key_pressed, set_last_key_pressed

WINDOW: tk.Tk = None
CANVAS: tk.Canvas = None

ENTITIES: Dict = {}
SCORE: int = 0

def init_game_loop(window: tk.Tk, canvas: tk.Canvas):
    global WINDOW, CANVAS, ENTITIES, SCORE
    WINDOW = window
    CANVAS = canvas
    SCORE = 0
    WINDOW.title(WINDOW_TITLE + str(SCORE))
    set_last_key_pressed("")
    init_game_entities()
    game_loop()
    pass

def game_loop():
    global WINDOW, CANVAS, ENTITIES, SCORE
    if get_last_key_pressed():
        ENTITIES["snake"].change_direction(get_last_key_pressed())
    if ENTITIES["snake"].move():
        playsound("assets/death.mp3", block=True)
        init_game_loop(WINDOW, CANVAS)
        return
    if ENTITIES.get("food") and ENTITIES["snake"].collides_with_tile(ENTITIES.get("food").position):
        ENTITIES["snake"].append_piece()
        ENTITIES["food"].destroy()
        ENTITIES["food"] = Food(CANVAS, ENTITIES["snake"])
        playsound("assets/eat.mp3", block=False)
        SCORE += 1
        WINDOW.title(WINDOW_TITLE + str(SCORE))

    WINDOW.after(200, game_loop)
    pass

def init_game_entities():
    global CANVAS, ENTITIES
    CANVAS.delete("all")
    ENTITIES.clear()
    ENTITIES["snake"] = Snake(CANVAS)
    ENTITIES["food"] = Food(CANVAS, ENTITIES["snake"])
    pass

__all__ = ["init_game_loop"]