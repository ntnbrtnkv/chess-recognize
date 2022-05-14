
import json
import statistics
import sys
import bisect
import re

from Figure import FigureCode, FigureEncoder
from Recognition import Figure
from log import get_logger

logger = get_logger('OKChess')

def optimize_fen(s):
    return re.sub(f'{FigureCode.Space.value}+', lambda m: str(len(m[0])), s)

class Board:
    def __init__(self):
        self.figures = None
        self.fen_list: list[str] = ['', '', '', '', '', '', '', '']
        self.sorted_figures: list[list[Figure]] = []
        self.space = 0
        self.width = 0

    def set_space(self, figures: "list[Figure]"):
        found = next((f for f in figures if f.code == FigureCode.Space), figures[0])
        self.space = found.w * 3 / 4

    def set_figures(self, figures: "list[Figure]"):
        self.figures = figures
        self.set_space(figures)
        self.set_max_width(figures)
        logger.debug('Figures setted: ' + json.dumps(self.figures, indent=4, cls=FigureEncoder))

    def set_max_width(self, figures: "list[Figure]"):
        widths = [f.w for f in figures]
        self.width = statistics.median(widths)

    def d(self, a, b):
        return abs(a - b)

    def get_left_coord(self):
        x = sys.maxsize
        for f in self.figures:
            x = min(x, f.x)
        return x

    def sort_figures(self) -> "list[list[Figure]]":
        res = [[], [], [], [], [], [], [], []]
        for f in self.figures:
            for i in range(0, 8):
                line = res[i]
                if len(line) == 0:
                    res[i].append(f)
                    break
                fr = line[0]
                if self.d(fr.y, f.y) <= self.space:
                    bisect.insort(res[i], f, key=lambda a: a.x)
                    break
        res.sort(key=lambda x: sys.maxsize if len(x) == 0 else x[0].y)

        logger.debug('Figures sorted: ' + json.dumps(res, indent=4, cls=FigureEncoder))

        self.sorted_figures = res

        return res

    def process_fen_line(self, ind: int):
        logger.debug('Start processing FEL line: ' + str(ind))
        x = self.get_left_coord()
        res = ''
        line: list[Figure] = self.sorted_figures[ind]
        i = 0
        
        while len(res) < 8:
            if i >= len(line):
                res += FigureCode.Space.value
                x += self.width
                continue

            f = line[i]
            if self.d(f.x, x) <= self.space:
                res += str(f)
                i += 1
            else:
                res += FigureCode.Space.value
            x += self.width

        res = optimize_fen(res)

        self.fen_list[ind] = res
        
        return res

    def process_fen(self):
        for i in range(0, 8):
            self.process_fen_line(i)

    def get_fen(self):
        return '/'.join(self.fen_list)
    
    def get_fen_by_figures(self, figures: "list[Figure]"):
        self.set_figures(figures)
        self.sort_figures()
        self.process_fen()
        return self.get_fen()