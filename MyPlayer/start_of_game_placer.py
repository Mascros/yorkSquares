import const
from placer import Placer

class StartOfGamePlacer(Placer):
    def get_move(self, board):
        for edge in const.STARTERS:
            if edge in board.getUnplayedEdges() and self.check_safe(edge, board):
                return edge
        return None