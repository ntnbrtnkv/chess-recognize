import cv2 as cv
import unittest

from Board import Board
from Recognition import Recognition

class TestRecognition(unittest.TestCase):
    def recognize(self, file, expect):
        img = cv.imread(f'examples/{file}.png', cv.IMREAD_UNCHANGED)
        res = Recognition.find_figures(img)
        b = Board()
        self.assertEqual(b.get_fen_by_figures(res), expect)

    def test_example_1(self):
        self.recognize('1', 'rnbkk2r/2p1bppp/p3p3/N1ppP3/3P4/5N2/PPP2PPP/R1BQ1RK1')

    def test_example_2(self):
        self.recognize('2', '6k1/8/8/5p1p/8/6P1/5PKP/8')

    def test_example_3(self):
        self.recognize('3', '3rk2k/pb5p/1p3pn1/2pP1N2/5P2/1P4Q1/P5PK/1B2R3')

    def test_example_5(self):
        self.recognize('5', 'rnb1kbnr/ppp1pppp/8/3q4/8/2N5/PPPP1PPP/R1BQKBNR')

    def test_example_6(self):
        self.recognize('6', '3rk2k/pb5p/1p3pn1/2pP1N2/5P2/1P4Q1/P5PK/1B2R3')