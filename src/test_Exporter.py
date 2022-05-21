import unittest

from Exporter import LichessExporter

class TestExporter(unittest.TestCase):
    def test_white_to_move(self):
        lichess = LichessExporter('6k1/8/8/5p1p/8/6P1/5PKP/8')
        self.assertEqual(lichess.white_to_move(), 'https://lichess.org/analysis/6k1/8/8/5p1p/8/6P1/5PKP/8_w')

    def test_black_to_move(self):
        lichess = LichessExporter('6k1/8/8/5p1p/8/6P1/5PKP/8')
        self.assertEqual(lichess.black_to_move(), 'https://lichess.org/analysis/6k1/8/8/5p1p/8/6P1/5PKP/8_b')

if __name__ == '__main__':
    unittest.main()