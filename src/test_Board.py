import unittest

from Figure import Color, FigureCode, Figure
from Board import Board

class TestBoard(unittest.TestCase):
    def get_board(self):
        b = Board()
        b.set_figures([
            Figure(FigureCode.Space, Color.White, 20, 67, 62, 62),
            Figure(FigureCode.Space, Color.White, 60, 17, 62, 60)
        ])
        return b

    def test_get_left_coord(self):
        b = self.get_board()
        self.assertEqual(b.get_left_coord(), 20)

    def test_space_with_empty_cells(self):
        b = self.get_board()
        self.assertEqual(b.space, 46.5)

    def test_space_without_empty_cells(self):
        b = Board()
        b.set_figures([
            Figure(FigureCode.King, Color.White, 60, 17, 61, 60),
            Figure(FigureCode.Bishop, Color.White, 20, 67, 62, 62)
        ])
        self.assertEqual(b.space, 45.75)

    def test_first_columt_coords(self):
        b = Board()
        f01 = Figure(FigureCode.King, Color.White, 60, 17, 61, 60)
        f10 = Figure(FigureCode.Bishop, Color.White, 20, 65, 62, 62)
        f11 = Figure(FigureCode.Bishop, Color.White, 64, 67, 61, 62)
        b.set_figures([
            f11,
            f01,
            f10
        ])
        self.assertListEqual(b.sort_figures(), [[f01], [f10, f11], [], [], [], [], [], []])

    def test_process_fen_line(self):
        b = Board()
        f01 = Figure(FigureCode.King, Color.White, 72, 2, 61, 60)
        f10 = Figure(FigureCode.Bishop, Color.Black, 10, 65, 62, 62)
        f11 = Figure(FigureCode.Knight, Color.Black, 74, 67, 61, 62)
        f20 = Figure(FigureCode.Queen, Color.White, 10, 122, 62, 62)
        f21 = Figure(FigureCode.Rook, Color.Black, 127, 122, 61, 62)
        f22 = Figure(FigureCode.Space, Color.Black, 190, 124, 61, 62)
        b.set_figures([
            f11,
            f01,
            f10,
            f20,
            f21,
            f22
        ])
        b.sort_figures()
        self.assertEqual(b.process_fen_line(0), '0K000000')
        self.assertEqual(b.process_fen_line(1), 'bn000000')
        self.assertEqual(b.process_fen_line(2), 'Q0r00000')

if __name__ == '__main__':
    unittest.main()