class LichessExporter:
    def __init__(self, fen: str) -> None:
        self.fen = fen
        self.link_pattern = 'https://lichess.org/analysis/{fen}_{to_move}'

    def white_to_move(self):
        return self.link_pattern.format(fen=self.fen, to_move='w')

    def black_to_move(self):
        return self.link_pattern.format(fen=self.fen, to_move='b')