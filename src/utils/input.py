import re
from socket import timeout
from tkinter import LAST
import keyboard

LAST_KEY_PRESSED: str = ""

def change_last_key_pressed(key: str):
    global LAST_KEY_PRESSED
    LAST_KEY_PRESSED = key
    pass

def get_last_key_pressed() -> str:
    global LAST_KEY_PRESSED
    return LAST_KEY_PRESSED

def set_last_key_pressed(key: str):
    global LAST_KEY_PRESSED
    LAST_KEY_PRESSED = key
    pass

def is_space_pressed() -> bool:
    return keyboard.is_pressed(" ")

def init_hotkeys():
    global keyboard
    keyboard.add_hotkey("left", lambda: change_last_key_pressed("left"), timeout=1)
    keyboard.add_hotkey("right", lambda: change_last_key_pressed("right"), timeout=1)
    keyboard.add_hotkey("up", lambda: change_last_key_pressed("up"), timeout=1)
    keyboard.add_hotkey("down", lambda: change_last_key_pressed("down"), timeout=1)
    keyboard.add_hotkey(" ", lambda: change_last_key_pressed("space"), timeout=1000)
    pass

__all__ = ["get_last_key_pressed", "set_last_key_pressed", "init_hotkeys"]