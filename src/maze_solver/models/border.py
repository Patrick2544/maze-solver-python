# models/border.py

from enum import IntFlag, auto

class Border(IntFlag):
    EMPTY = 0   # serve as the null object
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()