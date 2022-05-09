import math
from random import randrange
import tkinter as tk
from PIL import ImageTk, Image
from typing import List

from src.const import TILE_SIZE, TILEMAP_WIDTH, TILEMAP_HEIGHT
from src.game.snake import Snake


class Food():

    _position: List[int] = [0, 0]

    def __init__(self, canvas: tk.Canvas, snake: Snake):
        self._canvas = canvas
        pos_generated: bool = False
        while(not pos_generated):
            self._position = [math.floor(randrange(0, TILEMAP_WIDTH)), math.floor(randrange(0, TILEMAP_HEIGHT))]
            if not snake.collides_with_tile(self.position):
                pos_generated = True
        # self._canvas_id = self._canvas.create_rectangle(0, 0, TILE_SIZE[0], TILE_SIZE[1], fill="red")
        self._img_asset = ImageTk.PhotoImage(Image.open("assets/bug.png").resize(size=(16, 16)))
        self._canvas_id = canvas.create_image(0, 0, image=self._img_asset)
        self._canvas.moveto(tagOrId=self._canvas_id, x=self._position[0] * TILE_SIZE[0], y=self._position[1] * TILE_SIZE[1])
        pass

    @property
    def position(self) -> List[int]:
        return self._position

    def destroy(self):
        self._canvas.delete(self._canvas_id)
        pass

