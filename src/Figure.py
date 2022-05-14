import copy
from enum import Enum
import json

import numpy

class Color(Enum):
    White: str = 'w'
    Black: str = 'b'

class FigureCode(Enum):
    Pawn: str = 'p'
    King: str = 'k'
    Knight: str = 'n'
    Bishop: str = 'b'
    Space: str = '0'
    Queen: str = 'q'
    Rook: str = 'r' # should be last because of broken black on black pattern


class Figure(object):
    def __init__(self, code: FigureCode, color: Color, x: int, y: int, w: int, h: int):
        self.color = color
        self.code = code
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def __str__(self) -> str:
        return self.code.value.upper() if self.color == Color.White else self.code.value.lower()

class FigureEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Figure):
            d = copy.deepcopy(obj.__dict__)
            d['color'] = obj.color.value
            d['code'] = obj.code.value
            return d
        elif isinstance(obj, numpy.integer):
            return int(obj)
        if isinstance(obj, numpy.floating):
            return float(obj)
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()

        return json.JSONEncoder.default(self, obj)