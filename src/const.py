from typing import Final, List
import math

WINDOW_TITLE: Final[str] = "Score: "
WINDOW_SIZE: Final[List[int]] = [320, 320]
TILE_SIZE: Final[List[int]] = [16, 16]
TILEMAP: Final[List[int]] = [[0] * math.floor(WINDOW_SIZE[0]/TILE_SIZE[0])] * math.floor(WINDOW_SIZE[1]/TILE_SIZE[1])
TILEMAP_WIDTH: Final[int] = math.floor(WINDOW_SIZE[0]/TILE_SIZE[0])
TILEMAP_HEIGHT: Final[int] = math.floor(WINDOW_SIZE[1]/TILE_SIZE[1])