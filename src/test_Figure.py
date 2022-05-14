import json
import unittest

from Figure import Color, Figure, FigureCode, FigureEncoder

class TestFigures(unittest.TestCase):
    def test_white_figure_fen_code(self):
        bishop = Figure(FigureCode.Bishop, Color.White, 0, 0, 62, 62)
        self.assertEqual(str(bishop), 'B')

    def test_black_figure_fen_code(self):
        bishop = Figure(FigureCode.King, Color.Black, 0, 0, 62, 62)
        self.assertEqual(str(bishop), 'k')

    def test_serialization(self):
        bishop = Figure(FigureCode.King, Color.Black, 1.0, 0, 62, 62)
        self.assertEqual('{"color": "b", "code": "k", "x": 1, "y": 0, "w": 62, "h": 62}', json.dumps(bishop, cls=FigureEncoder))

if __name__ == '__main__':
    unittest.main()