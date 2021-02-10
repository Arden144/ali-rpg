from copy import deepcopy
from functools import reduce

from menu import columnify


class Tile:
    view: str
    hard = False
    win = False

    def __str__(self):
        return self.view


class Player(Tile):
    view = """\
playe
playe"""


class Wall(Tile):
    hard = True
    view = """\
wall
wall """


class Hut(Tile):
    view = """\
 hut
 hut """


class Grass(Tile):
    view = """\
grass
grass"""


class Goal(Tile):
    win = True
    view = """\
 win
 win """


class Map:
    def __init__(self, get_player_pos):
        self.get_player_pos = get_player_pos

        self.map = [
            [Wall(), Wall(), Wall(), Wall()],
            [Grass(), Grass(), Grass(), Grass()],
            [Grass(), Hut(), Grass(), Grass()],
            [Grass(), Grass(), Grass(), Grass()],
            [Wall(), Wall(), Wall(), Goal()],
        ]

    def __str__(self):
        x, y = self.get_player_pos()
        map_copy = deepcopy(self.map)
        map_copy[y][x] = Player()

        return "\n".join(
            reduce(
                lambda p, v: p + [*columnify(*map(str, v), sep=" ")],
                map_copy,
                [],
            )
        )

    def get_pos(self, x, y):
        return self.map[y][x]

    @property
    def width(self):
        return len(self.map[0])

    @property
    def height(self):
        return len(self.map)
