from src.const import TILE_SIZE, TILEMAP_WIDTH, TILEMAP_HEIGHT
from copy import deepcopy

class Snake():

    append_on_next_move: bool = False
    append_color: str = "yellow"

    def __init__(self, canvas):
        self._canvas = canvas
        self._pieces = [
            {
                "position": [TILEMAP_WIDTH/2, TILEMAP_HEIGHT/2],
                "canvas_id": self._canvas.create_rectangle(0, 0, TILE_SIZE[0], TILE_SIZE[1], fill="white", outline="")
            }
        ]
        self._direction = [0, 0]

    def change_direction(self, key: str):
        if key == "left":
            if len(self._pieces) > 1 and self._direction == [1, 0]:
                return
            self._direction = [-1, 0]
        if key == "right":
            if len(self._pieces) > 1 and self._direction == [-1, 0]:
                return
            self._direction = [1, 0]
        if key == "up":
            if len(self._pieces) > 1 and self._direction == [0, 1]:
                return
            self._direction = [0, -1]
        if key == "down":
            if len(self._pieces) > 1 and self._direction == [0, -1]:
                return
            self._direction = [0, 1]
        pass

    def move(self) -> bool:
        if self.append_on_next_move:
            self._pieces.append({
                "position": [self._pieces[-1]["position"][0], self._pieces[-1]["position"][1]],
                "canvas_id": self._canvas.create_rectangle(0, 0, TILE_SIZE[0], TILE_SIZE[1], fill=self.append_color, outline="")
            })
            self.append_on_next_move = False

        old_pieces = deepcopy(self._pieces)
        self._pieces[0]["position"][0] += self._direction[0]
        self._pieces[0]["position"][1] += self._direction[1]

        for i, piece in enumerate(self._pieces):
            if i > 0:
                if self._pieces[0]["position"] == piece["position"]:
                    return True
                piece["position"] = old_pieces[i - 1]["position"]
            if piece["position"][0] > TILEMAP_WIDTH:
                piece["position"][0] = 0
            if piece["position"][0] < 0:
                piece["position"][0] = TILEMAP_WIDTH

            if piece["position"][1] > TILEMAP_HEIGHT:
                piece["position"][1] = 0
            if piece["position"][1] < 0:
                piece["position"][1] = TILEMAP_HEIGHT
            self._canvas.moveto(tagOrId=piece["canvas_id"], x=piece["position"][0] * TILE_SIZE[0], y=piece["position"][1] * TILE_SIZE[1])
        
        return False

    def collides_with_tile(self, tile_position) -> bool:
        for piece in self._pieces:
            if piece["position"] == tile_position:
                return True
        return False

    def append_piece(self):
        self.append_on_next_move = True
        self.append_color = "yellow" if self.append_color == "blue" else "blue"
        pass
