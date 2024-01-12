# models/role.py

# class extends the enum.IntEnum base class from the standard library, 
# which provides special semantics for its instances.
from enum import IntEnum, auto

# give each member the next numeric value in turn
# by calling enum.auto()
class Role(IntEnum):
    NONE = 0    # serve as the null object
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()
