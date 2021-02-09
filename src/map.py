from copy import deepcopy
from functools import reduce

from menu import columnify


def Grass():
    return Segment(
        [
            "grass",
            "grass",
        ]
    )


def Hut():
    return Segment(
        [
            " hut ",
            " hut ",
        ]
    )


def Wall():
    return Segment(
        [
            "wall ",
            "wall ",
        ]
    )


def Player():
    return Segment(
        [
            "playe",
            "playe",
        ]
    )


class Segment:
    def __init__(self, view):
        self.view = "\n".join(view)

    def __str__(self):
        return self.view


class Map:
    def __init__(self, get_player_pos):
        self.get_player_pos = get_player_pos

        self.map = [
            [Wall(), Wall(), Wall(), Wall()],
            [Grass(), Grass(), Grass(), Grass()],
            [Grass(), Hut(), Grass(), Grass()],
            [Grass(), Grass(), Grass(), Grass()],
            [Wall(), Wall(), Wall(), Wall()],
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
